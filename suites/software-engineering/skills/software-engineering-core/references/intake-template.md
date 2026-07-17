# Clarify Protocol

Use this protocol when the request is vague, solution-biased, missing source material, or lacks a verifiable outcome.

## Procedure

1. Restate the underlying objective without assuming the proposed solution is correct.
2. Separate the user's objective from any proposed explanation, system model, architecture, or implementation.
3. Record the user contract and working document.
4. Identify the desired outcome, affected boundary, constraints, and proof of done.
5. Perform only the shallow inspection needed to locate likely ownership or source material.
6. Separate direct statements and observations from assumptions.
7. Classify realistic interpretations and failure or decision domains.
8. Ask only questions whose answers can change correctness; route source-checkable questions to inspection instead.

## Exit Gate

Remain in `Clarify` unless all are true:

- The objective is one concrete sentence with a verifiable success condition.
- The failure or decision domain has direct support from the user, source, or runtime.
- `Source Material` names inspectable artifacts rather than placeholders.
- Every material question is answered, assigned to a source investigation, or recorded as an explicit assumption.
- Plausible alternative interpretations are ruled out with a reason.
- The intended state and proof of done are explicit enough to evaluate conformance later.
- Every user-proposed mechanism that can change the architecture is established, routed through the core entrypoint to `mechanism-design-protocol.md`, or kept explicitly unproven.

If two or more domains remain equally plausible without a distinguishing signal, present the open questions and stop. Do not route to Plan, Analyze, or Implement.

## Output Contract

Always include:

- `Working Document`
- `User Contract`
- `Objective`
- `User-Proposed Explanation`
- `User-Proposed Solution`
- `Desired Outcome`
- `Intended State`
- `Failure or Decision Domain`
- `Source Material`
- `Proof of Done`
- `Proof Gap`

Include when applicable:

- `Scoped Work`
- `Out of Scope`
- `Constraints`
- `Assumptions`
- `Ruled-out Interpretations`
- `Impact and Tradeoffs`
- `External Evidence Needed`
- `Mechanism Claims` — when a proposed design depends on harness, framework, runtime, protocol, platform, vendor, or other controlling behavior
- `Decision Dependencies` — which design choices change if a mechanism claim is false
- `Open Questions and Resolution Path`

Classify each open question as `Ask Now`, `Investigate from Source`, `Investigate Externally`, or `Assume Explicitly`.
