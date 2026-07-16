#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

if [[ -n "${SKILL_VALIDATE_PY:-}" ]]; then
  validate_py="$SKILL_VALIDATE_PY"
else
  codex_home="${CODEX_HOME:-${HOME:-}/.codex}"
  validate_py="$codex_home/skills/.system/skill-creator/scripts/quick_validate.py"
fi

if [[ ! -f "$validate_py" ]]; then
  echo "missing quick_validate.py: $validate_py" >&2
  exit 1
fi

run_python() {
  if command -v pyenv >/dev/null 2>&1 && pyenv versions --bare 2>/dev/null | grep -qx "3.12.2"; then
    PYENV_VERSION=3.12.2 pyenv exec python "$@"
  elif command -v python3 >/dev/null 2>&1; then
    python3 "$@"
  else
    python "$@"
  fi
}

echo "== skill validation =="
run_python "$validate_py" suites/software-engineering/skills/software-engineering-core
run_python "$validate_py" suites/software-engineering/skills/change-review
run_python "$validate_py" suites/software-engineering/skills/verification-hazards

echo "== skill architecture =="
run_python suites/software-engineering/scripts/check-skill-architecture.py

echo "== node fixtures =="
node --test $(find suites/software-engineering/tests -name '*.test.ts' -print | sort)

echo "== suite structure =="
test -f suites/software-engineering/tests/golden-transcripts/cases.md
test -f suites/software-engineering/tests/internet-derived/cases.md
test -f suites/software-engineering/tests/mini-stress/cases.md
test -f suites/software-engineering/tests/verification-hazards/cases.md
test -f suites/software-engineering/skills/software-engineering-core/references/causal-debugging-protocol.md
test -f suites/software-engineering/scripts/check-skill-architecture.py

echo "== registration =="
grep -q "verification-hazards" .claude-plugin/plugin.json
grep -q "verification-hazards" scripts/link-codex-skills.ps1
grep -q "verification-hazards" scripts/link-software-engineering-skills.ps1
grep -q "verification-hazards" README.md
grep -q "golden-transcripts" suites/software-engineering/README.md
grep -q "internet-derived" suites/software-engineering/README.md
grep -q "mini-stress" suites/software-engineering/README.md
grep -q "## Preflight" suites/software-engineering/references/orchestration-policy.md
grep -q "Authority Mode" suites/software-engineering/skills/software-engineering-core/SKILL.md
grep -q "Acceptance Coverage" suites/software-engineering/skills/change-review/SKILL.md
grep -q "Weak-Oracle Green" suites/software-engineering/skills/verification-hazards/SKILL.md
grep -q "Weak-Oracle Green" suites/software-engineering/tests/verification-hazards/cases.md
grep -q "Evidence Before Action" suites/software-engineering/references/four-principles.md
grep -q "Smallest Sufficient Change" suites/software-engineering/references/four-principles.md
grep -q "Proven Change Boundary" suites/software-engineering/references/four-principles.md
grep -q "Requirement-to-Proof Closure" suites/software-engineering/references/four-principles.md
grep -q "Root-Cause Gate" suites/software-engineering/skills/software-engineering-core/references/causal-debugging-protocol.md
grep -q "Hypothesis Ledger" suites/software-engineering/skills/software-engineering-core/references/causal-debugging-protocol.md
grep -q "Original-Reproduction Replay" suites/software-engineering/skills/software-engineering-core/references/causal-debugging-protocol.md
grep -q "Do Not Patch The Symptom" suites/software-engineering/tests/software-engineering-core/analysis/cases.md
grep -q "The First Plausible Cause Wins" suites/software-engineering/tests/mini-stress/cases.md
grep -q "Intent-to-Outcome Conformance" suites/software-engineering/skills/software-engineering-core/SKILL.md
grep -q "working but nonconforming" suites/software-engineering/skills/verification-hazards/SKILL.md
grep -q "Intent-Conformance Gate" suites/software-engineering/skills/change-review/SKILL.md
grep -q "Working But Plan-Divergent" suites/software-engineering/tests/golden-transcripts/cases.md
grep -q "Working But Nonconforming Green" suites/software-engineering/tests/verification-hazards/cases.md

echo "== stale routing scan =="
if grep -R "clarify/analyze/implement/review" suites/software-engineering README.md AGENTS.md CLAUDE.md >/dev/null 2>&1; then
  echo "stale flow wording found: clarify/analyze/implement/review" >&2
  exit 1
fi

if grep -R -E "The Five Hazards|the five hazards|all five gates|five repeatable ways" suites/software-engineering/skills suites/software-engineering/references suites/software-engineering/tests suites/software-engineering/README.md >/dev/null 2>&1; then
  echo "stale five-hazard wording found" >&2
  exit 1
fi

if grep -R -E "Think Before Coding|Simplicity First|Surgical Changes|Goal-Driven Execution" suites/software-engineering/skills suites/software-engineering/references suites/software-engineering/tests suites/software-engineering/README.md >/dev/null 2>&1; then
  echo "stale vague-principle wording found" >&2
  exit 1
fi

if grep -R "Phase Handoff" suites/software-engineering/skills suites/software-engineering/references suites/software-engineering/tests suites/software-engineering/README.md >/dev/null 2>&1; then
  echo "stale section name found: Phase Handoff (the section is named Handoff)" >&2
  exit 1
fi

echo "suite validation passed"
