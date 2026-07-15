# Review Template

Use this template for final review after a patch and after a justified `no patch` conclusion.

## Findings

- `[severity] [file]: issue and impact`
- `Observed Evidence:` what in the diff, surrounding code, test output, log, or source directly supports the finding
- `Inference:` what risk is inferred beyond directly observed evidence, if any

## Instruction Compliance

- Authority mode, required sequence, deliverables, forbidden actions, commit/report instructions, and proof obligations checked

## Acceptance Coverage

| Commitment | Type | Source | Expected State | Observed State | Status | Evidence |
| --- | --- | --- | --- | --- | --- | --- |

## Intent Conformance

- `Intended State`
- `Observed State`
- `Material Deltas`
- `Conformance Verdict` — `conforms`, `authorized deviation`, or `unresolved deviation`
- `Authority Source` for every authorized deviation

## Deviations

- Record expected state, observed state, affected commitment, authority, and required resolution for every material departure, including corrected departures
- Write `none observed` only after comparing the artifact with the user contract, working document, intended state, and work history

## Open Questions

- Missing context that could change the review outcome

## Ruled-out Concerns

- Risks considered but not promoted to findings, and why

## Residual Risk

- Tests not run
- Areas not inspected
- Behavior that still depends on assumptions

## Proof Gap

- What the inspected artifact and observed proof establish
- What remains unverified or nonconforming
- The next evidence or owner needed to close the gap

## Verdict

- `accept`, `accept with authorized deviation`, or `return to <owner/mode>`
