---
name: software-engineering-core
description: Drive software-engineering work with one evidence-first workflow that can clarify objectives, choose an approach, investigate failures, implement the smallest justified change, and prove the result before handoff to review.
---

# Software Engineering Core

## Intent

Use one disciplined workflow for software-engineering work instead of switching mental models per task. Start by clarifying the objective, classify the failure or decision domain, gather the best available evidence, choose the next justified mode, and prove each conclusion before moving on.
Stay in core mode: move between clarification, planning, diagnosis, and implementation only when the current evidence justifies that transition. Do not silently jump from a vague request to a patch, from a report to a root cause, or from a design idea to a rewrite.
Golden rule: one skill, multiple modes. Pick the narrowest mode that fits the current evidence, and keep the work scoped to that mode until the proof gap changes.

## When To Use

Use this skill for most software-engineering work, including:

- vague or broad requests that still need shaping
- implementation work where the patch point must be traced first
- design or migration choices that need a recommendation before coding
- bugs, regressions, runtime issues, and environment failures that need diagnosis
- multi-step tasks that may move from clarification to planning, diagnosis, or implementation

## When Not To Use

- Do not use this skill as a substitute for final acceptance review; use `change-review`.
- Do not use this skill for non-engineering work that does not depend on code, systems, runtime behavior, or technical evidence.

## Four Principles

Apply the repo's shared doctrine throughout all modes:

- `Think Before Coding`
- `Simplicity First`
- `Surgical Changes`
- `Goal-Driven Execution`

## Core Workflow

Always walk these questions in order:

1. What is the real objective?
2. What failure domain or decision domain am I actually in?
3. What evidence do I already have?
4. What is the narrowest justified next mode?
5. What is already proven, and what is still a proof gap?

The main modes inside this skill are:

- `Clarify` for intake and scope shaping
- `Plan` for solution, migration, or boundary decisions
- `Analyze` for bugs, regressions, runtime issues, and unexplained behavior
- `Implement` for narrow, evidence-backed changes

## Execution Loop

Use this loop for every mode, but keep it light when the task is small:

1. Read the request and restate the real objective.
2. Collect the facts that can actually be inspected.
3. Decide whether you need `Clarify`, `Plan`, `Analyze`, or `Implement`.
4. Confirm the current assumption set against source material or runtime evidence.
5. Narrow the next action to the smallest justified step.
6. Run that step and observe the result.
7. Check impact, adjacent behavior, and proof gaps before moving on.

If the loop is still missing a fact that changes correctness, stop and confirm instead of guessing.

## Confirm Gates

Pause and confirm with facts before crossing these gates:

- from user wording to objective
- from objective to plan
- from suspicion to root cause
- from root cause or plan to patch point
- from code change to done

Confirmation can come from local source, runtime output, tests, logs, external docs, or direct user approval. Do not use memory alone when inspectable evidence exists.

## Clarify The Objective

Use `Clarify` mode when the request is vague, broad, or solution-biased.

- Restate the request in one sentence.
- Extract the real objective, desired outcome, stakeholders, constraints, and proof of done.
- Do not accept a proposed solution as the goal until the underlying problem, decision need, or missed outcome is clear.
- If phase routing depends on likely ownership or seam location, do only a shallow source scan.
- Stop clarifying when the task is narrow enough to choose the next mode responsibly.

### Clarify Output

- `Objective`
- `Desired Outcome`
- `Failure or Decision Domain`
- `Source Material`
- `External Evidence Needed`
- `Scoped Work`
- `Out of Scope`
- `Constraints`
- `Assumptions`
- `Ruled-out Interpretations`
- `Impact and Tradeoffs`
- `Proof of Done`
- `Open Questions and Resolution Path`

## Classify The Domain

Before planning, diagnosis, or implementation, classify the dominant domain with evidence:

- application logic or data handling
- dependency, package, or tooling behavior
- runtime environment or host state
- sandbox, permissions, or network restrictions
- orchestration, process lifecycle, retry behavior, or worker coordination
- system resource pressure such as CPU, memory, disk, or file handles
- external vendor or platform behavior
- design, migration, integration, or boundary choice

Do not assume the issue lives in application code if the failure may happen before the application even runs.

## Choose The Next Mode

### Plan

Use `Plan` mode when the objective is clear but the approach is not settled yet.

- Frame the actual decision to be made.
- Compare only realistic options, usually 2-4.
- Recommend one path explicitly.
- Define execution boundaries, tradeoffs, and proof strategy.
- Do not turn planning into generic architecture essays or speculative redesign.

#### Decision Log

When comparing options, record the decision in a way that can be audited later:

- the recommendation
- the main alternative(s) that were ruled out
- the evidence or constraint that ruled them out
- the expected impact if the recommendation is wrong
- the next proof needed before implementation

#### Plan Output

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

### Analyze

Use `Analyze` mode when the main obstacle is still understanding a failure.

- Gather incident evidence from the failure point first.
- Reproduce or simulate the failure whenever feasible.
- Separate second-hand reports from observed evidence.
- Trace to the exact fault location or runtime step where the failure is introduced.
- Rule out competing hypotheses before naming a root cause.
- If fixing is in scope, do not patch until the root cause is proven.

#### Incident Evidence Pack

Before a root cause is finalized, collect the smallest useful pack of evidence from the failure point:

- logs, traces, and error output
- process tree or worker state when orchestration is involved
- sandbox, permission, or network signals when commands fail early
- metrics, resource pressure, or retry counts when the system is degraded
- the exact repro or simulation input used to observe the failure

#### Analyze Output

- `Failure`
- `Failure Domain`
- `Evidence`
- `Incident Evidence`
- `Process / Orchestration Evidence`
- `Runtime Constraints`
- `External Evidence`
- `Reproduction Path`
- `Fault Location`
- `Root Cause`
- `Why This Is The Root Cause`
- `Ruled-out Hypotheses`
- `Fix Scope`
- `Impact and Tradeoffs`
- `Verification`
- `Observed Result`
- `Open Risks`

### Implement

Use `Implement` mode when the objective and patch boundary are clear enough to execute safely.

- Inspect the real code path before editing.
- Name the exact patch point and why it is the narrowest safe place to change.
- Prefer the smallest justified patch.
- Do not drift into redesign, cleanup passes, or indefinite research.
- Do not call the work complete until the target behavior is observed to work or the original failure is observed to disappear.

#### Reversibility Gate

Before editing, confirm whether the change can be rolled back cleanly:

- can the patch be reverted without extra migration work
- does the change preserve the caller contract or require a staged rollout
- will the tests catch the intended rollback risk
- is a narrower patch available if reversibility is weak

#### Implement Output

- `Objective`
- `Evidence`
- `External Evidence`
- `Assumptions`
- `Change Location`
- `Why This Patch Point`
- `Rejected Approaches`
- `Scoped Plan`
- `Out of Scope`
- `Impact and Tradeoffs`
- `Verification`
- `Observed Result`
- `Open Risks`

## Evidence Rules

- Use the best available evidence, in this order:
  1. runtime output, logs, traces, metrics, failing commands, observed results
  2. local artifacts such as code, config, tests, docs, tickets, diagrams, and workspace data
  3. official external docs, standards, release notes, source repos, and vendor references
  4. secondary external commentary only as support
- Treat memory, conventions, and pattern matching as hints, not proof.
- Keep `Observed Evidence` separate from `Inference`.
- State what is proven, what is still uncertain, and what next evidence would close the gap.
- Do not answer from memory when the workspace, logs, docs, or runtime can be checked directly.
- If a claim can be inspected or tested, inspect or test it before elevating it to a conclusion.

## Escalation And Boundaries

- If the objective is still unclear, stay in `Clarify`.
- If the task needs a design or migration choice, move to `Plan`.
- If the task is blocked on understanding a failure, move to `Analyze`.
- If the approach and patch boundary are clear, move to `Implement`.
- If implementation reveals an unproven failure mechanism, go back to `Analyze`.
- If current evidence does not justify any change, `no patch` is valid.

## Proof Gap Rule

For any mode, always state:

- what the current evidence already proves
- what is still unproven, assumed, or blocked
- what next evidence, check, or mode transition would close the gap

## Phase Handoff

- Stay inside `software-engineering-core` until the work reaches either:
  - a concrete implementation result, or
  - a justified `no patch` conclusion
- Hand off to `change-review` for every accepted end state, including self-review and `no patch`.

## Reference

Use these references as needed:

- [references/intake-template.md](references/intake-template.md)
- [references/planning-template.md](references/planning-template.md)
- [references/analysis-playbook.md](references/analysis-playbook.md)
- [references/implementation-checklist.md](references/implementation-checklist.md)
- [../../references/four-principles.md](../../references/four-principles.md)
