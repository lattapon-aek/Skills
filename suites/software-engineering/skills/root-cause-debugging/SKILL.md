---
name: root-cause-debugging
description: Investigate software defects with an evidence-first, root-cause-driven workflow. Use when an agent must debug failing tests, incorrect behavior, crashes, regressions, data issues, or environment-specific problems and prove the root issue is understood before fixing it.
---

# Root Cause Debugging

## Intent

Treat every bug as an investigation. Do not patch symptoms until the underlying cause is supported by evidence.
Stay in debugging mode: reproduce, inspect, isolate, prove, and only then patch. Do not silently drift into generic cleanup, redesign, or speculative fixes.
Do not claim a root cause from pattern-matching alone. Trace the failure through the real source path until you can point to the concrete file, function, query, config, or runtime step where the failure is actually introduced.
Do not trust reports, screenshots, logs, or user descriptions as sufficient proof by themselves when the failure can be reproduced or simulated. Recreate the failure path yourself whenever feasible so you can see where it actually happens.
When incident evidence exists near the point of failure, gather it first: logs, traces, requests, responses, payloads, timestamps, metrics, failing inputs, runtime output, and environment details. Use simulation to explain or confirm that evidence, not to replace it.
Default boundary: this skill owns diagnosis first. If the task explicitly includes fixing the issue, debugging may continue into a narrow fix after the root cause is proven. If the diagnosis is still uncertain, do not drift into patching.

## Four Principles

Apply these principles during investigation:

### 1. Think Before Coding

- Do not commit to a root cause before the evidence supports it.
- Surface competing hypotheses and eliminate them deliberately.
- Ask for missing reproduction context when the failure is underspecified.

### 2. Simplicity First

- Prefer the smallest explanation that fits the evidence.
- Fix the confirmed cause without bundling speculative hardening or unrelated cleanup.

### 3. Surgical Changes

- Keep the fix tied to the proven root cause.
- Do not mix debugging with opportunistic refactoring.

### 4. Goal-Driven Execution

- Reproduce the failure first when feasible.
- Define the proof that the real issue is resolved.
- Re-run the failing path and adjacent checks before claiming success.

## Clarify Until Clear

- Define the failure precisely: expected behavior, actual behavior, environment, and trigger.
- Ask for missing reproduction context when the issue cannot be investigated reliably without it.
- Narrow the objective to one confirmed failure mode at a time.
- Ask for or locate the closest incident evidence available from the failure point before expanding into broader theories.
- If no reproduction or simulation path exists yet, prioritize building one before debating causes.

## When Not To Use

- Do not use this skill for ordinary feature implementation when no unexplained failure or regression exists.
- Do not use this skill when the request is still fundamentally unclear; route that through `task-intake`.
- Do not use this skill as a substitute for final diff acceptance; use `change-review`.

## Source Of Truth

Use the best available evidence for the investigation:

- Start from failing tests, logs, stack traces, commands, user steps, data samples, runtime behavior, and the relevant code.
- Prefer evidence captured at or near the failure point before relying on downstream symptoms or retrospective explanations.
- Trace from the observed failure back through the real implementation until you know where the defect is introduced, not just where it becomes visible.
- Search external sources when the failure may depend on vendor behavior, framework bugs, documented limits, protocol details, or version-specific changes not provable from the repo alone.
- Prefer official docs, changelogs, issue trackers from maintainers, and primary references before community speculation.
- Separate observed facts from hypotheses.
- If the evidence does not support a claimed root cause, keep investigating.
- Treat second-hand descriptions as leads, not proof. Try to observe the failure yourself through a reproduction, a minimal test, a debug run, or another simulation path.
- If logs or traces exist but are incomplete, say what is missing and what additional capture would most reduce uncertainty.

## Root Cause Sufficiency

Do not call something the root cause until all of these are true:

- the closest available incident evidence has been reviewed or explicitly noted as unavailable
- the failure is reproduced or otherwise anchored in concrete evidence
- a reproduction, simulation, or direct observation path has been attempted whenever feasible
- the exact fault location is known at the level of file, function, query, config, template, dependency boundary, or runtime step
- competing explanations have been ruled out or made less likely with evidence
- the proposed fix is tied directly to that fault location
- there is a concrete plan to prove the original failure disappears after the fix

## Scope Narrowing

- Isolate the smallest reproducible case.
- Distinguish root cause from side effects, secondary errors, and noisy symptoms.
- Fix one confirmed cause at a time unless multiple causes are tightly coupled.
- Prefer the smallest fix that removes the proven cause.
- If the scope grows, explain what evidence showed the original patch would have been insufficient.

## Reproduction Strategy

Before or during debugging, try to establish one of these:

- incident logs, traces, requests, payloads, metrics, or runtime output from the real failing path
- a failing automated test
- a deterministic command or request
- a minimal fixture or input sample
- a local debug run with the same failure
- a simulated path that reproduces the same symptom under controlled conditions

If real incident evidence exists, inspect it before relying on simulation alone. If none of these are possible, state why and reduce confidence accordingly.

## Work In Parts

1. Gather incident evidence from the failure point.
2. Reproduce or simulate the failure.
3. Inspect the code and runtime evidence around the failure.
4. Form hypotheses and eliminate them with evidence.
5. Trace the exact fault location.
6. Confirm the root cause.
7. If fixing is in scope and the root cause is proven, implement the smallest fix that addresses that cause.

## Fault Analysis

Before patching, be able to answer:

- What exact failure is happening now
- What direct incident evidence exists from the failure point
- Where the failure first becomes observable
- Where the defect is actually introduced
- Why that location is the root cause instead of just a symptom site
- What nearby code paths or data paths could produce similar symptoms but have been ruled out
- What competing hypotheses were considered and what evidence ruled them out
- What must remain unchanged after the fix
- What incident evidence plus reproduction or simulation path proves the diagnosis

## Impact And Tradeoffs

- State what systems, data paths, or user flows are affected.
- Call out the risk of regressions or hidden sibling defects.
- Recommend broader remediation when the evidence shows the local bug is a symptom of a larger design issue.
- Identify the likely blast radius around the fix: callers, downstream consumers, contracts, data shape, tests, and runtime behavior.

## Verification

- Re-run the failing path after the fix.
- Add or update regression coverage when the repo supports it.
- Check adjacent behavior that could be impacted by the same cause.
- If the diagnosis relied on external evidence, cite that evidence and still prove the fix against the local failing behavior.
- If logs, traces, or metrics were part of the diagnosis, confirm that the same signals now show the failure is gone or the behavior is corrected.
- If reproduction was impossible, state what evidence was used instead and why confidence is limited.
- Do not treat “code changed” as “bug fixed”. The bug is not fixed until the original failure is observed to disappear or the target behavior is observed to work.
- Prefer tangible proof: a previously failing test now passes, a broken repro now works, an error no longer occurs, or a measured symptom is gone.

## Proof Gap Rule

- State what the incident evidence and reproduction path already prove.
- State what is still uncertain, unobserved, or outside the verified failure path.
- State what additional capture, reproduction, or downstream inspection would close that gap.

## Debugging Boundaries

- If the task is diagnosis-only, stop after proving the root cause and state the smallest justified fix scope without editing.
- If the task includes fixing, do not patch until the root cause meets the sufficiency bar above.
- If the root cause is not yet proven, route the remaining work as continued debugging, not implementation.

## Phase Handoff

- Hand back to `task-intake` if the failure description is still too unclear to investigate responsibly.
- Hand off to `change-implementation` when the root cause is proven and fixing is in scope.
- Hand off to `change-review` after a change or justified no-change conclusion is ready to be assessed.

## Output

Report:

- `Failure`
- `Evidence`
- `Incident Evidence`
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

## Reference

Use [references/debug-playbook.md](references/debug-playbook.md) when you need a deeper debugging checklist.
Use [../../references/four-principles.md](../../references/four-principles.md) for the shared doctrine and rationale.
