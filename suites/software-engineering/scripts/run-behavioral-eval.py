#!/usr/bin/env python3
"""Grade agent transcripts against the suite's behavioral cases.

Modes:
  --transcripts DIR   Grade <case-id>.md or <case-id>.txt transcripts found in DIR.
  --agent-cmd TMPL    Run each case prompt through an agent command, then grade.
                      TMPL runs through the shell; {prompt_file} is replaced with
                      the path of a UTF-8 file containing the case prompt.
  --self-test         Validate cases.json and grade the bundled good/bad fixture
                      transcripts; good must pass, bad must fail.

Check semantics (tests/behavioral/cases.json):
  must_start_with   Plain prefix the first non-empty content line must start with.
  must_include      Python regexes; every pattern must match somewhere.
  must_include_any  Python regexes; at least one must match.
  must_not_include  Python regexes; none may match.
  ordered           Python regexes; all must match with strictly increasing
                    first-match positions.
Patterns are case-sensitive unless they opt in with (?i).

Exit code is 1 when any graded case fails, when a fixture expectation is not
met in --self-test, or when --require-all is set and a transcript is missing.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

SUITE = Path(__file__).resolve().parents[1]
CASES_FILE = SUITE / "tests" / "behavioral" / "cases.json"
FIXTURES_DIR = SUITE / "tests" / "behavioral" / "fixtures"


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
        for key in ("must_include", "must_include_any", "must_not_include", "ordered"):
            for pattern in case["checks"].get(key, []):
                re.compile(pattern)
    return cases


def first_content_line(text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip().lstrip("#>*-`").strip()
        if stripped:
            return stripped
    return ""


def grade(case: dict, transcript: str) -> list[str]:
    checks = case["checks"]
    failures: list[str] = []

    prefix = checks.get("must_start_with")
    if prefix and not first_content_line(transcript).startswith(prefix):
        failures.append(f"must_start_with: transcript does not open with '{prefix}'")

    for pattern in checks.get("must_include", []):
        if not re.search(pattern, transcript, re.MULTILINE):
            failures.append(f"must_include: no match for /{pattern}/")

    any_patterns = checks.get("must_include_any", [])
    if any_patterns and not any(
        re.search(pattern, transcript, re.MULTILINE) for pattern in any_patterns
    ):
        failures.append(f"must_include_any: no match among {any_patterns}")

    for pattern in checks.get("must_not_include", []):
        match = re.search(pattern, transcript, re.MULTILINE)
        if match:
            snippet = match.group(0)[:80].replace("\n", " ")
            failures.append(f"must_not_include: /{pattern}/ matched '{snippet}'")

    last_position = -1
    for pattern in checks.get("ordered", []):
        match = re.search(pattern, transcript, re.MULTILINE)
        if not match:
            failures.append(f"ordered: no match for /{pattern}/")
            break
        if match.start() <= last_position:
            failures.append(f"ordered: /{pattern}/ appears out of order")
            break
        last_position = match.start()

    return failures


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
        if name.endswith("_rate"):
            entry["value"] = round(entry["failed"] / entry["cases"], 3)
        else:
            entry["value"] = round((entry["cases"] - entry["failed"]) / entry["cases"], 3)
    return metrics


def find_transcript(directory: Path, case_id: str) -> Path | None:
    for suffix in (".md", ".txt"):
        candidate = directory / f"{case_id}{suffix}"
        if candidate.is_file():
            return candidate
    return None


def run_agent(template: str, prompt: str, out_file: Path) -> None:
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", suffix=".md", delete=False
    ) as handle:
        handle.write(prompt)
        prompt_file = Path(handle.name)
    try:
        command = template.replace("{prompt_file}", str(prompt_file))
        completed = subprocess.run(
            command, shell=True, capture_output=True, text=True, encoding="utf-8"
        )
        out_file.write_text(completed.stdout or "", encoding="utf-8")
        if completed.returncode != 0:
            print(
                f"agent command exited {completed.returncode} for {out_file.stem}: "
                f"{(completed.stderr or '')[:200]}",
                file=sys.stderr,
            )
    finally:
        prompt_file.unlink(missing_ok=True)


def grade_directory(cases: list[dict], directory: Path) -> dict[str, dict]:
    results: dict[str, dict] = {}
    for case in cases:
        transcript_path = find_transcript(directory, case["id"])
        if transcript_path is None:
            results[case["id"]] = {"status": "missing", "metrics": case["metrics"], "failures": []}
            continue
        failures = grade(case, transcript_path.read_text(encoding="utf-8"))
        results[case["id"]] = {
            "status": "pass" if not failures else "fail",
            "metrics": case["metrics"],
            "failures": failures,
        }
    return results


def print_report(results: dict[str, dict], metrics: dict[str, dict]) -> None:
    for case_id, result in results.items():
        print(f"[{result['status'].upper():7}] {case_id}")
        for failure in result["failures"]:
            print(f"          - {failure}")
    passed = sum(1 for r in results.values() if r["status"] == "pass")
    failed = sum(1 for r in results.values() if r["status"] == "fail")
    missing = sum(1 for r in results.values() if r["status"] == "missing")
    print(f"\ncases: {passed} pass, {failed} fail, {missing} missing")
    if metrics:
        print("metrics:")
        for name, entry in sorted(metrics.items()):
            print(f"  {name}: {entry['value']} ({entry['cases'] - entry['failed']}/{entry['cases']} pass)")


def self_test(cases: list[dict]) -> int:
    by_id = {case["id"]: case for case in cases}
    fixtures = sorted(FIXTURES_DIR.glob("*.md"))
    if not fixtures:
        print("self-test failed: no fixture transcripts found", file=sys.stderr)
        return 1

    problems: list[str] = []
    checked = 0
    for fixture in fixtures:
        stem = fixture.name[: -len(".md")]
        if stem.endswith(".good"):
            case_id, expect_pass = stem[: -len(".good")], True
        elif stem.endswith(".bad"):
            case_id, expect_pass = stem[: -len(".bad")], False
        else:
            problems.append(f"{fixture.name}: fixture name must end in .good.md or .bad.md")
            continue
        case = by_id.get(case_id)
        if case is None:
            problems.append(f"{fixture.name}: no case with id {case_id}")
            continue
        failures = grade(case, fixture.read_text(encoding="utf-8"))
        checked += 1
        if expect_pass and failures:
            problems.append(f"{fixture.name}: expected pass, got failures: {failures}")
        if not expect_pass and not failures:
            problems.append(f"{fixture.name}: expected at least one failure, got a clean pass")

    for problem in problems:
        print(f"self-test failed: {problem}", file=sys.stderr)
    if problems:
        return 1
    print(f"behavioral eval self-test passed: {len(cases)} cases valid, {checked} fixtures graded")
    return 0


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", type=Path, default=CASES_FILE)
    parser.add_argument("--transcripts", type=Path, help="directory of transcripts to grade")
    parser.add_argument("--agent-cmd", help="shell command template; {prompt_file} is replaced")
    parser.add_argument("--out", type=Path, help="transcript output directory for --agent-cmd")
    parser.add_argument("--case-id", action="append", help="limit the run to these case ids")
    parser.add_argument("--report", type=Path, help="write a JSON report to this path")
    parser.add_argument("--require-all", action="store_true", help="missing transcripts fail the run")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    cases = load_cases(args.cases)
    if args.case_id:
        wanted = set(args.case_id)
        unknown = wanted - {case["id"] for case in cases}
        if unknown:
            parser.error(f"unknown case ids: {sorted(unknown)}")
        cases = [case for case in cases if case["id"] in wanted]

    if args.self_test:
        return self_test(cases)

    if args.agent_cmd:
        out_dir = args.out or Path(tempfile.mkdtemp(prefix="behavioral-eval-"))
        out_dir.mkdir(parents=True, exist_ok=True)
        for case in cases:
            print(f"running agent for {case['id']} ...")
            run_agent(args.agent_cmd, case["prompt"], out_dir / f"{case['id']}.md")
        print(f"transcripts written to {out_dir}")
        transcripts_dir = out_dir
    elif args.transcripts:
        transcripts_dir = args.transcripts
    else:
        parser.error("choose one of --transcripts, --agent-cmd, or --self-test")
        return 2

    results = grade_directory(cases, transcripts_dir)
    metrics = summarize_metrics(results)
    print_report(results, metrics)

    if args.report:
        args.report.write_text(
            json.dumps({"cases": results, "metrics": metrics}, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        print(f"report written to {args.report}")

    failed = any(result["status"] == "fail" for result in results.values())
    missing = any(result["status"] == "missing" for result in results.values())
    return 1 if failed or (missing and args.require_all) else 0


if __name__ == "__main__":
    raise SystemExit(main())
