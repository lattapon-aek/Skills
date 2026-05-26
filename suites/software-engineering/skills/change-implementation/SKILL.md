---
name: change-implementation
description: Implement repository changes with an evidence-first, scope-first workflow. Use when an agent must add or modify software behavior, refactor code, or update internal tooling while grounding decisions in the real codebase, narrowing scope, assessing impact, and verifying results before claiming success.
---

# Change Implementation

## Intent

Implement the right change, not the fastest-looking change. Read the real repo first, narrow the scope, then execute in small verified steps.
Stay in execution mode: inspect, edit, and verify the requested change. Do not silently drift into open-ended architecture work, broad redesign, or prolonged research when the task is really blocked on missing objective, missing access, or missing evidence.
Do not propose a fix from pattern-matching alone. Trace the real source path until you can point to the concrete file, function, code path, or configuration entry that must change.
Before editing, be able to explain why that exact place must change, what surrounding behavior depends on it, and what could break if you change it incorrectly.

## Four Principles

Apply these principles throughout the job:

### 1. Think Before Coding

- State assumptions explicitly.
- Surface ambiguity and tradeoffs instead of picking silently.
- Push back when evidence supports a simpler or safer approach.

### 2. Simplicity First

- Implement the minimum code that solves the real problem.
- Do not add speculative abstraction, configurability, or edge handling that was not requested.
- If a smaller implementation is sufficient, prefer it.

### 3. Surgical Changes

- Touch only lines that trace directly to the request.
- Do not refactor adjacent code unless a narrow change cannot solve the problem safely.
- Clean up only the mess created by your own change.

### 4. Goal-Driven Execution

- Define proof before editing.
- Pair each step with a concrete verification target.
- Do not stop at "looks right"; stop at "proved right."

## Clarify Until Clear

- Restate the objective, expected result, and success criteria before editing.
- Ask follow-up questions when ambiguity affects correctness, architecture, access, or user-visible behavior.
- Make an explicit assumption only when the risk is low and the choice is reversible.
- If the task is still fundamentally underspecified, stop and push it back through intake instead of pretending execution has started.

## When Not To Use

- Do not use this skill when the main problem is still understanding an unclear request; route that through `task-intake`.
- Do not use this skill when the main problem is still proving the root cause of a failure; route that through `root-cause-debugging`.
- Do not use this skill as a substitute for reviewing an already completed diff; use `change-review`.

## Source Of Truth

Use the best available evidence before changing code:

- Inspect the relevant files, code paths, config, tests, logs, command output, and current repo state before proposing an approach.
- Trace the behavior through the real implementation until you know where the bug, constraint, or requested behavior actually lives.
- Search external sources when the task depends on library behavior, framework APIs, vendor docs, standards, version-specific behavior, or current ecosystem facts not provable from the workspace alone.
- Prefer official docs, release notes, source repos, and primary references over summaries.
- Treat framework conventions and memory as hints, not evidence.
- When describing current behavior, cite the artifact or external source that supports the claim.
- Gather enough evidence to choose a safe implementation path, then start editing. Do not turn execution into indefinite research once the next step is already clear.

## Evidence Sufficiency

Execution can proceed when all of these are true:

- the target behavior is specific enough to implement
- the relevant local code path or artifact is identified
- the concrete change location is known at the level of file, function, config entry, template, query, or command
- any external behavior that materially affects correctness has an authoritative source
- the smallest safe implementation surface is visible
- there is at least one concrete verification path

If these are not true, either ask the user for the missing blocker or route the task back through intake.

## Scope Narrowing

- Define the smallest implementation surface that can solve the real problem.
- Avoid speculative abstraction or opportunistic refactors.
- Expand the scope only when a narrow patch cannot solve the issue safely.
- Prefer a 3-line fix over a 100-line rewrite when both solve the same proven problem.
- If the change grows, explain exactly which newly discovered evidence forced the scope to expand.

## Change Analysis

Before you edit, be able to answer all of these:

- What exact behavior is wrong or missing now
- Where that behavior is implemented today
- Why that location is the correct patch point
- What alternative patch points exist and why they are worse
- What local and adjacent behavior could be affected by the change
- What must remain unchanged after the fix
- What plausible implementation approaches were rejected and what evidence ruled them out

## Work In Parts

1. Inspect the current implementation.
2. Trace the exact place that must change.
3. Identify the smallest coherent patch plan.
4. Execute one part at a time.
5. Re-check behavior after each meaningful step.

## Patch Plan

Before editing, be able to state:

- which file(s) must change
- which function, block, query, config, or template is responsible
- what exact behavior must change there
- what code must stay untouched
- why a smaller patch would be insufficient, if the change is larger than expected
- what side effects or regressions this patch could cause
- what adjacent areas must be checked after the patch

## Impact And Tradeoffs

- Call out user-visible changes, compatibility risks, migration needs, and areas likely to break.
- Recommend the safer or more correct option when a larger change is justified by evidence.
- Do not avoid a necessary refactor merely because it is larger; explain why the larger change is warranted.
- Identify the blast radius around the patch: callers, downstream consumers, data shape, contracts, tests, runtime behavior, and operational consequences.
- Treat impact analysis as part of the work, not as an afterthought after coding.

## Execution Boundaries

- Do not expand a code change into a redesign unless the narrower fix cannot solve the problem safely.
- Do not browse or research beyond the decision you need for the next implementation step.
- If new information reveals that the real problem is different from the brief, stop and surface that mismatch instead of continuing on stale assumptions.
- If access to critical files, systems, or authoritative docs is missing, report the blocker directly instead of simulating progress.
- Do not edit broad surrounding code just because you are already in the file.
- Do not convert a local fix into a cleanup pass unless the cleanup is required for correctness.

## Verification

- Prove the change with the lightest meaningful check: focused tests, a reproduction path, a build step, or a direct runtime check.
- If correctness depends on external behavior or docs, state which external evidence was used and what was still validated locally.
- Do not claim success from code inspection alone when behavior can be exercised.
- Do not treat “finished coding” as “finished work”. The work is not done until the target behavior has been observed to work or the original failure has been observed to disappear.
- If verification is blocked, state exactly what was not proven.
- Verify not only the target fix, but also the most likely adjacent regressions implied by the patch.
- Prefer tangible proof: passing focused tests, successful reproductions, measured metrics, observed output, or runtime behavior that demonstrates the change actually worked.

## Proof Gap Rule

- State what the current evidence already proves about the change.
- State what is still unproven, unverified, or blocked.
- State the next concrete check required to close that proof gap.

## Output

Report:

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

For very small changes, do not collapse or omit `Change Location` or `Why This Patch Point`. The response may be shorter overall, but those two fields must still be explicit.
If no proof has been run yet, `Observed Result` must say that no real result has been observed yet and that the work is not complete.

## Phase Handoff

- Hand back to `task-intake` if the task is still too unclear to execute safely.
- Hand back to `root-cause-debugging` if a failure still lacks a proven root cause.
- Hand off to `change-review` after a change or justified no-change outcome is ready for acceptance review.

## Reference

Use [references/execution-checklist.md](references/execution-checklist.md) as the execution checklist.
Use [../../references/four-principles.md](../../references/four-principles.md) for the shared doctrine and rationale.
