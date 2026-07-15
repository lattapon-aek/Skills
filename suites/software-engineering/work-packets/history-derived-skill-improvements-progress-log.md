# Progress Log: History-Derived Skill Improvements

## Timeline

- Selected `skill-creator`, `software-engineering-core`, `verification-hazards`, and `change-review` before edits.
- Created the work packet before doctrine changes.
- Updated shared orchestration and context-continuity contracts.
- Updated all three shipped skills, references, metadata, docs, tests, and validation.

## Evidence Inspected

- Current skill entrypoints and linked references.
- Existing golden, mini-stress, flow, verification-hazard, and executable fixtures.
- History-derived failures approved in the preceding analysis.

## Decisions Made

- Keep the three-skill ownership split.
- Add user-contract traceability inside core and review rather than creating a fourth skill.
- Add Weak-Oracle Green as hazard 6.
- Permit micro inline contracts and same-turn phase transitions only under explicit low-risk/authority conditions.

## Changes Made

- Added skill-selection preflight and authority modes.
- Added acceptance coverage and deviation reporting.
- Added continuity risk tiers.
- Added the outcome/oracle proof gate.
- Added history-derived regression scenarios.
- Expanded suite validation to all executable fixtures and new contract scans.

## Verification Runs

- `./scripts/validate-suite.sh`: passed; three skills valid and all 14 executable tests passed.
- `CODEX_HOME=/Users/lattapon/.codex env -u HOME ./scripts/validate-suite.sh`: passed, confirming validator discovery does not require `HOME` when `CODEX_HOME` is set.
- Blind forward test 1: behavioral pass on weak-oracle detection and `still a lead`; output-shape partial because it substituted `Baseline` for the `Not-Your-Red` hazard label.
- Blind forward test 2 after tightening: passed; it used all six exact hazard labels, marked `Weak-Oracle Green` at risk, returned `still a lead`, and required exact cardinality.
- Final `./scripts/validate-suite.sh`: passed on the amended tree; three skill validators and all 14 executable tests passed.
- `git diff --check`: passed with no whitespace errors.

## Proof Gaps

- No provider-backed transcript runner exercises every history-derived scenario automatically. Current behavior proof consists of structured cases plus two independent targeted forward tests.

## Deviations

- Provider-backed automated transcript evaluation remains out of scope for this patch; no provider-neutral harness exists in the repository.

## Next Action

Hand off the final report and residual transcript-harness gap. Commit or push only if the user requests it.
