# Implement Protocol

Use this protocol only when objective, approach, assumptions, patch boundary, intended state, and amendment authority are confirmed.

## Pre-Edit Gate

Before editing:

1. Re-read the relevant source; do not rely on an earlier phase summary.
2. Revalidate every assumption and plan commitment.
3. Name the exact file, function, block, query, config, or template to change.
4. Explain why this is the narrowest safe patch point and what remains untouched.
5. Trace callers, external consumers, data shapes, runtime side effects, and likely blast radius.
6. Confirm rollback and whether a migration, staged rollout, or deprecation is required.
7. Freeze the original failure reproduction for issue work.
8. Confirm the functional oracle and intent-conformance oracle.

Return to `Plan` when an assumption, boundary, or commitment changed. Return to `Analyze` when the failure mechanism is not proven.

## Editing Rules

- Keep steps small and inside the proven boundary.
- Preserve unrelated code and surrounding style.
- Do not bundle cleanup or speculative hardening with the required change.
- Expand the diff only when new evidence justifies the expansion; update the plan before editing the new area.
- Track every user requirement and plan commitment in acceptance coverage.
- Record a material deviation immediately, including one later corrected.
- Never use working behavior as authority to accept an unplanned substitute.

When observed implementation needs to differ from the plan:

1. stop before completing the alternative
2. record the evidence invalidating the current plan
3. state the proposed delta and impact
4. return to `Plan`
5. amend the working document prospectively
6. obtain authority when the delta is outside pre-approved variation

## Verification

After editing:

1. Run the targeted checks that exercise the changed boundary.
2. For a fix, replay the frozen original reproduction or closest faithful incident simulation.
3. Observe the user-visible outcome oracle and former divergence point.
4. Run at least one negative or adjacent control.
5. Compare observed state against every intended-state criterion.
6. Name one plausible working-but-nonconforming implementation and confirm the oracle rejects it.
7. State the recurrence boundary and anything the environment could not exercise.
8. Route the result through `verification-hazards` before trusting it.

If the issue persists, changes form, or disappears for an unexplained reason, return to `Analyze`; do not stack another speculative patch.

## Conformance Verdict

Use exactly one:

- `conforms`
- `authorized deviation`
- `unresolved deviation`

For every delta record:

- expected state
- observed state
- affected commitment
- functional impact
- conformance impact
- authority source
- required resolution

An `unresolved deviation` blocks completion and acceptance even when functional verification is green.

## Output Contract

- `Working Document`
- `User Contract`
- `Objective`
- `Evidence`
- `Assumptions Revalidated`
- `Change Location`
- `Why This Patch Point`
- `Reversibility Assessment`
- `Caller Contract Impact`
- `Rejected Approaches`
- `Scoped Plan`
- `Out of Scope`
- `Intended State`
- `Observed State`
- `Plan Commitments`
- `Allowed Variations`
- `Conformance Check`
- `Conformance Verdict`
- `Verification`
- `Test Coverage`
- `Original-Reproduction Replay`
- `Recurrence Boundary`
- `Acceptance Coverage`
- `Deviations`
- `Observed Result`
- `Proof Gap`
- `Open Risks`
