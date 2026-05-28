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

Confirmation must come from at least one of:
- inspectable source: code, config, tests, or docs read directly from the workspace
- runtime evidence: output, logs, traces, metrics, or a command that was run and observed
- official external documentation with a cited source
- direct user statement when no inspectable source is available

Do not use memory alone when inspectable evidence exists. If the gate cannot be confirmed, state the missing evidence explicitly instead of proceeding.

**Gate: from user wording to objective** — this gate is CLOSED when any of the following is true:
- The failure domain has two or more equally-probable candidates with no distinguishing signal from the user's report
- Source Material is empty or contains only placeholders such as "not yet collected"
- Any question classified `Ask Now` has not been answered by the user
- The objective cannot be stated in one concrete sentence with a verifiable success condition

When this gate is closed, present the Clarify output and stop. Do not move to Plan, Analyze, or Implement in the same response.

## Clarify The Objective

Use `Clarify` mode when the request is vague, broad, or solution-biased.

- Restate the request in one sentence.
- Extract the real objective, desired outcome, stakeholders, constraints, and proof of done.
- Do not accept a proposed solution as the goal until the underlying problem, decision need, or missed outcome is clear.
- If phase routing depends on likely ownership or seam location, do only a shallow source scan.
- For incident reports where the failure domain is not immediately clear from the user's words alone, `Open Questions and Resolution Path` and `Ruled-out Interpretations` are required, not optional.

**Clarify Exit Conditions** — all of the following must be true before leaving this mode:

1. The Failure or Decision Domain is supported by at least one direct user statement, runtime signal, or shallow source scan — not inferred from pattern matching alone.
2. Source Material names specific artifacts (files, logs, systems, commands to run) — not a placeholder like "not yet collected".
3. Every question marked `Ask Now` has been answered by the user, or re-classified as `Assume Explicitly` with the assumption stated.
4. Ruled-out Interpretations lists at least one alternative reading of the request that was considered and rejected.
5. The objective can be stated in one concrete sentence with a verifiable success condition.

If any exit condition is not yet met, present the Clarify output and stop. Do not transition to another mode in the same response.

### Clarify Output

Required fields (always include):

- `Objective`
- `Desired Outcome`
- `Failure or Decision Domain`
- `Source Material`
- `Proof of Done`

Conditional fields (include when applicable):

- `External Evidence Needed` — when external sources must be checked before proceeding
- `Scoped Work` — when scope boundaries need to be made explicit
- `Out of Scope` — when explicit exclusions affect routing
- `Constraints` — when constraints exist that limit the solution space
- `Assumptions` — when assumptions are material to correctness
- `Ruled-out Interpretations` — when alternative readings of the request were considered
- `Impact and Tradeoffs` — when multiple valid paths exist with different consequences
- `Open Questions and Resolution Path` — when unresolved questions materially affect execution; mark each as `Ask Now`, `Investigate from Source`, `Investigate Externally`, or `Assume Explicitly`

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
- `Assumptions`
- `Options Considered`
- `Ruled-out Options`
- `Recommended Approach`
- `Why This Approach`
- `Impact and Tradeoffs`
- `Execution Boundaries`
- `Proof Strategy`
- `Proof Gap` — what this plan already has evidence for, what is still unverified or assumed, and what next check would close the gap
- `Open Questions` — mark each as `Ask Now`, `Investigate from Source`, `Investigate Externally`, or `Assume Explicitly`

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
- `Incident Evidence Pack` — logs, traces, error output, process/orchestration state, runtime constraints, sandbox or permission signals, metrics, repro or simulation input used; group by evidence type when multiple are present
- `External Evidence` — official docs, vendor sources, or community references that materially affect the diagnosis
- `Reproduction Path`
- `Fault Location`
- `Root Cause`
- `Why This Is The Root Cause`
- `Ruled-out Hypotheses`
- `Fix Scope`
- `Impact and Tradeoffs`
- `Verification`
- `Observed Result`
- `Proof Gap` — what is already demonstrated by evidence, what is still unproven or assumed, what direct evidence would close the gap
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
- `Reversibility Assessment` — whether the patch can be reverted cleanly, whether caller contracts are preserved, whether tests catch rollback risk, and whether a narrower patch is available if reversibility is weak
- `Rejected Approaches`
- `Scoped Plan`
- `Out of Scope`
- `Impact and Tradeoffs`
- `Verification`
- `Observed Result`
- `Proof Gap` — what is already proven by verification, what is still unverified or assumed, what next check would close the gap
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
- If local and external evidence conflict, state the conflict explicitly and resolve it using the most authoritative source available. Do not silently discard either side.

## Output Formatting

- Use the field names defined in each mode's output section as markdown headers or bold labels.
- List each field, even when its value is short. Do not collapse multiple fields into prose.
- For `Findings` and similar lists: one item per line, ordered by severity.
- For `Observed Evidence` vs `Inference`: always place these as sub-items directly under the finding they support.
- For `Open Questions`: always include the resolution path classification (`Ask Now`, `Investigate from Source`, `Investigate Externally`, `Assume Explicitly`).
- Do not omit required fields. If a required field has no content, write "none" rather than skipping it.

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
