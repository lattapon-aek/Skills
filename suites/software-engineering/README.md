# AI Agent Skills

Reusable software-engineering mindset and process skills for AI agents that must work from evidence, narrow scope, and prove results instead of guessing.

## Portable Install

This suite is packaged for the `skills` CLI. From the repository root, install the shipped skills with:

```powershell
npx skills add https://github.com/lattapon-aek/Skills --skill software-engineering-core --skill change-review --skill verification-hazards
```

## Adapters

- Claude Code: `.\scripts\link-software-engineering-skills.ps1`
- Codex: `.\scripts\link-codex-skills.ps1`
- skills CLI: `npx skills add https://github.com/lattapon-aek/Skills`

## Enforce Skill Use With `AGENTS.md`

Installing a skill makes it available, but it does not guarantee every agent will select it. Some agents may skip the skill when they consider a task "small", such as a single-file UI edit or a quick script. Use a repository `AGENTS.md` or global agent instruction to make skill selection mandatory.

Copy this into projects where you want the software-engineering suite enforced:

```md
# Agent Instructions

## Required Software-Engineering Workflow

For any software-engineering task, use `agents-skills:software-engineering-core` before planning, editing, debugging, reviewing, or running verification.

This requirement applies to:

- creating, editing, deleting, renaming, formatting, or generating files
- single-file UI/app/script edits
- empty workspaces and greenfield prototypes
- bug fixes, refactors, migrations, config changes, tests, docs, and tooling
- design or implementation plans that may later become code

Do not skip the skill because the task looks small.

Before the first file edit, satisfy the Document Gate:

- use the user-supplied task document, issue, PR, packet, design brief, or runbook if one exists
- otherwise create a repo-local work packet before editing
- if this repo has no convention, use `.agent/work-packets/<task>.md`
- inline work packets are allowed only for read-only one-turn work that does not touch files
- if the user explicitly refuses artifacts, state the audit and resume risk before continuing

During work:

- update the work packet or progress log when objective, scope, decisions, evidence, patch boundary, verification, proof gaps, or next action change
- after context compaction, interruption, or handoff, read the work packet/progress log/final report before continuing
- verify with real commands or runtime checks before claiming completion

Before accepting completion:

- use `agents-skills:verification-hazards` when trusting a green/red test, CI result, benchmark, rollout result, or agent report
- use `agents-skills:change-review` for every accepted patch or justified no-patch conclusion
```

For stricter global use, place the same policy in the agent's global instructions. Keep repo-local `AGENTS.md` files for project-specific paths, package managers, test commands, and artifact locations.

Recommended prompt when starting a task:

```text
Use agents-skills:software-engineering-core and follow this repo's AGENTS.md. If no working document exists, create the required work packet before editing files.
```

## Catalog

```text
skills/
  software-engineering-core/
  change-review/
  verification-hazards/
references/
  context-continuity.md
  four-principles.md
  orchestration-policy.md
tests/
  software-engineering-core/
  change-review/
  verification-hazards/
  golden-transcripts/
  internet-derived/
  mini-stress/
```

## Skills

### `software-engineering-core`

Use for nearly all engineering work. This one skill changes the agent's default thought path before it changes code: request -> objective -> evidence -> domain -> mode -> action -> proof -> review.

It contains the shared mindset and switches between four modes as evidence demands:

- `Clarify` for vague, broad, or solution-biased requests
- `Plan` for design, migration, integration, or boundary decisions
- `Analyze` for failures, regressions, runtime issues, and system-level incidents
- `Implement` for narrow, justified code, config, docs, or tooling changes

Primary job:
- clarify the real objective
- classify the failure or decision domain
- choose the narrowest justified mode
- gather evidence before conclusions
- avoid patch-first behavior when evidence is still missing
- prove reasoning and results before handoff to review
- follow the core execution loop: inspect facts, confirm assumptions, act narrowly, observe, and re-check impact

Mode output shapes:
- `Clarify`: `Objective`, `Desired Outcome`, `Failure or Decision Domain`, `Source Material`, `Proof of Done`
- `Plan`: `Decision`, `Current State`, `Options Considered`, `Recommended Approach`, `Proof Strategy`
- `Analyze`: `Failure`, `Failure Domain`, `Incident Evidence Pack`, `Fault Location`, `Root Cause`, `Ruled-out Hypotheses`
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

### `verification-hazards`

Use as a lens (not a mode) whenever a green test, CI run, benchmark, or agent report is about to be trusted. It names the five repeatable ways a passing result lies and gives the cheapest counter-check for each:

- `Bypassed-Layer Green` — the test hit a mock/shim/direct-call, not the real trigger, transport, or transition
- `Subset Green` — the run covered a slice (packet subset, local-only, sandbox-limited) that cannot reach the failing case
- `Wrong-Theory Green` — the fix rests on an unobserved root cause; the offline test encodes the same wrong assumption
- `Wrong-Tree Green` — the verified bytes are not the committed/shipping bytes
- `Not-Your-Red` — a pre-existing flake or environment contention misattributed to the change

Before elevating green to `Observed Result`, it requires five gates to pass — `Layer`, `Surface`, `Cause`, `Artifact`, `Baseline` — and otherwise returns a `still a lead` verdict with the cheapest next check. It sharpens core's `Verification`/`Proof Gap` and review's `Proof Sufficiency`; it does not replace them.

Expected output shape:
- `Claim Under Test`
- `Hazard Scan` (per-hazard `clear` / `at risk` / `not applicable` with the deciding tell)
- `Counter-Checks Run`
- `Verification Verdict` (`confirmed` / `still a lead`)
- `Proof Gap`
- `Residual Risk`

## Shared Doctrine

All skills follow the same operating model:

- clarify until the real objective is clear
- use the best available evidence
- narrow scope before acting
- break work into parts
- state impact and tradeoffs
- prove claims and results with evidence

Shared principles live in [references/four-principles.md](references/four-principles.md):

- `Think Before Coding`
- `Simplicity First`
- `Surgical Changes`
- `Goal-Driven Execution`

Context continuity lives in [references/context-continuity.md](references/context-continuity.md). For substantial work, agents must identify a user-supplied working document, create a repo-local work packet, or state an inline work packet before acting. The conversation context window is not enough for multi-step, file-changing, design, review, or resume-prone work.

Evidence hierarchy:

1. Real behavior: runtime output, logs, traces, metrics, failing commands, observed results
2. Local artifacts: source code, config, tests, docs, tickets, diagrams, workspace data
3. Official external sources: vendor docs, standards, API refs, release notes, source repos
4. Supporting external sources: issue trackers, maintainer comments, reputable community writeups

## Compose The Skills

Suite-level orchestration policy lives in [references/orchestration-policy.md](references/orchestration-policy.md).

Operating contract:

- `software-engineering-core` owns the work: clarify, plan, analyze, implement, or justify no patch.
- `verification-hazards` challenges proof: use it only when a green/red run, CI result, benchmark, or agent report is being treated as evidence.
- `change-review` accepts or rejects the result: use it only when there is a concrete diff, working tree, implemented result, PR, or justified no-patch outcome.
- every substantial phase carries a working document so decisions, evidence, proof gaps, and next actions survive context compaction.

If a gate applies, run it or state why it does not apply. Do not jump to review while objective, diagnosis, patch boundary, or proof is still missing.

Typical flow:

1. `software-engineering-core`
2. `verification-hazards` when a green/red result or agent report is about to be trusted
3. `change-review`

Recommended routing:

- vague or broad request -> core `Clarify`
- clear objective but unsettled solution or migration path -> core `Plan`
- bug or unexplained runtime issue -> core `Analyze`
- clear patch boundary and execution target -> core `Implement`
- a green result or agent report about to be trusted -> `verification-hazards`
- diff acceptance or self-review -> `change-review`
- any accepted final state -> emit a `change-review`-shaped report

Handoff packets:

- Core to hazards: working document, claim under test, exact command/report/result, expected proof, artifact checked, known gaps
- Hazards to core: working document, failed hazard, observed tell, cheapest next check, mode to resume
- Hazards to review: working document, verdict, confirmed gates, open hazards, residual risk
- Core to review: working document, objective, diff or no-patch conclusion, evidence, verification, hazard verdict if applicable, proof gaps
- Review to core: working document, blocking finding, mode to resume, exact evidence or patch needed next

## Reporting Conventions

Use these conventions across the repo:

- `Observed Evidence` vs `Inference`
  - `Observed Evidence` is what the agent directly saw in code, diff, tests, logs, traces, runtime output, or authoritative sources.
  - `Inference` is a risk or conclusion derived from that evidence.
- `Working Document` is the user-supplied task source or repo-local work packet that preserves context beyond the current chat. Use an inline work packet only for small one-turn work that does not need file artifacts.
- `No patch` is valid when the current workspace does not reproduce the reported issue and no justified change is supported by evidence.
- A patch is only one possible outcome; a justified `no patch` conclusion still needs review.
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

- [tests/software-engineering-core/README.md](tests/software-engineering-core/README.md)
- [tests/change-review/README.md](tests/change-review/README.md)
- [tests/verification-hazards/cases.md](tests/verification-hazards/cases.md)
- [tests/golden-transcripts/cases.md](tests/golden-transcripts/cases.md)
- [tests/internet-derived/cases.md](tests/internet-derived/cases.md)
- [tests/mini-stress/cases.md](tests/mini-stress/cases.md)

Current coverage themes:

- small surgical change vs over-fix
- local evidence vs external evidence
- incident evidence before simulation
- failure-domain thinking across code, tooling, runtime, sandbox, orchestration, and resource pressure
- misleading signals and ruled-out hypotheses
- design-choice recommendation before implementation
- decision logging and reversibility before implementation
- review findings vs ruled-out concerns
- green-result hazards: bypassed layer, subset, wrong theory, wrong tree, and not-your-red
- golden transcript checks for routing and output-shape regressions
- internet-derived public incident cases for rollout safety, data recovery, distributed systems, destructive scripts, partial deployments, and interface contracts
- mini-model stress cases for premature patching, false-green acceptance, and unsourced external claims
- end-to-end skill composition across multiple phases
- context continuity through work packets, progress logs, final reports, and resume after compaction

## Usage Notes

- These skills are opinionated toward consultative, evidence-first software engineering work.
- They are designed to prefer `no patch` over speculative patching when the current workspace does not reproduce the reported issue.
- They are also designed to make proof gaps explicit instead of hiding them behind confident language.
- They require substantial work to preserve task context in inspectable artifacts instead of relying on chat history alone.

## Add A New Skill

```powershell
.\scripts\new-skill.ps1 -Name my-skill -DisplayName "My Skill" -ShortDescription "What it does" -DefaultPrompt "Use $my-skill to help with this task."
```

Then edit the generated `SKILL.md`, add any needed references, scripts, or assets, and validate it.

## Validation

Run the full suite validation:

```bash
./scripts/validate-suite.sh
```

Or run the individual skill validators:

```powershell
python "C:\Users\lattapon.kea\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\suites\software-engineering\skills\software-engineering-core
python "C:\Users\lattapon.kea\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\suites\software-engineering\skills\change-review
python "C:\Users\lattapon.kea\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\suites\software-engineering\skills\verification-hazards
```

On macOS or Linux with pyenv:

```bash
PYENV_VERSION=3.12.2 pyenv exec python /Users/lattapon/.codex/skills/.system/skill-creator/scripts/quick_validate.py suites/software-engineering/skills/software-engineering-core
PYENV_VERSION=3.12.2 pyenv exec python /Users/lattapon/.codex/skills/.system/skill-creator/scripts/quick_validate.py suites/software-engineering/skills/change-review
PYENV_VERSION=3.12.2 pyenv exec python /Users/lattapon/.codex/skills/.system/skill-creator/scripts/quick_validate.py suites/software-engineering/skills/verification-hazards
```
