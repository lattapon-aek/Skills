# Operating Gates

Use these as observable decision gates, not values to praise in prose. Task size never authorizes skipping an applicable gate.

## Evidence Hierarchy

Prefer:

1. Runtime behavior, logs, traces, metrics, failing commands, and observed results.
2. Current source, config, tests, docs, tickets, diagrams, and workspace artifacts.
3. Official documentation, standards, release notes, APIs, and source repositories.
4. Secondary sources only as support.

Memory, conventions, summaries, issue theories, and prior agent reports are leads. A working document records the contract but does not replace fresh inspection of current source or runtime state.

## 1. Evidence Before Action

- `Trigger` — before choosing a mode, root cause, patch point, or acceptance verdict.
- `Required Action` — state the claim, inspect the strongest evidence, and separate observation from inference.
- `Proceed Gate` — name the observed fact that justifies the next action.
- `Violation Signal` — acting from a plausible explanation when inspectable evidence exists.

## 2. Smallest Sufficient Change

- `Trigger` — when choosing an approach or implementation.
- `Required Action` — map every added behavior to a requirement, proven fault, compatibility need, approved plan, or proof strategy.
- `Proceed Gate` — explain why a smaller change cannot satisfy the contract.
- `Violation Signal` — speculative abstractions, options, fallbacks, cleanup, or hardening without a contract reason.

## 3. Proven Change Boundary

- `Trigger` — before the first edit and whenever the diff expands to another file, module, contract, or runtime path.
- `Required Action` — map every touched area to the objective, proven fault, caller impact, or required verification; preserve unrelated code.
- `Proceed Gate` — each touched area has a concrete reason, expected impact, and rollback path recorded before editing it.
- `Violation Signal` — scope growth justified by proximity, preference, or convenience.

## 4. Requirement-to-Proof Closure

- `Trigger` — before claiming a patch, no-patch result, migration, review, or task complete.
- `Required Action` — map each user requirement and approved plan commitment to implementation or justified no-change plus observed proof.
- `Proceed Gate` — no row is silently missing; satisfied rows have evidence and unsatisfied rows are explicit gaps or blockers.
- `Violation Signal` — closing from “tests pass,” code shape, summary, or confidence without requirement-level proof.

## Intent-to-Outcome Conformance Gate

This hard gate is cross-cutting and does not replace the four gates above.

- `Trigger` — before implementation, after each material result, whenever actual state differs from expected state, and before acceptance.
- `Required Action` — freeze intended state, plan commitments, observable conformance criteria, allowed variations, forbidden substitutions, and amendment authority; then compare observed state against them.
- `Proceed Gate` — every material delta is corrected or explicitly authorized. Allowed variations default to `none`.
- `Stop Condition` — an unresolved deviation changes a requirement, plan decision, architecture boundary, output contract, required sequence, compatibility constraint, or explicit exclusion.
- `Violation Signal` — accepting a different result because it works, tests pass, looks equivalent, seems simpler, or appears harmless.

Functional success does not close this gate. An agent cannot authorize its own material deviation or rewrite the plan retrospectively. When evidence invalidates the plan, return to planning, amend the working document prospectively, and obtain the authority the delta requires.

## Mechanism-Before-Design Gate

Use this conditional gate when a design decision depends on controlling behavior outside or not established by current local source.

- `Trigger` — a proposed architecture, migration, configuration, or optimization depends on how a harness, framework, runtime, protocol, platform, vendor, model, tool, or infrastructure component behaves.
- `Required Action` — separate objective from proposed explanation and solution; identify decision-changing mechanism claims; inspect implementing source, official contracts, or live behavior.
- `Proceed Gate` — every mechanism claim that can change the architecture is established and the proof strategy measures the user objective rather than only structural conformance.
- `Violation Signal` — editing because the user or agent supplied a plausible system model, or treating a green manifest/build/schema check as runtime proof.

Do not apply this gate to pure preference or behavior fully controlled and directly inspectable in current local source.

## Evidence Gathering Rule

Start locally when the answer belongs to the workspace or runtime. Search externally when local evidence is missing, contradictory, or depends on vendor, library, platform, policy, or ecosystem behavior. Surface conflicts and resolve them from the most authoritative applicable source.
