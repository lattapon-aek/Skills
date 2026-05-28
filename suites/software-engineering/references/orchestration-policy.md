# Orchestration Policy

Use this policy when one software-engineering task may span multiple phases.

## Default Flow

1. `software-engineering-core`
2. `change-review` after a change or justified no-change outcome is ready to be assessed

Not every task requires every core mode. The point is to move forward only when the current evidence justifies the next mode.

## Routing Rules

- Start in core `Clarify` mode when the request is vague, broad, solution-biased, or missing proof of done.
- During core `Clarify`, a shallow source scan is allowed when routing depends on locating the likely seam, boundary, or owning module. Do not turn that into proof or solution work.
- Route to core `Plan` when the request is clear enough to act on but still needs a design, integration, migration, or boundary decision.
- Route to core `Analyze` when the task is blocked on understanding a failure rather than choosing an implementation path.
- Route to core `Implement` when the objective, approach, and patch boundary are clear enough to execute.
- Route to `change-review` when the result needs acceptance review, proof-gap review, or residual-risk review.
- Do not end a multi-phase task with implementation or debugging output alone; emit an explicit `change-review`-shaped final report for any accepted patch or justified `no patch` outcome.

## Escalation Rules

- If the objective is still unclear, go backward to core `Clarify`, not forward into planning or coding.
- If implementation uncovers an unproven failure mechanism, go backward to core `Analyze`.
- If debugging proves the code is already correct in the current workspace, prefer `no patch` and surface the historical-vs-current-state mismatch explicitly.
- If review finds a correctness gap that still lacks diagnosis, go backward to core `Analyze`.
- If review finds a concrete execution gap with a clear fix, go backward to core `Implement`.

## Required Reporting Across Phases

- Keep `Observed Evidence` separate from `Inference`.
- State `Current Workspace State` separately from `Historical Incident State` when they differ.
- Use the skill-specific ruled-out field to show what was considered and rejected.
- State proof gaps explicitly:
  - what is already proven
  - what is not yet proven
  - what next evidence or check would close the gap

## Execution Loop

For multi-step work, enforce this loop:

1. inspect the facts that can actually be checked
2. confirm the current assumption set against source material or runtime evidence
3. choose the narrowest justified core mode
4. act on one small step
5. observe the result
6. re-check impact and proof gaps before moving on

If a fact is inspectable, inspect it instead of guessing. If the current evidence does not justify the next step, route back to the earlier core mode that can close the gap.

## No-Patch Rule

`No patch` is a valid end state when:

- the current workspace does not reproduce the reported issue
- no justified code change is supported by evidence
- the agent clearly reports what was checked
- residual risk and remaining proof gaps are stated explicitly
