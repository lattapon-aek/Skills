# Context Continuity

Use this reference whenever a software-engineering task may outlive the current response, require multiple steps, alter workspace files, depend on user decisions, or need to survive context compaction.

## Intent

The conversation context window is not a source of truth. It is a working surface that can be compacted, truncated, or resumed by another agent. Important task state must live in inspectable workspace artifacts so the user and the next agent can audit what was agreed, what was done, what was proven, and what remains open.

## Document Gate

Before substantial action, confirm that the task has a working document.

Substantial action includes:

- editing code, docs, config, tests, generated assets, or repository metadata
- planning or designing a non-trivial change
- debugging across more than one file, command, log, or system boundary
- reviewing a diff, PR, branch, or patch set with acceptance consequences
- running a multi-step workflow, packet, migration, rollout, or release check
- any task likely to resume after a context transition

If the user supplied a task document, packet, issue, PR, design brief, or runbook, use it as the working document and cite its path or source in the response.

If no working document exists:

- for file-changing or multi-step work, create a work packet before implementation begins
- for planning or design work, create or update a decision-bearing work packet before presenting the plan as actionable
- for very small one-turn work, an inline work packet is acceptable, but state the objective, source material, proof of done, and proof gap
- if the user forbids creating artifacts, state the audit and resume risk explicitly before continuing

Do not treat private reasoning, chat memory, or a prior assistant summary as the working document.

## Required Artifacts

Use the smallest artifact set that preserves auditability.

### Work Packet

Create or identify this before substantial action. It records the job contract.

Required fields:

- `Objective`
- `User Instructions`
- `Source Documents`
- `Current Assumptions`
- `Scope`
- `Out of Scope`
- `Decisions`
- `Plan`
- `Proof Strategy`
- `Open Questions`
- `Resume Instructions`

### Progress Log

Create or update this when the work spans multiple steps, changes direction, uncovers new evidence, or needs interruption-safe state.

Required fields:

- `Timeline`
- `Evidence Inspected`
- `Decisions Made`
- `Changes Made`
- `Verification Runs`
- `Proof Gaps`
- `Next Action`

### Final Report

Create or update this before accepted completion for substantial work.

Required fields:

- `Objective`
- `What Changed`
- `Files Touched`
- `Decisions`
- `Verification`
- `Observed Evidence`
- `Remaining Risks`
- `Resume Or Follow-up Notes`

## Update Triggers

Update the working artifact when any of these changes:

- objective or scope
- user instruction or constraint
- decision or ruled-out option
- source material or evidence
- patch boundary
- verification result
- proof gap, residual risk, or next action

For long-running tasks, update before starting a risky edit, after each meaningful verification result, and before handing off or stopping.

## Resume Rule

After context compaction, interruption, handoff, or a new agent joining the work:

1. Read the work packet or user-supplied task document.
2. Read the progress log or latest final report if present.
3. Inspect current workspace state before trusting the document as current.
4. Continue from the recorded next action, or explain why current evidence invalidates it.

The resume answer must distinguish documented facts from fresh observations and assumptions.

## Artifact Location

Prefer a repo-local path that follows existing conventions, such as:

- `docs/work-packets/<task>.md`
- `doc/dev/impl/reports/<task>.md`
- `.agent/work-packets/<task>.md`
- a suite-specific path when the repo already has one

Do not add ad hoc root files when repository instructions define a documentation area.

## Anti-Patterns

- Starting a patch from a plan that exists only in chat.
- Saying "as discussed" without a document or source reference.
- Summarizing user decisions from memory after compaction.
- Treating the final chat response as the only report for multi-step work.
- Letting a progress log become a narrative dump without decisions, evidence, verification, and next action.
