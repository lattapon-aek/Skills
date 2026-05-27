# Orchestration Policy

Use this policy when one software-engineering task may span multiple phases.

## Default Flow

1. `task-intake`
2. `solution-planning` when the objective is clear but the implementation approach is still unsettled
3. `root-cause-analysis` when the main obstacle is an unexplained failure, regression, or runtime mismatch
4. `change-implementation` when the objective and approach are clear enough to execute safely
5. `change-review` after a change or justified no-change outcome is ready to be assessed

Not every task requires all phases. The point is to move forward only when the current phase has produced enough evidence for the next one.

## Routing Rules

- Start with `task-intake` when the request is vague, broad, solution-biased, or missing proof of done.
- During `task-intake`, a shallow source scan is allowed when phase routing depends on locating the likely seam, boundary, or owning module. Do not turn that into proof or solution work.
- Route to `solution-planning` when the request is clear enough to act on but still needs a design, integration, migration, or boundary decision.
- Route to `root-cause-analysis` when the task is blocked on understanding a failure rather than choosing an implementation path.
- Route to `change-implementation` when the objective, approach, and patch boundary are clear enough to execute.
- Route to `change-review` when the result needs acceptance review, proof-gap review, or residual-risk review.
- Do not end a multi-phase task with implementation or debugging output alone; emit an explicit `change-review`-shaped final report for any accepted patch or justified `no patch` outcome.

## Escalation Rules

- If the objective is still unclear, go backward to `task-intake`, not forward into planning or coding.
- If implementation uncovers an unproven failure mechanism, go backward to `root-cause-analysis`.
- If debugging proves the code is already correct in the current workspace, prefer `no patch` and surface the historical-vs-current-state mismatch explicitly.
- If review finds a correctness gap that still lacks diagnosis, go backward to `root-cause-analysis`.
- If review finds a concrete execution gap with a clear fix, go backward to `change-implementation`.

## Required Reporting Across Phases

- Keep `Observed Evidence` separate from `Inference`.
- State `Current Workspace State` separately from `Historical Incident State` when they differ.
- Use the skill-specific ruled-out field to show what was considered and rejected.
- State proof gaps explicitly:
  - what is already proven
  - what is not yet proven
  - what next evidence or check would close the gap

## No-Patch Rule

`No patch` is a valid end state when:

- the current workspace does not reproduce the reported issue
- no justified code change is supported by evidence
- the agent clearly reports what was checked
- residual risk and remaining proof gaps are stated explicitly
