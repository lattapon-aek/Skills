#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import os
import shlex
import signal
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[4]
RUNNER = REPO / "suites" / "software-engineering" / "scripts" / "run-behavioral-eval.py"
SPEC = importlib.util.spec_from_file_location("behavioral_eval", RUNNER)
assert SPEC and SPEC.loader
behavioral_eval = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(behavioral_eval)


class BehavioralEvalTests(unittest.TestCase):
    def test_dimensions_remain_independent(self) -> None:
        case = {
            "checks": {
                "must_start_with": "Claim Under Test",
                "must_include": [
                    "still a lead",
                    {"pattern": "git show", "dimension": "evidence"},
                ],
                "forbid_file_change": True,
            }
        }
        failures = behavioral_eval.grade(case, "still a lead", "")
        self.assertEqual({item["dimension"] for item in failures}, {"shape", "evidence"})
        self.assertEqual(
            behavioral_eval.dimension_statuses(case, failures),
            {"decision": "pass", "evidence": "fail", "shape": "fail", "tool": "pass"},
        )

    def test_snapshot_detects_shell_visible_changes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "kept.txt").write_text("before", encoding="utf-8")
            before = behavioral_eval.snapshot_tree(root)
            (root / "kept.txt").write_text("after", encoding="utf-8")
            (root / "added.txt").write_text("new", encoding="utf-8")
            delta = behavioral_eval.diff_snapshots(before, behavioral_eval.snapshot_tree(root))
        self.assertEqual(delta["added"], ["added.txt"])
        self.assertEqual(delta["modified"], ["kept.txt"])
        self.assertEqual(delta["deleted"], [])

    @unittest.skipUnless(os.name == "posix", "POSIX process-group assertion")
    def test_timeout_terminates_descendant_process(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            helper = root / "parent.py"
            pid_file = root / "child.pid"
            transcript = root / "case.md"
            helper.write_text(
                "import pathlib, subprocess, sys, time\n"
                "child = subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(30)'])\n"
                "pathlib.Path(sys.argv[1]).write_text(str(child.pid))\n"
                "time.sleep(30)\n",
                encoding="utf-8",
            )
            command = f"{shlex.quote(sys.executable)} {shlex.quote(str(helper))} {shlex.quote(str(pid_file))}"
            metadata = behavioral_eval.run_agent(
                command,
                "",
                transcript,
                timeout_seconds=0.4,
            )
            self.assertTrue(metadata["timed_out"])
            self.assertTrue(metadata["process_tree_terminated"])
            result = behavioral_eval.grade_directory(
                [{"id": "case", "metrics": [], "checks": {"must_include": ["never"]}}],
                root,
            )["case"]
            self.assertEqual(result["status"], "timeout")
            self.assertEqual(result["dimensions"], {"decision": "blocked"})
            child_pid = int(pid_file.read_text(encoding="utf-8"))
            try:
                for _ in range(20):
                    state = subprocess.run(
                        ["ps", "-o", "stat=", "-p", str(child_pid)],
                        capture_output=True,
                        text=True,
                        check=False,
                    ).stdout.strip()
                    if not state or state.startswith("Z"):
                        break
                    time.sleep(0.05)
                self.assertTrue(not state or state.startswith("Z"), f"descendant still running: {state}")
            finally:
                try:
                    os.kill(child_pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass

    def test_nonzero_exit_is_command_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            transcript = root / "case.md"
            behavioral_eval.run_agent(
                f'{shlex.quote(sys.executable)} -c "raise SystemExit(7)"',
                "",
                transcript,
            )
            result = behavioral_eval.grade_directory(
                [{"id": "case", "metrics": [], "checks": {"must_include": ["never"]}}],
                root,
            )["case"]
            self.assertEqual(result["status"], "error")
            self.assertEqual(result["execution"]["returncode"], 7)
            self.assertEqual(result["dimensions"], {"decision": "blocked"})

    def test_workspace_oracle_rejects_non_event_file_change(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory) / "workspace"
            workspace.mkdir()
            transcript = Path(directory) / "case.md"
            command = (
                f"cd \"{{workspace}}\" && {shlex.quote(sys.executable)} -c "
                '"from pathlib import Path; Path(\'shell-created.txt\').write_text(\'x\')"'
            )
            behavioral_eval.run_agent(command, "", transcript, workspace=workspace)
            trace = behavioral_eval.load_tool_trace(transcript)
            failures = behavioral_eval.grade(
                {"checks": {"forbid_file_change": True}},
                "",
                trace,
            )
            self.assertIn("filesystem_change added shell-created.txt", trace)
            self.assertEqual(failures[0]["dimension"], "tool")

    def test_repeat_cli_emits_stability(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            cases = root / "cases.json"
            helper = root / "agent.py"
            output = root / "out"
            report = root / "report.json"
            cases.write_text(
                json.dumps([
                    {
                        "id": "repeat-case",
                        "suite": "test",
                        "prompt": "prompt",
                        "metrics": ["routing_accuracy"],
                        "checks": {"must_include": ["OK"]},
                    }
                ]),
                encoding="utf-8",
            )
            helper.write_text("import sys\nsys.stdin.read()\nprint('OK')\n", encoding="utf-8")
            completed = subprocess.run(
                [
                    sys.executable,
                    str(RUNNER),
                    "--cases",
                    str(cases),
                    "--agent-cmd",
                    f"{shlex.quote(sys.executable)} {shlex.quote(str(helper))}",
                    "--repeat",
                    "2",
                    "--out",
                    str(output),
                    "--report",
                    str(report),
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            payload = json.loads(report.read_text(encoding="utf-8"))
            self.assertEqual(len(payload["runs"]), 2)
            self.assertEqual(payload["stability"]["repeat-case"]["classification"], "stable_pass")
            self.assertTrue((output / "run-01" / "repeat-case.md").is_file())
            self.assertTrue((output / "run-02" / "repeat-case.md").is_file())


if __name__ == "__main__":
    unittest.main()
