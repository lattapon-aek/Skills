#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

validate_py="${SKILL_VALIDATE_PY:-/Users/lattapon/.codex/skills/.system/skill-creator/scripts/quick_validate.py}"

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

echo "== node fixtures =="
node --test suites/software-engineering/tests/software-engineering-core/flows/sample-app/src/payments/retry-status-mapper.test.ts
node --test suites/software-engineering/tests/change-review/scenario-3/base/src/openai/support-assistant.test.ts

echo "== suite structure =="
test -f suites/software-engineering/tests/golden-transcripts/cases.md
test -f suites/software-engineering/tests/internet-derived/cases.md
test -f suites/software-engineering/tests/mini-stress/cases.md
test -f suites/software-engineering/tests/verification-hazards/cases.md

echo "== registration =="
grep -q "verification-hazards" .claude-plugin/plugin.json
grep -q "verification-hazards" scripts/link-codex-skills.ps1
grep -q "verification-hazards" scripts/link-software-engineering-skills.ps1
grep -q "verification-hazards" README.md
grep -q "golden-transcripts" suites/software-engineering/README.md
grep -q "internet-derived" suites/software-engineering/README.md
grep -q "mini-stress" suites/software-engineering/README.md

echo "== stale routing scan =="
if grep -R "clarify/analyze/implement/review" suites/software-engineering README.md AGENTS.md CLAUDE.md >/dev/null 2>&1; then
  echo "stale flow wording found: clarify/analyze/implement/review" >&2
  exit 1
fi

echo "suite validation passed"
