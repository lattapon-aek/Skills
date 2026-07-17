---
name: change-review
description: Final acceptance gate for a concrete software change, diff, pull request, working tree, implemented result, or justified no-patch conclusion. Use to find correctness risks, regressions, intent or plan divergence, instruction violations, false-green proof, hidden blast radius, and residual risk before accepting the result.
---

# Change Review

## Role

Own acceptance, not clarification, diagnosis, planning, or implementation. Review a concrete artifact and decide whether it is ready, must return to an earlier owner, or remains blocked by proof.

Targets: a diff, PR, working tree, commit, build, deployment, implemented result tied to inspectable proof, or justified `no patch` conclusion.

If the request is an approve, merge, ship, close, or production decision based mainly on a green/red result or report, use `verification-hazards` first. If no concrete target or justified no-patch artifact exists, return to `software-engineering-core`.

## Must Obey

- Inspect the target and surrounding behavior; do not review from summary.
- Confirm objective, intended state, contract, and plan commitments before judgment.
- Separate observed evidence from inference and source external behavior in the current review.
- Prioritize correctness, conformance, regressions, blast radius, and proof over style.
- Do not implement fixes in review mode; hand back to the exact owner and gate.
- Do not accept a working result that materially diverges from the approved plan without explicit authority.
- Do not erase a temporary or corrected material deviation from the audit trail.

## Review Procedure

1. Identify the exact artifact and acceptance target.
2. Read the working document, user contract, intended state, plan commitments, and allowed variations.
3. Inspect the diff and surrounding behavior-determining paths.
4. Trace callers, contracts, data, runtime and operational effects, and rollback.
5. Check whether the result solves the proven objective or failure mechanism.
6. For mechanism-dependent designs, require an observed or authoritative controlling-system model.
7. Compare observed state with intended state and classify every material delta.
8. Inspect tests, commands, logs, and hazard verdicts used as proof.
9. Map each requirement and commitment to implementation and observed evidence.
10. Report blockers first and hand back when an earlier gate is open.

## Review Rubric

- `Functionality` — required behavior works and any demonstrated failure is fixed.
- `Mechanism Validity` — design follows controlling behavior, not unverified theory.
- `Intent Conformance` — observed state matches the approved requirements, plan, architecture boundary, output contract, required sequence, and exclusions.
- `Code Health` — maintainable without unnecessary complexity.
- `Smallest Sufficient Change` — every behavior and touched area has a requirement, fault, compatibility, or proof reason.
- `Blast Radius` — caller, consumer, data, config, runtime, migration, rollout, and rollback effects are understood.
- `Proof Sufficiency` — observed evidence exercises the right layer, surface, cause, artifact, baseline, outcome, and conformance criteria.
- `Instruction Compliance` — authority, sequence, deliverables, forbidden actions, and proof obligations were followed.
- `Oracle Strength` — a plausible incorrect or plan-divergent implementation would fail the available assertion.

Do not infer safety from naming, code shape, or passing tests alone. Reduce confidence or keep a gap open when critical source, runtime, or external contract evidence is unavailable.

## Intent-Conformance Gate

For every recorded commitment compare:

`Expected State -> Observed State -> Delta -> Authority -> Disposition`

Use these dispositions:

- `conforms`
- `authorized deviation` — allowed in advance or explicitly approved by the user or governing document
- `unresolved deviation`

An `unresolved deviation` blocks changes to a requirement, plan decision, architecture boundary, named contract, output shape, sequence, compatibility constraint, or exclusion.

“It works”, “tests pass”, “the alternative is simpler”, “users are not affected”, and “functionally equivalent” do not authorize the deviation. If evidence shows the plan itself is wrong, route to core `Plan` for a prospective amendment; do not approve a retrospective rewrite.

Conformance does not prove mechanism validity. If the plan depends on an unverified controlling-system model, return to core `Plan` rather than accepting faithful execution of a bad theory.

## Proof Review

When a green/red observation supports acceptance, require a `verification-hazards` verdict or run the smallest necessary scan. Check that:

- production does not bypass the tested layer
- the run covers the relevant shipping surface
- the claimed cause was observed
- the verified artifact is the accepted artifact
- red attribution survives baseline comparison
- the oracle rejects plausible wrong behavior
- the oracle rejects a working but nonconforming result

A missing or `still a lead` hazard verdict is a proof finding or residual risk; “tests pass” cannot hide it.

## Findings

Report findings first and order them:

- `critical` — incorrect or unsafe in a likely path
- `high` — blocks correctness, intent conformance, safety, or reliable acceptance
- `medium` — notable risk needing resolution or explicit acceptance
- `low` — minor issue with real behavior impact
- `note` — context or tradeoff without required action

Name the file and tight lines when applicable, impact, observed evidence, inference, and resolution. Ignore style unless it hides behavioral or maintenance risk.

## Output Contract

- `Findings`
- `Instruction Compliance`
- `Acceptance Coverage`
- `Intent Conformance`
- `Mechanism Validity`
- `Deviations`
- `Open Questions`
- `Ruled-out Concerns`
- `Proof Gap`
- `Residual Risk`
- `Verdict` — `accept`, `accept with authorized deviation`, or `return to <owner/mode>`

Use [references/review-template.md](references/review-template.md) for the compact structure. If there are no findings, say so explicitly and still report proof gaps, conformance, and residual risk.

For `no patch`, state whether any justified change remains, which candidate fixes were ruled out, how current state conforms to the intended state, and what historical or external condition remains unproven.

## Handoff

- Return to core `Clarify` when objective or intended state is unclear.
- Return to core `Analyze` when the claimed failure mechanism is unproven.
- Return to core `Plan` when implementation diverges materially or the approved approach needs amendment.
- Return to core `Plan` when the artifact conforms to a plan whose controlling-mechanism claims remain unproven.
- Return to core `Implement` when a concrete execution or oracle gap must be corrected.
- Return to `verification-hazards` when acceptance depends on an unchallenged green/red result or report.

State the exact open gate, evidence or change required, and mode to resume. Do not hand back with a generic request to “fix the issues.”
