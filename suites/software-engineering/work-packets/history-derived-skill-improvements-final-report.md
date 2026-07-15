# Final Report: History-Derived Skill Improvements

## Objective

Improve the software-engineering suite against observed collaboration failures without adding a fourth skill or weakening evidence-first acceptance.

## What Changed

- Added preflight skill selection before engineering tools or edits.
- Added user-contract authority modes and exact instruction traceability.
- Made phase gates evidence boundaries instead of mandatory user round trips.
- Added acceptance coverage and deviation reporting to core and review.
- Added micro, standard, and high-risk continuity tiers.
- Added `Weak-Oracle Green` and the `Outcome` sufficiency gate.
- Added history-derived golden, mini-stress, flow, and hazard scenarios.
- Expanded suite validation to every executable TypeScript test and new contract scans.
- Made validator discovery portable through `SKILL_VALIDATE_PY`, `CODEX_HOME`, or the normal Codex home.

## Files Touched

- Repository enforcement: `AGENTS.md`
- Validation: `scripts/validate-suite.sh`
- Suite docs and shared references under `suites/software-engineering/`
- All three skill entrypoints, relevant references, and agent metadata
- Golden, mini-stress, flow, assessment, and verification-hazard cases
- Work packet, progress log, and this final report

## Decisions

- Preserve core -> hazards -> review ownership.
- Put instruction compliance inside core and review rather than creating another skill.
- Permit inline micro contracts only for low-risk, one-response, reversible work.
- Require all six exact hazard labels to avoid gate-name/hazard-name confusion.

## Verification

- `./scripts/validate-suite.sh` passed on the final doctrine/test tree.
- Three skill validators reported `Skill is valid!`.
- All 14 executable Node tests passed.
- `CODEX_HOME=/Users/lattapon/.codex env -u HOME ./scripts/validate-suite.sh` passed.
- `git diff --check` passed.
- Blind weak-oracle forward test 1 found the intended risk but exposed a label-shape gap.
- A fresh blind rerun after tightening used all six exact labels, returned `still a lead`, and required exact-cardinality proof.

## Observed Evidence

- Static validation finds the selection, authority, acceptance, deviation, and weak-oracle contracts in their owning files.
- The executable fixture surface increased from two representative files in the suite script to all seven test files, producing 14 passing tests.
- The clean blind rerun distinguished `>= 1` from `== 1` and refused acceptance from the weak assertion.

## Acceptance Coverage

| Requirement | Source | Status | Evidence |
| --- | --- | --- | --- |
| Enforce deliberate skill selection | approved analysis | satisfied | orchestration policy, AGENTS.md, suite README, regression cases |
| Preserve speed after authority is clear | approved analysis | satisfied | authority modes and same-turn phase transition rule |
| Trace exact packet/user instructions | approved analysis | satisfied | user contract, acceptance matrix, exact-sequence regression |
| Preserve corrected deviations | approved analysis | satisfied | core/review outputs and templates |
| Catch weak assertions and zero-value passes | approved analysis | satisfied | hazard 6, Outcome gate, catalog, scenarios, blind rerun |
| Avoid excessive small-task ceremony | approved analysis | satisfied | continuity tiers and micro-task golden case |
| Strengthen validation truth | approved analysis | satisfied with residual risk | all executable tests and contract scans run; provider-backed transcript harness remains absent |

## Deviations

- A provider-backed automated transcript service was not added because the repository has no provider-neutral agent execution harness; structured cases and independent forward testing were used instead.
- The first blind forward test substituted `Baseline` for `Not-Your-Red`; the skill was tightened and a fresh blind rerun passed.

## Remaining Risks

- Most doctrine scenarios are still assessment artifacts rather than automated model evaluations.
- Only the weak-oracle path received a fresh independent forward test in this run.
- The working tree is not committed; the acceptance target for this report is the current working tree, not `HEAD`.

## Resume Or Follow-up Notes

If a provider-backed eval harness is added later, start with the history-derived golden cases and assert selected skill, first heading, exact hazard labels, authority mode, acceptance coverage, and forbidden actions. Commit or push this change set only on explicit user request.
