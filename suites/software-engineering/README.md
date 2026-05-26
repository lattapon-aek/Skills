# AI Agent Skills

Reusable software-engineering skills for AI agents that must work from evidence, narrow scope, and prove results instead of guessing.

## Catalog

```text
skills/
  task-intake/
  change-implementation/
  root-cause-debugging/
  change-review/
references/
  four-principles.md
tests/
  change-implementation/
  change-review/
  root-cause-debugging/
  skill-flow/
```

## Skills

### `task-intake`

Use when the request is vague, broad, solution-biased, or missing proof of done.

Primary job:
- clarify the real objective
- narrow scope
- identify required evidence
- define proof of done before handoff

Expected output shape:
- `Objective`
- `Desired Outcome`
- `Source Material`
- `External Evidence Needed`
- `Scoped Work`
- `Out of Scope`
- `Constraints`
- `Assumptions`
- `Ruled-out Interpretations`
- `Impact and Tradeoffs`
- `Proof of Done`
- `Open Questions and Resolution Path`

### `change-implementation`

Use when the objective is clear enough and the agent must change code, config, docs, or tooling.

Primary job:
- inspect real source first
- trace the exact patch point
- implement the smallest justified change
- prove the result with observed behavior

Expected output shape:
- `Objective`
- `Evidence`
- `External Evidence`
- `Assumptions`
- `Change Location`
- `Why This Patch Point`
- `Rejected Approaches`
- `Scoped Plan`
- `Out of Scope`
- `Impact and Tradeoffs`
- `Verification`
- `Observed Result`
- `Open Risks`

### `root-cause-debugging`

Use when the issue is a bug, regression, crash, bad data path, or unexplained runtime behavior.

Primary job:
- gather incident evidence first
- reproduce or simulate the issue
- rule out competing hypotheses
- identify the exact fault location before patching

Expected output shape:
- `Failure`
- `Evidence`
- `Incident Evidence`
- `External Evidence`
- `Reproduction Path`
- `Fault Location`
- `Root Cause`
- `Why This Is The Root Cause`
- `Ruled-out Hypotheses`
- `Fix Scope`
- `Impact and Tradeoffs`
- `Verification`
- `Observed Result`
- `Open Risks`

### `change-review`

Use when the agent must review a diff, PR, patch set, or working tree before acceptance.

Primary job:
- inspect the real diff and surrounding code
- separate observed evidence from inference
- report correctness, regression, proof, and blast-radius risks

Expected output shape:
- `Findings`
- `Open Questions`
- `Ruled-out Concerns`
- `Residual Risk`

Inside findings, distinguish `Observed Evidence` from `Inference` when the risk is not directly executed or proven.

## Shared Doctrine

All skills follow the same operating model:

- clarify until the real objective is clear
- use the best available evidence
- narrow scope before acting
- break work into parts
- state impact and tradeoffs
- prove claims and results with evidence

Shared principles live in [references/four-principles.md](C:/Users/lattapon.kea/Desktop/Agents%20Skills/suites/software-engineering/references/four-principles.md):

- `Think Before Coding`
- `Simplicity First`
- `Surgical Changes`
- `Goal-Driven Execution`

Evidence hierarchy:

1. Real behavior: runtime output, logs, traces, metrics, failing commands, observed results
2. Local artifacts: source code, config, tests, docs, tickets, diagrams, workspace data
3. Official external sources: vendor docs, standards, API refs, release notes, source repos
4. Supporting external sources: issue trackers, maintainer comments, reputable community writeups

## Compose The Skills

Typical flow:

1. `task-intake`
2. `root-cause-debugging` or `change-implementation`
3. `change-review`

Recommended routing:

- unclear request -> `task-intake`
- clear change request -> `change-implementation`
- bug or unexplained runtime issue -> `root-cause-debugging`
- diff acceptance or self-review -> `change-review`

## Reporting Conventions

Use these conventions across the repo:

- `Observed Evidence` vs `Inference`
  - `Observed Evidence` is what the agent directly saw in code, diff, tests, logs, traces, runtime output, or authoritative sources.
  - `Inference` is a risk or conclusion derived from that evidence.
- `No patch` is valid when the current workspace does not reproduce the reported issue and no justified change is supported by evidence.
- Separate `Historical Incident State` from `Current Workspace State` when an incident report and the current codebase disagree.
- Use the skill-specific ruled-out field to show what was considered and rejected:
  - `Ruled-out Interpretations`
  - `Rejected Approaches`
  - `Ruled-out Hypotheses`
  - `Ruled-out Concerns`

These conventions are meant to reduce confident-but-undersupported conclusions and make the agent's reasoning easier to audit.

## Stress Tests

The repo includes fixture suites for forward-testing skill behavior:

- [tests/change-implementation/README.md](C:/Users/lattapon.kea/Desktop/Agents%20Skills/suites/software-engineering/tests/change-implementation/README.md)
- [tests/root-cause-debugging/README.md](C:/Users/lattapon.kea/Desktop/Agents%20Skills/suites/software-engineering/tests/root-cause-debugging/README.md)
- [tests/change-review/README.md](C:/Users/lattapon.kea/Desktop/Agents%20Skills/suites/software-engineering/tests/change-review/README.md)
- [tests/skill-flow/README.md](C:/Users/lattapon.kea/Desktop/Agents%20Skills/suites/software-engineering/tests/skill-flow/README.md)

Current coverage themes:

- small surgical change vs over-fix
- local evidence vs external evidence
- incident evidence before simulation
- misleading signals and ruled-out hypotheses
- review findings vs ruled-out concerns
- end-to-end skill composition across multiple phases

## Usage Notes

- These skills are opinionated toward consultative, evidence-first software engineering work.
- They are designed to prefer `no patch` over speculative patching when the current workspace does not reproduce the reported issue.
- They are also designed to make proof gaps explicit instead of hiding them behind confident language.

## Add A New Skill

```powershell
.\scripts\new-skill.ps1 -Name my-skill -DisplayName "My Skill" -ShortDescription "What it does" -DefaultPrompt "Use $my-skill to help with this task."
```

Then edit the generated `SKILL.md`, add any needed references, scripts, or assets, and validate it.

## Validation

```powershell
python "C:\Users\lattapon.kea\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\suites\software-engineering\skills\task-intake
python "C:\Users\lattapon.kea\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\suites\software-engineering\skills\change-implementation
python "C:\Users\lattapon.kea\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\suites\software-engineering\skills\root-cause-debugging
python "C:\Users\lattapon.kea\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\suites\software-engineering\skills\change-review
```
