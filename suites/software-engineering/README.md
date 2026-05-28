# AI Agent Skills

Reusable software-engineering skills for AI agents that must work from evidence, narrow scope, and prove results instead of guessing.

## Catalog

```text
skills/
  software-engineering-core/
  change-review/
references/
  four-principles.md
  orchestration-policy.md
tests/
  software-engineering-core/
  change-review/
```

## Skills

### `software-engineering-core`

Use for nearly all engineering work. This one skill contains the shared mindset and switches between four modes as evidence demands:

- `Clarify` for vague, broad, or solution-biased requests
- `Plan` for design, migration, integration, or boundary decisions
- `Analyze` for failures, regressions, runtime issues, and system-level incidents
- `Implement` for narrow, justified code, config, docs, or tooling changes

Primary job:
- clarify the real objective
- classify the failure or decision domain
- choose the narrowest justified mode
- gather evidence before conclusions
- prove reasoning and results before handoff to review
- follow the core execution loop: inspect facts, confirm assumptions, act narrowly, observe, and re-check impact

Mode output shapes:
- `Clarify`: `Objective`, `Desired Outcome`, `Failure or Decision Domain`, `Source Material`, `Proof of Done`
- `Plan`: `Decision`, `Current State`, `Options Considered`, `Recommended Approach`, `Proof Strategy`
- `Analyze`: `Failure`, `Failure Domain`, `Incident Evidence`, `Fault Location`, `Root Cause`, `Ruled-out Hypotheses`
- `Implement`: `Change Location`, `Why This Patch Point`, `Rejected Approaches`, `Verification`, `Observed Result`

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
Use the same structure for self-review and justified `no patch` outcomes.

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

Suite-level orchestration policy lives in [references/orchestration-policy.md](C:/Users/lattapon.kea/Desktop/Agents%20Skills/suites/software-engineering/references/orchestration-policy.md).

Typical flow:

1. `software-engineering-core`
2. `change-review`

Recommended routing:

- vague or broad request -> core `Clarify`
- clear objective but unsettled solution or migration path -> core `Plan`
- bug or unexplained runtime issue -> core `Analyze`
- clear patch boundary and execution target -> core `Implement`
- diff acceptance or self-review -> `change-review`
- any accepted final state -> emit a `change-review`-shaped report

## Reporting Conventions

Use these conventions across the repo:

- `Observed Evidence` vs `Inference`
  - `Observed Evidence` is what the agent directly saw in code, diff, tests, logs, traces, runtime output, or authoritative sources.
  - `Inference` is a risk or conclusion derived from that evidence.
- `No patch` is valid when the current workspace does not reproduce the reported issue and no justified change is supported by evidence.
- Separate `Historical Incident State` from `Current Workspace State` when an incident report and the current codebase disagree.
- Use the skill-specific ruled-out field to show what was considered and rejected:
  - `Ruled-out Interpretations`
  - `Ruled-out Options`
  - `Ruled-out Hypotheses`
  - `Rejected Approaches`
  - `Ruled-out Concerns`

These conventions are meant to reduce confident-but-undersupported conclusions and make the agent's reasoning easier to audit.

## Stress Tests

The repo includes fixture suites for forward-testing skill behavior:

- [tests/software-engineering-core/README.md](C:/Users/lattapon.kea/Desktop/Agents%20Skills/suites/software-engineering/tests/software-engineering-core/README.md)
- [tests/change-review/README.md](C:/Users/lattapon.kea/Desktop/Agents%20Skills/suites/software-engineering/tests/change-review/README.md)

Current coverage themes:

- small surgical change vs over-fix
- local evidence vs external evidence
- incident evidence before simulation
- failure-domain thinking across code, tooling, runtime, sandbox, orchestration, and resource pressure
- misleading signals and ruled-out hypotheses
- design-choice recommendation before implementation
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
python "C:\Users\lattapon.kea\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\suites\software-engineering\skills\software-engineering-core
python "C:\Users\lattapon.kea\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\suites\software-engineering\skills\change-review
```
