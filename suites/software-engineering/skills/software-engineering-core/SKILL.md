---
name: software-engineering-core
description: Primary working skill for software-engineering tasks. Use when an agent must clarify an objective, choose an approach, diagnose a failure, implement a scoped change, or justify no patch from evidence. Owns the work until a concrete result or no-patch conclusion is ready; then hand proof through verification-hazards when green/red evidence is being trusted and change-review for acceptance.
---

# Software Engineering Core

## Intent

Use one disciplined workflow for software-engineering work instead of switching mental models per task. Start by clarifying the objective, classify the failure or decision domain, gather the best available evidence, choose the next justified mode, and prove each conclusion before moving on.
Stay in core mode: move between clarification, planning, diagnosis, and implementation only when the current evidence justifies that transition. Do not silently jump from a vague request to a patch, from a report to a root cause, or from a design idea to a rewrite.
Golden rule: one skill, multiple modes. Pick the narrowest mode that fits the current evidence, and keep the work scoped to that mode until the proof gap changes.

## Suite Role

This is the default owner for engineering work. Use it to decide what the task really is, what evidence is available, which mode is justified, and what action is safe.

Do not use this skill as a loose checklist. It must either:

- produce a justified next mode and action,
- produce a concrete implementation or no-patch result, or
- stop with the specific proof gap that blocks safe progress.

When the result depends on a green/red run or an agent report, hand the claim to `verification-hazards` before acceptance. When an end state is ready, hand it to `change-review`.

## Must Obey

- Do not skip the current gate because the next step seems obvious.
- Do not patch before objective, domain, and patch boundary are supported by evidence.
- Do not call work done without observed verification and a stated proof gap.
- Do not use `change-review` or `verification-hazards` as a substitute for core diagnosis or implementation.
- Do not start substantial work without a working document, user-supplied task document, or explicit inline work packet for small one-turn tasks.

## Mindset Contract

Optimize for a proven engineering outcome, not for producing code first.

- A patch is only one possible outcome.
- `No patch` is valid when evidence does not justify a change.
- A user report is a lead, not proof.
- Memory and conventions are hints, not evidence.
- "Verified" means observed output from source, tests, logs, runtime behavior, or authoritative docs.
- Review is not optional for an accepted patch or accepted `no patch` conclusion.
- The agent must not proceed to the next phase only because the current phase feels likely; it needs a stated gate, evidence, and proof gap.

## Default Thought Path

Use this mental path before acting:

`request -> document gate -> objective -> evidence -> domain -> mode -> action -> proof -> verification-hazards when proof depends on a green/red result -> review`

If any link is missing, do the smallest step that closes that gap. Do not skip from `request` to `action`.

## When To Use

Use this skill for most software-engineering work, including:

- vague or broad requests that still need shaping
- implementation work where the patch point must be traced first
- design or migration choices that need a recommendation before coding
- bugs, regressions, runtime issues, and environment failures that need diagnosis
- multi-step tasks that may move from clarification to planning, diagnosis, or implementation

## When Not To Use

- Do not use this skill as a substitute for a false-green scan; use `verification-hazards` when proof depends on a green/red result or agent report.
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

1. What working document records the task contract, or do I need to create one before substantial action?
2. What is the real objective?
3. What failure domain or decision domain am I actually in?
4. What evidence do I already have?
5. What is the narrowest justified next mode?
6. What is already proven, and what is still a proof gap?
7. Could the current green or red result be lying because it used the wrong layer, surface, cause, artifact, or baseline?

The main modes inside this skill are:

- `Clarify` for intake and scope shaping
- `Plan` for solution, migration, or boundary decisions
- `Analyze` for bugs, regressions, runtime issues, and unexplained behavior
- `Implement` for narrow, evidence-backed changes

Use `verification-hazards` as a verification lens inside any mode before trusting a green test, CI result, benchmark, agent report, or suspicious red result. When that lens applies, use `change-review` only after the hazard scan either confirms the result or names the remaining proof gap.

## Execution Loop

Use this loop for every mode, but keep it light when the task is small:

1. Read the request and restate the real objective.
2. Run the document gate: identify the user-supplied task document, create a work packet, or state the inline packet for a small one-turn task.
3. Collect the facts that can actually be inspected.
4. Decide whether you need `Clarify`, `Plan`, `Analyze`, or `Implement`.
5. Confirm the current assumption set against source material or runtime evidence.
6. Narrow the next action to the smallest justified step.
7. Run that step and observe the result.
8. Scan the observed result for verification hazards before treating it as proof.
9. Check impact, adjacent behavior, and proof gaps before moving on.

If the loop is still missing a fact that changes correctness, stop and confirm instead of guessing.

## Anti-Patterns

Avoid these behaviors even when the requested task sounds urgent:

- patching before the objective or patch boundary is clear
- treating a user report, issue title, or failing summary as confirmed root cause
- calling work verified without observed command, test, log, runtime, or authoritative-source output
- expanding scope because nearby code looks weak but is not part of the proof path
- using memory, naming, conventions, or pattern matching as proof when source or runtime evidence is inspectable
- weakening or deleting a test to make a fix look green
- accepting a green result without checking whether it exercised the shipping layer, full surface, proven cause, committed artifact, and stable baseline
- ending implementation with status prose instead of a review-shaped acceptance report
- relying on chat context as the only task record for multi-step work, design decisions, or user-agreed constraints
- resuming after compaction or handoff without reading the work packet, progress log, or user-supplied task document first

## Context Continuity

Apply [../../references/context-continuity.md](../../references/context-continuity.md) before substantial action.

The conversation context window is not a source of truth. Important task state must live in inspectable artifacts when the work may affect files, span phases, require decisions, or need later resume.

### Document Gate

Before planning, analyzing, implementing, or reviewing substantial work, confirm one of these is true:

- the user supplied a task document, packet, issue, PR, design brief, or runbook and you have identified it as the working document
- you created or updated a repo-local work packet using [references/work-packet-template.md](references/work-packet-template.md)
- the task is small enough for an inline work packet and no file artifact is needed
- the user explicitly declined artifacts and you stated the audit and resume risk

When the gate is closed, do not continue into implementation. Create the work packet or ask the user for the missing working document path when the correct location cannot be inferred safely.

### Continuity Updates

Update the working artifact when objective, scope, decision, source material, patch boundary, verification, proof gap, or next action changes. Use [references/progress-log-template.md](references/progress-log-template.md) for multi-step work and [references/final-report-template.md](references/final-report-template.md) before accepted completion.

After context compaction, interruption, or handoff, read the work packet or user-supplied task document before continuing. Then inspect current workspace state and distinguish documented facts from fresh observations.

## Confirm Gates

Pause and confirm with facts before crossing these gates:

- from user wording to objective
- from objective to plan
- from suspicion to root cause
- from root cause or plan to patch point
- from plan to implementation
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

**Gate: from plan to implementation** — this gate is CLOSED until all of the following are true:
- The patch boundary is confirmed by inspectable source read directly from the workspace, or by explicit user statement
- All questions marked `Ask Now` in the Plan output have been answered
- The `Proof Gap` in the Plan output has been reviewed and the remaining unknowns are acceptable to proceed

When this gate is closed, present the Plan output and stop. Do not begin Implement in the same response as Plan.

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
4. When the request is ambiguous or has multiple plausible readings, Ruled-out Interpretations lists at least one alternative reading that was considered and rejected.
5. The objective can be stated in one concrete sentence with a verifiable success condition.

If any exit condition is not yet met, present the Clarify output and stop. Do not transition to another mode in the same response.

### Clarify Output

Required fields (always include):

- `Working Document`
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

- `Working Document`
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

- `Working Document`
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

#### Assumption Re-validation

Before editing, re-validate every assumption listed in any prior Clarify or Plan output:

- Read the relevant source files again; do not rely on what was read in an earlier phase.
- State which assumptions held against current evidence.
- State which assumptions required revision and how that changes the patch boundary.
- If a revised assumption invalidates the current plan, return to `Plan` before proceeding.

#### Reversibility Gate

Before editing, confirm whether the change can be rolled back cleanly:

- can the patch be reverted without extra migration work
- does the change affect callers outside this file or repository, including other services or repos that depend on the changed signature, return type, behavior, or data shape
- does the change require a staged rollout or deprecation notice for external callers
- will the tests catch the intended rollback risk
- is a narrower patch available if reversibility is weak

#### Implement Output

- `Working Document`
- `Objective`
- `Evidence`
- `External Evidence`
- `Assumptions`
- `Change Location`
- `Why This Patch Point`
- `Reversibility Assessment` — whether the patch can be reverted cleanly; whether caller contracts are preserved; whether tests catch rollback risk; whether a narrower patch is available if reversibility is weak
- `Caller Contract Impact` — whether callers outside this file or repository depend on the changed signature, return type, behavior, or data shape; whether a staged rollout or deprecation notice is required; none if the change is purely internal with no external consumers
- `Rejected Approaches`
- `Scoped Plan`
- `Out of Scope`
- `Impact and Tradeoffs`
- `Verification`
- `Test Coverage` — list of test cases that exercise this patch; must be runnable and observed green before `Observed Result` is valid; if no tests exist for this path, state that explicitly as a proof gap
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
- **Verified means:** a command was run and its output was observed, or a test was executed and its result was included. Model self-assertion without execution does not count as verification. "It should work" is not an observed result.

## Output Formatting

- Use the field names defined in each mode's output section as markdown headers or bold labels.
- List each field, even when its value is short. Do not collapse multiple fields into prose.
- For `Findings` and similar lists: one item per line, ordered by severity.
- For `Observed Evidence` vs `Inference`: always place these as sub-items directly under the finding they support.
- For `Open Questions`: always include the resolution path classification (`Ask Now`, `Investigate from Source`, `Investigate Externally`, `Assume Explicitly`).
- Do not omit required fields. If a required field has no content, write "none" rather than skipping it.

### Compact Output For Small Tasks

For small, clear tasks, keep field values terse instead of expanding into a long report. Preserve the proof path with these fields:

- `Objective`
- `Working Document`
- `Evidence`
- `Mode`
- `Change` or `No Patch`
- `Verification`
- `Proof Gap`
- `Residual Risk`

Compact output is not permission to skip evidence, verification, or review handoff. It is only a shorter format for the same reasoning.

### No-Patch Pattern

Use `no patch` when current evidence does not justify a code change. State it plainly:

- `No Patch`: why no change is justified in the current workspace
- `Observed Evidence`: source, test, log, runtime, or authoritative docs that support that conclusion
- `Ruled-out Hypotheses`: likely explanations or fixes that were checked and rejected
- `Residual Risk`: what historical or external condition may still differ from current evidence
- `Review`: hand off to `change-review` shape before acceptance

## Escalation And Boundaries

- If the objective is still unclear, stay in `Clarify`.
- If the task needs a design or migration choice, move to `Plan`.
- If the task is blocked on understanding a failure, move to `Analyze`.
- If the approach and patch boundary are clear, move to `Implement`.
- If implementation reveals an unproven failure mechanism, go back to `Analyze`.
- If current evidence does not justify any change, `no patch` is valid.

**Mandatory stop conditions** — stop immediately, surface the situation to the user, and do not proceed when:

1. The fix requires deleting, disabling, or weakening an existing test to pass.
2. The change boundary has grown beyond the patch point stated in the current Implement output.
3. The Proof Gap cannot be closed after two directed searches for the required evidence.
4. Implementation reveals a failure mechanism that was not diagnosed in Analyze — return to `Analyze` before editing further.

## Proof Gap Rule

For any mode, always state:

- what the current evidence already proves
- what is still unproven, assumed, or blocked
- what next evidence, check, or mode transition would close the gap

## Phase Handoff

- Stay inside `software-engineering-core` until the work reaches either:
  - a concrete implementation result, or
  - a justified `no patch` conclusion
- Before handoff, use `verification-hazards` when the acceptance evidence includes a green test, CI result, benchmark, agent report, or red result attributed to the change.
- Hand off to `change-review` for every accepted end state, including self-review and `no patch`. Include any `verification-hazards` verdict or proof gap in the review evidence.

## Reference

Use these references as needed:

- [references/intake-template.md](references/intake-template.md)
- [references/planning-template.md](references/planning-template.md)
- [references/analysis-playbook.md](references/analysis-playbook.md)
- [references/implementation-checklist.md](references/implementation-checklist.md)
- [references/output-patterns.md](references/output-patterns.md)
- [references/work-packet-template.md](references/work-packet-template.md)
- [references/progress-log-template.md](references/progress-log-template.md)
- [references/final-report-template.md](references/final-report-template.md)
- [../../references/four-principles.md](../../references/four-principles.md)
- [../../references/context-continuity.md](../../references/context-continuity.md)
