# Plan Protocol

Use this protocol when the objective and decision domain are clear but the approach, migration, integration, or change boundary is not settled.

## Procedure

1. State the exact decision and current source-backed state.
2. When the decision depends on unestablished controlling behavior, apply `mechanism-design-protocol.md` through the core entrypoint before comparing architectures.
3. Compare only realistic options, normally two to four.
4. Tie each option to constraints, impact, reversibility, and proof cost.
5. Recommend one approach and rule out alternatives with evidence or explicit tradeoffs.
6. Define the change boundary and what must remain untouched.
7. Freeze the intended state and commitments that implementation must preserve.
8. Define functional, mechanism, and conformance oracles before implementation.
9. Record remaining assumptions and the next evidence that would invalidate or confirm them.

## Intent Contract

Record:

- `Intended State` — observable behavior, structure, interfaces, outputs, and boundaries expected after implementation.
- `Plan Commitments` — decisions implementation must follow.
- `Observable Conformance Criteria` — checks that distinguish the approved result from a merely functional alternative.
- `Allowed Variations` — default `none`; list only variations explicitly allowed.
- `Forbidden Substitutions` — working alternatives that would still violate intent.
- `Plan Amendment Authority` — who may approve a material change and whether another user turn is required.

Do not use broad phrases such as “equivalent implementation is acceptable” without naming the exact equivalence boundary.

## Mechanism Contract

Include this section only when the decision depends on behavior not established by current local source:

- `System Model`
- `Mechanism Claims`
- `Mechanism Evidence`
- `Local Observation vs External Behavior`
- `Decision Sensitivity`
- `Falsifying Evidence`
- `Unverified Mechanisms`

Do not promote a user-proposed solution to `Plan Commitments` while a decision-changing mechanism claim is `conditional` or `unproven`.

## Exit Gate

Do not enter `Implement` until:

- the real source path and patch boundary were inspected
- the recommended approach is justified against alternatives
- every `Ask Now` question is answered
- assumptions that affect correctness have a source-check or explicit accepted risk
- intended state and conformance criteria are observable
- material variations and amendment authority are explicit
- the remaining proof gap is acceptable under the recorded authority mode
- every mechanism claim that can change the architecture is established from implementing source, official documentation, or a live probe
- the proof strategy measures the requested runtime outcome rather than only folder, manifest, schema, or build conformance

If new evidence later invalidates a commitment, return here and amend the working document before implementing the alternative. Never rewrite the plan retrospectively.

## Output Contract

- `Working Document`
- `User Contract`
- `Decision`
- `Objective`
- `Current State`
- `Constraints`
- `Assumptions`
- `Options Considered`
- `Ruled-out Options`
- `Recommended Approach`
- `Why This Approach`
- `Impact and Tradeoffs`
- `Execution Boundaries`
- `Intended State`
- `Plan Commitments`
- `Observable Conformance Criteria`
- `Allowed Variations`
- `Forbidden Substitutions`
- `Plan Amendment Authority`
- `Proof Strategy`
- `Mechanism Contract` — when applicable
- `Proof Gap`
- `Open Questions`
- `Phase Transition`
