---
name: software-engineering-core
description: Primary evidence gate for software engineering and agent-skill architecture. Use before coding or specialized creation skills for bugs, features, refactors, migrations, runtime issues, technical plans, skill creation or updates, skill splits, AGENTS.md doctrine moves, and context optimization. Establish objective, controlling mechanism, boundary, and proof; route proof claims through verification-hazards and concrete end states through change-review.
---

# Software Engineering Core

## Role

Own work from request to implementation or justified `no patch`. Use one mode: `Clarify` for the contract, `Plan` for the approach, `Analyze` for cause, or `Implement` for a proven boundary.

Follow `request -> evidence -> earliest unmet gate -> action -> observed proof -> conformance -> verification-hazards -> change-review`. Task size changes artifact needs, not rigor.

## Preflight

Before the first engineering tool call or edit: inspect available skills, name the primary skill and reason, and identify the working document and authority mode. Before choosing a mode, parse causal wording such as `do X because Y`; when Y is an unestablished controlling mechanism, choose `Clarify` or `Plan` and read the mechanism protocol first. `Implement` is unavailable regardless of explicit solution wording. Do not skip preflight for small, single-file, visual, experimental, or empty-workspace tasks.

## Must Obey

- Treat user reports, issue titles, prior agent reports, memory, and plausible explanations as leads, not proof.
- Before a mechanism-dependent target write, publish the complete claim ledger with inspected source or probe evidence and `Mechanism Verdict: established`; user wording is not evidence.
- Do not patch before the objective, domain, and change boundary are supported by inspected evidence.
- A successful patch does not retrospectively prove its root-cause theory.
- Never weaken a test or expand the boundary for cleanup, preference, or proximity.
- Do not treat “works” as equivalent to “matches the approved intent and plan.”
- Do not authorize your own material deviation or rewrite the plan after the fact to match the implementation.
- Do not accept a patch or `no patch` without observed verification, intent conformance, proof gaps, and `change-review`.

## User Contract

Before substantial action, record `Authority Mode`, `Required Sequence`, `Required Deliverables`, `Required Verification`, and `Forbidden Actions`. Authority is `plan-only`, `execute-within-scope`, `ask-before-edit`, or `exact-sequence`.

Track every explicit instruction and approved plan commitment to observed evidence or an open gap. A phase boundary is not an automatic user round trip when `execute-within-scope` permits the next proven step.

## Operating Gates

### Evidence Before Action

Before choosing a mode, root cause, patch point, or verdict, state the claim and inspect the strongest available evidence. Separate observations from inference. If no evidence justifies the next action, investigate, ask, or stop with the missing fact.

### Mechanism Before Design

When an architecture, migration, configuration, or optimization decision depends on harness, framework, runtime, protocol, platform, vendor, model, tool, or infrastructure behavior not established by the workspace, do not turn the proposed solution into a plan commitment yet. Separate the user's objective from their explanation and solution, identify the decision-changing mechanism claims, and establish the controlling behavior from implementing source, official documentation, or a live probe. Keep the plan conditional when an unverified claim could change the architecture.

The gate is fail-closed across the complete claim chain: a missing claim or evidence for only one system link leaves the mechanism unproven.

### Smallest Sufficient Change

Implement only behavior required by the user contract, proven fault, compatibility need, approved plan, or proof strategy. A smaller change wins unless evidence shows it cannot satisfy the contract.

### Proven Change Boundary

Before the first edit and whenever the diff expands, map every touched area to the objective, fault, caller impact, or required proof. Each touched file needs a reason, expected impact, and rollback path.

### Requirement-to-Proof Closure

Before completion, map every user requirement and plan commitment to implementation or justified no-change plus observed proof. Missing or unsupported rows remain explicit proof gaps.

### Intent-to-Outcome Conformance

Functional success and conformance are separate gates. Before implementation, freeze:

- `Intended State`
- `Plan Commitments`
- `Observable Conformance Criteria`
- `Allowed Variations` — default `none`
- `Forbidden Substitutions`
- `Plan Amendment Authority`

After implementation, compare `Observed State` with `Intended State` and record every material delta. A delta is material when it changes a recorded requirement, plan decision, architecture boundary, output contract, required sequence, compatibility constraint, or explicit exclusion.

Only these verdicts may proceed:

- `conforms`
- `authorized deviation` — the variation was allowed in advance or explicitly approved by the user or governing document

`unresolved deviation` blocks completion even when tests pass or the system remains usable. Restore conformance within the proven boundary, or return to `Plan`, amend the working document prospectively, and obtain any required authority before continuing.

## Evidence Order

Prefer observed runtime evidence, then current workspace source and artifacts, then official external contracts, with secondary sources only as support. Surface conflicts and resolve them from the most authoritative applicable source.

## Select The Mode And Reference

Read the selected reference completely before performing that mode. Read only references whose trigger applies.

Check the mechanism row before honoring Plan or Implement wording. When it applies, read that protocol first; `Implement` is unavailable until its gate opens.

| Current need | Mode | Required reference |
| --- | --- | --- |
| A design decision depends on external or uninspected controlling behavior | `Clarify` or `Plan` | [references/mechanism-design-protocol.md](references/mechanism-design-protocol.md) |
| Objective, scope, domain, source material, or proof of done is unclear | `Clarify` | [references/intake-template.md](references/intake-template.md) |
| Objective is clear but approach, migration, or boundary is unsettled | `Plan` | [references/planning-template.md](references/planning-template.md) |
| A bug, incident, regression, hang, performance issue, flaky result, or environment failure is not causally proven | `Analyze` | [references/causal-debugging-protocol.md](references/causal-debugging-protocol.md) |
| Objective, approach, assumptions, and change boundary are confirmed | `Implement` | [references/implementation-checklist.md](references/implementation-checklist.md) |

For work that may span turns, change files, depend on decisions, or survive compaction, apply [references/context-continuity.md](references/context-continuity.md). Use its artifact rules only for continuity; never use them to reduce execution rigor.

Use these templates only when their artifact is required:

- [references/work-packet-template.md](references/work-packet-template.md)
- [references/progress-log-template.md](references/progress-log-template.md)
- [references/final-report-template.md](references/final-report-template.md)

## Cross-Mode Gates

Do not cross:

- request to objective, or objective to plan, without verifiable success and source-backed domain
- proposed system model to architecture without mechanism evidence
- suspicion to cause, or cause/plan to patch, without discriminating evidence and a proven boundary
- plan to implementation with a material question open, or implementation to done without proof and conformance

When an inspectable fact can change correctness, inspect it. When it cannot be established safely, keep the gate closed and name the cheapest next check.

## Execution Loop

1. Identify the contract, working document, objective, and mode.
2. Inspect gate-deciding facts and revalidate assumptions.
3. State the expected observation and which outcome advances, blocks, or routes back.
4. Take the smallest justified action and observe rather than predict.
5. Compare intended and observed state; update coverage, deviations, and artifacts.
6. Challenge green/red proof; recheck impact, adjacent behavior, gaps, and next owner.

If implementation reveals an unproven mechanism, return to `Analyze`. If evidence invalidates the approved approach or the observed result diverges materially, return to `Plan`. Do not stack another speculative patch on top.

## Suite Routing

Start at the earliest unmet gate; do not jump to review while objective, diagnosis, plan, implementation, conformance, or proof remains open. For approve, merge, ship, accept, close, or go/no-go questions that rest mainly on a green/red result or report, use `verification-hazards` first. A phase gate is an evidence boundary, not an automatic user round trip: continue when authority permits and the gate is proven.

Do not re-enter a gate that was already answered unless new evidence changed the answer. When a handoff would repeat a prior verdict without new evidence, stop and surface the missing fact instead of looping.

## Reporting

Rigor is constant; report verbosity adapts. Use a compact report — `Current Gate`, `Action`, `Observed Evidence`, `Decision`, `Next Gate` — when evidence is clear, the scope was fully inspected, and no finding, deviation, or proof gap remains. Expand the report when hypotheses compete, scope or plan changes, a deviation or proof gap exists, risk is high, or the work will be resumed or handed off.

## Verification And Acceptance

Use `verification-hazards` before trusting tests, probes, CI, benchmarks, rollout signals, suspicious reds, or reports; prove behavior and conformance. Use `change-review` before accepting a patch, result, or justified `no patch`. Pass the contract, intended and observed state, artifact/diff, coverage, deviations, command output, hazard verdict, gaps, and residual risk.

## Stop Conditions

Stop and name the gate when the objective is ambiguous; competing domains or causes lack a distinguishing signal; required source, authority, or user decision is missing; scope exceeds plan; a material deviation lacks authority; a fix weakens a test; two directed searches find no deciding evidence; or the result persists, changes, or disappears unexplained.

`No patch` is valid only when current evidence does not justify a change. It must still state what was inspected, what was ruled out, what remains unproven, the intent-conformance status, and the final review verdict.
