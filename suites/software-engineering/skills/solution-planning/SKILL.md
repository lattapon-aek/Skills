---
name: solution-planning
description: Turn a clear objective into an evidence-backed solution decision before implementation. Use when an agent must compare solution options, choose an approach, define execution boundaries, and justify tradeoffs without jumping into code changes too early.
---

# Solution Planning

## Intent

Decide the right approach before implementation begins. Use real system context, constraints, and tradeoffs to recommend one path that is specific enough to execute.
Stay in planning mode: inspect the current state, compare realistic options, choose one recommendation, and define execution boundaries. Do not drift into implementation, speculative brainstorming, or generic architecture essays.
Golden rule: make the decision space smaller and clearer. Do not widen it with unnecessary options or abstract patterns that are not justified by the actual system.

## When To Use

Use this skill when:

- the objective is clear enough to act on, but the implementation approach is not settled yet
- multiple design or integration paths are possible and tradeoffs matter
- the task may require migration sequencing, boundary decisions, or rollout planning before code changes
- implementing immediately would be risky because the solution shape is still unclear

## When Not To Use

- Do not use this skill when the request itself is still vague or underspecified; route that through `task-intake`.
- Do not use this skill when the main problem is still proving why a failure happens; route that through `root-cause-analysis`.
- Do not use this skill when the approach is already clear enough to execute safely; route that through `change-implementation`.
- Do not use this skill as a substitute for final diff acceptance; use `change-review`.

## Four Principles

Apply these principles while planning:

### 1. Think Before Coding

- Frame the real decision before comparing solutions.
- Surface ambiguity, assumptions, and tradeoffs explicitly.
- Prefer one recommended path over a long undecided option list.

### 2. Simplicity First

- Prefer the smallest design that satisfies the objective.
- Avoid speculative extensibility or abstract architecture that the current scope does not require.

### 3. Surgical Changes

- Keep the decision aligned to the actual system and immediate problem.
- Avoid turning a local design choice into a broad platform rewrite unless evidence clearly requires it.

### 4. Goal-Driven Execution

- Define how the chosen approach will later be proven by implementation and verification.
- Do not stop at “sounds reasonable”; stop at “specific enough to execute and verify.”

## Clarify Until Clear

- Restate the objective, decision to be made, and success criteria.
- Confirm whether the task is about architecture, integration choice, migration sequencing, API shape, module boundaries, or another concrete planning question.
- Ask follow-up questions when ambiguity affects correctness, migration cost, blast radius, or reversibility.
- If the task is still fundamentally underspecified, stop and route it back through intake.

## Source Of Truth

Use the best available evidence before recommending an approach:

- Inspect the relevant code, module boundaries, data flow, configs, tests, docs, tickets, diagrams, and existing runtime constraints.
- Search external sources when the decision depends on framework capabilities, vendor constraints, standards, API contracts, version behavior, or current external facts not provable from the workspace alone.
- Prefer official docs, standards, release notes, source repos, and maintainer-owned references over summaries.
- Treat conventions, memory, and architecture taste as hints, not evidence.
- Separate observed system facts from planning assumptions.

## Decision Sufficiency

Planning can conclude when all of these are true:

- the decision to be made is explicitly framed
- the current state is understood well enough to compare realistic options
- constraints and success criteria are concrete enough to shape the recommendation
- the option set has been narrowed to plausible paths only
- one recommended approach is specific enough to execute later
- there is a clear proof strategy for the implementation phase

If these are not true, either gather the missing evidence or route the task back through intake.

## Decision Framing

Before comparing options, be able to answer:

- What exact decision must be made now
- What outcome the decision must support
- What constraints cannot be broken
- What current-system facts materially shape the decision
- What would make a solution unacceptable even if it is technically possible

## Options And Tradeoffs

- Compare only the smallest realistic option set, usually 2-4 options.
- For each option, assess complexity, blast radius, migration cost, reversibility, testability, operability, and alignment with the current system.
- Rule out options that are unrealistic, oversized, or unsupported by the evidence.
- Recommend one path explicitly; do not stop at listing pros and cons.

## Execution Boundaries

- Define what later implementation must change.
- Define what must remain untouched in this phase.
- State whether rollout, migration, or phased delivery is required.
- If the chosen approach still leaves critical unknowns, say so explicitly instead of pretending the plan is ready.

## Proof Gap Rule

- State what the current evidence already proves about the design decision.
- State what is still assumed, uncertain, or deferred to implementation.
- State what later implementation or validation will need to prove.

## Output

Report:

- `Decision`
- `Objective`
- `Current State`
- `Constraints`
- `Options Considered`
- `Ruled-out Options`
- `Recommended Approach`
- `Why This Approach`
- `Impact and Tradeoffs`
- `Execution Boundaries`
- `Proof Strategy`
- `Open Questions`

## Phase Handoff

- Hand back to `task-intake` if the objective or decision framing is still too unclear.
- Hand off to `change-implementation` when one recommended approach is specific enough to execute safely.
- Hand off to `change-review` only after an implementation or explicit no-change outcome exists to assess.

## Reference

Use [references/design-template.md](references/design-template.md) for a compact planning artifact.
Use [../../references/four-principles.md](../../references/four-principles.md) for the shared doctrine and rationale.
