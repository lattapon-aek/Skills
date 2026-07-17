#!/usr/bin/env python3
"""Run and grade behavioral cases with transcript, event, filesystem, and repeat evidence."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import tempfile
import time
from pathlib import Path


SUITE = Path(__file__).resolve().parents[1]
CASES_FILE = SUITE / "tests" / "behavioral" / "cases.json"
FIXTURES_DIR = SUITE / "tests" / "behavioral" / "fixtures"
DIMENSIONS = ("decision", "shape", "evidence", "tool")
PATTERN_CHECKS = ("must_include", "must_include_any", "must_not_include", "ordered")


def pattern_parts(spec: str | dict, default_dimension: str) -> tuple[str, str]:
    if isinstance(spec, str):
        return spec, default_dimension
    if not isinstance(spec, dict) or set(spec) - {"pattern", "dimension"}:
        raise ValueError(f"invalid pattern spec: {spec!r}")
    pattern = spec.get("pattern")
    dimension = spec.get("dimension", default_dimension)
    if not isinstance(pattern, str) or dimension not in DIMENSIONS:
        raise ValueError(f"invalid pattern spec: {spec!r}")
    return pattern, dimension


def load_cases(path: Path) -> list[dict]:
    cases = json.loads(path.read_text(encoding="utf-8"))
    seen: set[str] = set()
    for case in cases:
        for field in ("id", "suite", "prompt", "metrics", "checks"):
            if field not in case:
                raise ValueError(f"case {case.get('id', '<missing id>')} lacks field: {field}")
        if case["id"] in seen:
            raise ValueError(f"duplicate case id: {case['id']}")
        seen.add(case["id"])
        checks = case["checks"]
        prefix = checks.get("must_start_with")
        if prefix is not None:
            pattern_parts(prefix, "shape")
        for key in PATTERN_CHECKS:
            default = "shape" if key == "ordered" else "decision"
            dimensions = set()
            for spec in checks.get(key, []):
                pattern, dimension = pattern_parts(spec, default)
                re.compile(pattern)
                dimensions.add(dimension)
            if key == "must_include_any" and len(dimensions) > 1:
                raise ValueError(f"case {case['id']} must_include_any mixes dimensions")
        if not isinstance(checks.get("forbid_file_change", False), bool):
            raise ValueError(f"case {case['id']} forbid_file_change must be boolean")
    return cases


def first_content_line(text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip().lstrip("#>*-`").strip()
        if stripped:
            return stripped
    return ""


def failure(dimension: str, check: str, message: str) -> dict:
    return {"dimension": dimension, "check": check, "message": message}


def dimensions_for_case(case: dict) -> set[str]:
    checks = case["checks"]
    dimensions: set[str] = set()
    if checks.get("must_start_with") is not None:
        _, dimension = pattern_parts(checks["must_start_with"], "shape")
        dimensions.add(dimension)
    for key in PATTERN_CHECKS:
        default = "shape" if key == "ordered" else "decision"
        for spec in checks.get(key, []):
            _, dimension = pattern_parts(spec, default)
            dimensions.add(dimension)
    if checks.get("forbid_file_change"):
        dimensions.add("tool")
    return dimensions


def grade(case: dict, transcript: str, tool_trace: str = "") -> list[dict]:
    checks = case["checks"]
    failures: list[dict] = []

    prefix_spec = checks.get("must_start_with")
    if prefix_spec is not None:
        prefix, dimension = pattern_parts(prefix_spec, "shape")
        if not first_content_line(transcript).startswith(prefix):
            failures.append(failure(dimension, "must_start_with", f"does not open with {prefix!r}"))

    for spec in checks.get("must_include", []):
        pattern, dimension = pattern_parts(spec, "decision")
        if not re.search(pattern, transcript, re.MULTILINE):
            failures.append(failure(dimension, "must_include", f"no match for /{pattern}/"))

    any_specs = checks.get("must_include_any", [])
    if any_specs:
        parsed = [pattern_parts(spec, "decision") for spec in any_specs]
        if not any(re.search(pattern, transcript, re.MULTILINE) for pattern, _ in parsed):
            failures.append(
                failure(parsed[0][1], "must_include_any", f"no match among {[p for p, _ in parsed]}")
            )

    for spec in checks.get("must_not_include", []):
        pattern, dimension = pattern_parts(spec, "decision")
        match = re.search(pattern, transcript, re.MULTILINE)
        if match:
            snippet = match.group(0)[:80].replace("\n", " ")
            failures.append(failure(dimension, "must_not_include", f"/{pattern}/ matched {snippet!r}"))

    last_position = -1
    for spec in checks.get("ordered", []):
        pattern, dimension = pattern_parts(spec, "shape")
        match = re.search(pattern, transcript, re.MULTILINE)
        if not match:
            failures.append(failure(dimension, "ordered", f"no match for /{pattern}/"))
            break
        if match.start() <= last_position:
            failures.append(failure(dimension, "ordered", f"/{pattern}/ appears out of order"))
            break
        last_position = match.start()

    if checks.get("forbid_file_change") and re.search(
        r"(?im)^file_change\b|^filesystem_change\b|patch rejected: writing is blocked",
        tool_trace,
    ):
        failures.append(
            failure("tool", "forbid_file_change", "observed a file-change attempt or filesystem delta")
        )
    return failures


def dimension_statuses(case: dict, failures: list[dict], blocked: bool = False) -> dict[str, str]:
    applicable = dimensions_for_case(case)
    failed = {item["dimension"] for item in failures}
    return {
        dimension: "blocked" if blocked else ("fail" if dimension in failed else "pass")
        for dimension in sorted(applicable)
    }


def summarize_metrics(results: dict[str, dict]) -> dict[str, dict]:
    metrics: dict[str, dict] = {}
    for result in results.values():
        if result["status"] == "missing":
            continue
        for name in result["metrics"]:
            entry = metrics.setdefault(name, {"cases": 0, "failed": 0})
            entry["cases"] += 1
            if result["status"] != "pass":
                entry["failed"] += 1
    for name, entry in sorted(metrics.items()):
        passed = entry["cases"] - entry["failed"]
        entry["value"] = round(
            entry["failed"] / entry["cases"] if name.endswith("_rate") else passed / entry["cases"],
            3,
        )
    return metrics


def summarize_dimensions(results: dict[str, dict]) -> dict[str, dict]:
    summary: dict[str, dict] = {}
    for result in results.values():
        for dimension, status in result.get("dimensions", {}).items():
            entry = summary.setdefault(dimension, {"cases": 0, "passed": 0, "blocked": 0})
            entry["cases"] += 1
            entry["passed"] += status == "pass"
            entry["blocked"] += status == "blocked"
    for entry in summary.values():
        entry["value"] = round(entry["passed"] / entry["cases"], 3)
    return summary


def find_transcript(directory: Path, case_id: str) -> Path | None:
    for suffix in (".md", ".txt"):
        candidate = directory / f"{case_id}{suffix}"
        if candidate.is_file():
            return candidate
    return None


def event_artifact(transcript: Path, suffix: str) -> Path:
    return transcript.with_name(f"{transcript.stem}.{suffix}")


def parse_event_stream(raw: str) -> tuple[str, str]:
    messages: list[str] = []
    trace: list[str] = []
    for line in raw.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        item = event.get("item") or {}
        item_type = item.get("type")
        if event.get("type") == "item.completed" and item_type == "agent_message":
            messages.append(item.get("text", ""))
        if event.get("type") == "item.started" and item_type:
            detail = item.get("command", "") if item_type == "command_execution" else ""
            trace.append(f"{item_type} {detail}".rstrip())
    return (messages[-1] if messages else "", "\n".join(trace))


def snapshot_tree(root: Path) -> dict[str, str]:
    snapshot: dict[str, str] = {}
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if ".git" in relative.parts:
            continue
        key = relative.as_posix()
        if path.is_symlink():
            snapshot[key] = f"symlink:{os.readlink(path)}"
        elif path.is_dir():
            snapshot[key] = "directory"
        elif path.is_file():
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            snapshot[key] = f"file:{path.stat().st_size}:{digest}"
    return snapshot


def diff_snapshots(before: dict[str, str], after: dict[str, str]) -> dict[str, list[str]]:
    return {
        "added": sorted(after.keys() - before.keys()),
        "modified": sorted(key for key in before.keys() & after.keys() if before[key] != after[key]),
        "deleted": sorted(before.keys() - after.keys()),
    }


def load_tool_trace(transcript: Path) -> str:
    parts: list[str] = []
    events = event_artifact(transcript, "events.jsonl")
    stderr = event_artifact(transcript, "stderr.txt")
    filesystem = event_artifact(transcript, "filesystem.json")
    if events.is_file():
        _, trace = parse_event_stream(events.read_text(encoding="utf-8"))
        parts.append(trace)
    if stderr.is_file():
        parts.append(stderr.read_text(encoding="utf-8"))
    if filesystem.is_file():
        delta = json.loads(filesystem.read_text(encoding="utf-8"))
        for kind in ("added", "modified", "deleted"):
            for path in delta.get(kind, []):
                parts.append(f"filesystem_change {kind} {path}")
    return "\n".join(parts)


def terminate_process_tree(process: subprocess.Popen) -> bool:
    if process.poll() is not None:
        return False
    if os.name == "posix":
        os.killpg(process.pid, signal.SIGTERM)
        try:
            process.wait(timeout=2)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            process.wait(timeout=2)
    elif os.name == "nt":
        subprocess.run(
            ["taskkill", "/PID", str(process.pid), "/T", "/F"],
            capture_output=True,
            check=False,
        )
        process.wait(timeout=5)
    else:
        process.kill()
        process.wait(timeout=2)
    return True


def run_agent(
    template: str,
    prompt: str,
    out_file: Path,
    *,
    json_events: bool = False,
    timeout_seconds: float | None = 180,
    workspace: Path | None = None,
    case_id: str = "",
    run_index: int = 1,
) -> dict:
    prompt_file: Path | None = None
    stdin_input: str | None = None
    command = template.replace("{case_id}", case_id).replace("{run_index}", str(run_index))
    if workspace is not None:
        command = command.replace("{workspace}", str(workspace))
    if "{prompt_file}" in command:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".md", delete=False) as handle:
            handle.write(prompt)
            prompt_file = Path(handle.name)
        command = command.replace("{prompt_file}", str(prompt_file))
    else:
        stdin_input = prompt

    before = snapshot_tree(workspace) if workspace is not None else None
    started = time.monotonic()
    timed_out = False
    tree_terminated = False
    stdout = ""
    stderr = ""
    process: subprocess.Popen | None = None
    try:
        popen_kwargs = {
            "shell": True,
            "stdin": subprocess.PIPE,
            "stdout": subprocess.PIPE,
            "stderr": subprocess.PIPE,
            "text": True,
            "encoding": "utf-8",
            "start_new_session": os.name == "posix",
        }
        if os.name == "nt":
            popen_kwargs["creationflags"] = subprocess.CREATE_NEW_PROCESS_GROUP
        process = subprocess.Popen(command, **popen_kwargs)
        try:
            stdout, stderr = process.communicate(input=stdin_input, timeout=timeout_seconds)
        except subprocess.TimeoutExpired:
            timed_out = True
            tree_terminated = terminate_process_tree(process)
            stdout, stderr = process.communicate()
    finally:
        if prompt_file is not None:
            prompt_file.unlink(missing_ok=True)

    duration = round(time.monotonic() - started, 3)
    returncode = process.returncode if process is not None else None
    if json_events:
        transcript, _ = parse_event_stream(stdout or "")
        out_file.write_text(transcript, encoding="utf-8")
        event_artifact(out_file, "events.jsonl").write_text(stdout or "", encoding="utf-8")
    else:
        out_file.write_text(stdout or "", encoding="utf-8")
    event_artifact(out_file, "stderr.txt").write_text(stderr or "", encoding="utf-8")

    if workspace is not None and before is not None:
        delta = diff_snapshots(before, snapshot_tree(workspace))
        event_artifact(out_file, "filesystem.json").write_text(
            json.dumps(delta, indent=2, ensure_ascii=False), encoding="utf-8"
        )

    metadata = {
        "command": command,
        "duration_seconds": duration,
        "returncode": returncode,
        "timed_out": timed_out,
        "process_tree_terminated": tree_terminated,
    }
    event_artifact(out_file, "run.json").write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    return metadata


def load_run_metadata(transcript: Path) -> dict:
    path = event_artifact(transcript, "run.json")
    return json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}


def grade_directory(cases: list[dict], directory: Path) -> dict[str, dict]:
    results: dict[str, dict] = {}
    for case in cases:
        transcript_path = find_transcript(directory, case["id"])
        if transcript_path is None:
            results[case["id"]] = {
                "status": "missing",
                "metrics": case["metrics"],
                "failures": [],
                "dimensions": {dimension: "missing" for dimension in dimensions_for_case(case)},
            }
            continue
        metadata = load_run_metadata(transcript_path)
        failures = grade(
            case,
            transcript_path.read_text(encoding="utf-8"),
            load_tool_trace(transcript_path),
        )
        execution_status = None
        if metadata.get("timed_out"):
            execution_status = "timeout"
        elif metadata.get("returncode") not in (None, 0):
            execution_status = "error"
        status = execution_status or ("pass" if not failures else "fail")
        results[case["id"]] = {
            "status": status,
            "metrics": case["metrics"],
            "failures": failures,
            "dimensions": dimension_statuses(case, failures, blocked=execution_status is not None),
            "execution": metadata,
        }
    return results


def print_report(results: dict[str, dict], metrics: dict[str, dict], dimensions: dict[str, dict]) -> None:
    for case_id, result in results.items():
        labels = " ".join(f"{key}:{value}" for key, value in result["dimensions"].items())
        print(f"[{result['status'].upper():7}] {case_id} [{labels}]")
        for item in result["failures"]:
            print(f"          - {item['dimension']}/{item['check']}: {item['message']}")
    counts = {status: sum(r["status"] == status for r in results.values()) for status in ("pass", "fail", "timeout", "error", "missing")}
    print("\ncases: " + ", ".join(f"{count} {status}" for status, count in counts.items()))
    if dimensions:
        print("dimensions:")
        for name, entry in sorted(dimensions.items()):
            print(f"  {name}: {entry['value']} ({entry['passed']}/{entry['cases']} pass; {entry['blocked']} blocked)")
    if metrics:
        print("metrics:")
        for name, entry in sorted(metrics.items()):
            print(f"  {name}: {entry['value']} ({entry['cases'] - entry['failed']}/{entry['cases']} pass)")


def summarize_stability(run_results: list[dict[str, dict]]) -> dict[str, dict]:
    stability: dict[str, dict] = {}
    for case_id in run_results[0]:
        statuses = [results[case_id]["status"] for results in run_results]
        if all(status == "pass" for status in statuses):
            classification = "stable_pass"
        elif all(status == "fail" for status in statuses):
            classification = "stable_fail"
        elif len(set(statuses)) == 1:
            classification = f"stable_{statuses[0]}"
        else:
            classification = "flaky"
        stability[case_id] = {
            "classification": classification,
            "statuses": statuses,
            "pass_frequency": round(statuses.count("pass") / len(statuses), 3),
        }
    return stability


def aggregate_values(items: list[dict[str, dict]]) -> dict[str, dict]:
    names = sorted({name for item in items for name in item})
    aggregate: dict[str, dict] = {}
    for name in names:
        values = [item[name]["value"] for item in items if name in item]
        aggregate[name] = {
            "mean": round(sum(values) / len(values), 3),
            "min": min(values),
            "max": max(values),
        }
    return aggregate


def self_test(cases: list[dict]) -> int:
    by_id = {case["id"]: case for case in cases}
    fixtures = sorted(FIXTURES_DIR.glob("*.md"))
    problems: list[str] = []
    checked = 0
    for fixture in fixtures:
        stem = fixture.name[:-3]
        if stem.endswith(".good"):
            case_id, expect_pass = stem[:-5], True
        elif stem.endswith(".bad"):
            case_id, expect_pass = stem[:-4], False
        else:
            problems.append(f"{fixture.name}: expected .good.md or .bad.md")
            continue
        case = by_id.get(case_id)
        if case is None:
            problems.append(f"{fixture.name}: no case with id {case_id}")
            continue
        failures = grade(case, fixture.read_text(encoding="utf-8"), load_tool_trace(fixture))
        checked += 1
        if expect_pass and failures:
            problems.append(f"{fixture.name}: expected pass, got {failures}")
        if not expect_pass and not failures:
            problems.append(f"{fixture.name}: expected at least one failure")
    for problem in problems:
        print(f"self-test failed: {problem}", file=sys.stderr)
    if problems:
        return 1
    print(f"behavioral eval self-test passed: {len(cases)} cases valid, {checked} fixtures graded")
    return 0


def prepare_workspace(template: Path, root: Path, run_index: int, case_id: str) -> Path:
    workspace = root / f"run-{run_index:02d}" / case_id
    workspace.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(template, workspace, symlinks=True)
    return workspace


def run_case_set(cases: list[dict], args: argparse.Namespace, out_dir: Path, run_index: int) -> dict[str, dict]:
    out_dir.mkdir(parents=True, exist_ok=True)
    workspace_root = args.workspace_root or (args.out / ".workspaces")
    for case in cases:
        print(f"running agent for {case['id']} (run {run_index}/{args.repeat}) ...")
        workspace = None
        if args.workspace_template:
            workspace = prepare_workspace(args.workspace_template, workspace_root, run_index, case["id"])
        try:
            metadata = run_agent(
                args.agent_cmd,
                case["prompt"],
                out_dir / f"{case['id']}.md",
                json_events=args.json_events,
                timeout_seconds=None if args.timeout_seconds == 0 else args.timeout_seconds,
                workspace=workspace,
                case_id=case["id"],
                run_index=run_index,
            )
            if metadata["timed_out"]:
                print(f"agent timed out for {case['id']}", file=sys.stderr)
            elif metadata["returncode"] != 0:
                print(f"agent exited {metadata['returncode']} for {case['id']}", file=sys.stderr)
        finally:
            if workspace is not None and not args.keep_workspaces:
                shutil.rmtree(workspace)
    return grade_directory(cases, out_dir)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", type=Path, default=CASES_FILE)
    parser.add_argument("--transcripts", type=Path)
    parser.add_argument("--agent-cmd", help="shell template; supports {prompt_file}, {case_id}, {run_index}, {workspace}")
    parser.add_argument("--out", type=Path)
    parser.add_argument("--json-events", action="store_true")
    parser.add_argument("--timeout-seconds", type=float, default=180)
    parser.add_argument("--repeat", type=int, default=1)
    parser.add_argument("--workspace-template", type=Path)
    parser.add_argument("--workspace-root", type=Path)
    parser.add_argument("--keep-workspaces", action="store_true")
    parser.add_argument("--case-id", action="append")
    parser.add_argument("--report", type=Path)
    parser.add_argument("--require-all", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.repeat < 1 or args.timeout_seconds < 0:
        parser.error("--repeat must be >= 1 and --timeout-seconds must be >= 0")
    cases = load_cases(args.cases)
    if args.case_id:
        wanted = set(args.case_id)
        unknown = wanted - {case["id"] for case in cases}
        if unknown:
            parser.error(f"unknown case ids: {sorted(unknown)}")
        cases = [case for case in cases if case["id"] in wanted]
    if args.self_test:
        return self_test(cases)
    if args.json_events and not args.agent_cmd:
        parser.error("--json-events requires --agent-cmd")
    if args.repeat > 1 and not args.agent_cmd:
        parser.error("--repeat > 1 requires --agent-cmd")
    if args.workspace_template:
        if not args.agent_cmd or "{workspace}" not in args.agent_cmd:
            parser.error("--workspace-template requires --agent-cmd with {workspace}")
        if not args.workspace_template.is_dir():
            parser.error("--workspace-template must be a directory")
    elif args.agent_cmd and "{workspace}" in args.agent_cmd:
        parser.error("{workspace} requires --workspace-template")

    run_payloads: list[dict] = []
    if args.agent_cmd:
        args.out = args.out or Path(tempfile.mkdtemp(prefix="behavioral-eval-"))
        for run_index in range(1, args.repeat + 1):
            run_dir = args.out if args.repeat == 1 else args.out / f"run-{run_index:02d}"
            results = run_case_set(cases, args, run_dir, run_index)
            metrics = summarize_metrics(results)
            dimensions = summarize_dimensions(results)
            print_report(results, metrics, dimensions)
            run_payloads.append({"index": run_index, "cases": results, "metrics": metrics, "dimensions": dimensions})
        print(f"artifacts written to {args.out}")
    elif args.transcripts:
        results = grade_directory(cases, args.transcripts)
        metrics = summarize_metrics(results)
        dimensions = summarize_dimensions(results)
        print_report(results, metrics, dimensions)
        run_payloads.append({"index": 1, "cases": results, "metrics": metrics, "dimensions": dimensions})
    else:
        parser.error("choose --transcripts, --agent-cmd, or --self-test")

    stability = summarize_stability([payload["cases"] for payload in run_payloads])
    report = {
        "schema_version": 2,
        "runs": run_payloads,
        "stability": stability,
        "aggregate_metrics": aggregate_values([payload["metrics"] for payload in run_payloads]),
        "aggregate_dimensions": aggregate_values([payload["dimensions"] for payload in run_payloads]),
    }
    if len(run_payloads) == 1:
        report.update({key: run_payloads[0][key] for key in ("cases", "metrics", "dimensions")})
    if args.report:
        args.report.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"report written to {args.report}")

    statuses = [result["status"] for payload in run_payloads for result in payload["cases"].values()]
    failed = any(status in {"fail", "timeout", "error"} for status in statuses)
    missing = any(status == "missing" for status in statuses)
    return 1 if failed or (missing and args.require_all) else 0


if __name__ == "__main__":
    raise SystemExit(main())
