# Context Continuity

Use this reference when work may outlive the current response, change files, depend on decisions, require multiple steps, or survive compaction or handoff.

## Intent

Chat context is a working surface, not durable truth. Preserve objective, authority, decisions, intended state, evidence, changes, proof gaps, deviations, and next action in inspectable artifacts.

Continuity choices affect only artifact durability. They never reduce evidence gathering, causal analysis, intent conformance, verification, or review rigor.

## Document Gate

Before substantial action, identify one of:

- a user-supplied issue, PR, packet, design brief, runbook, or task document
- a repo-local work packet
- a compact inline contract for genuinely one-turn, reversible work with low resume risk
- an explicit user refusal of artifacts, with audit and resume risk stated

Substantial action includes multi-file or multi-step planning, editing, debugging, review, migration, release work, or any task likely to resume after a context transition.

Do not treat task size as execution authority. An inline contract changes where state is recorded, not which gates the work must pass. Escalate to a durable work packet as soon as the task gains multiple decisions, files, systems, handoff risk, or acceptance consequences.

## Artifact Selection

### Inline Contract

Use only when the task can finish in one response, is reversible, has no migration or external-contract risk, and is unlikely to require handoff. Record at least objective, authority, intended state, source material, proof of done, allowed variations, and proof gap.

### Work Packet

Use for multi-step work, meaningful decisions, file changes likely to continue, or any task needing an auditable plan.

Required fields:

- `Objective`
- `User Instructions`
- `Authority Mode`
- `Required Sequence`
- `Source Documents`
- `Current Assumptions`
- `Scope`
- `Out of Scope`
- `Decisions`
- `Intended State`
- `Plan Commitments`
- `Allowed Variations`
- `Plan Amendment Authority`
- `Plan`
- `Proof Strategy`
- `Acceptance Matrix`
- `Deviations`
- `Open Questions`
- `Resume Instructions`

### Progress Log

Use when work spans turns, changes direction, uncovers material evidence, or needs interruption-safe state.

Record timeline, inspected evidence, decisions, changes, verification runs, conformance results, proof gaps, deviations, and next action.

### Final Report

Use before accepting substantial work. Record objective, intended and observed state, files touched, decisions, verification, acceptance coverage, conformance verdict, deviations, remaining risks, and follow-up state.

## Update Triggers

Update the working artifact when any of these changes:

- objective, authority, scope, or user instruction
- decision, assumption, intended state, or allowed variation
- controlling-system model, mechanism claim, or mechanism evidence
- source material, causal conclusion, or patch boundary
- implementation result or observed state
- verification, conformance, proof gap, residual risk, or next action

Record a material deviation when it occurs, including one later corrected. Never edit the original plan after implementation to make an unplanned result appear intended.

## Resume Rule

After compaction, interruption, handoff, or a new agent joining:

1. Read the working document.
2. Read the progress log or latest final report when present.
3. Inspect current workspace state before trusting recorded state as current.
4. Compare documented intended state with fresh observed state.
5. Resume from the recorded next action or explain which evidence invalidates it.

Distinguish documented facts, fresh observations, and assumptions.

## Artifact Location

Follow repository conventions such as:

- `docs/work-packets/<task>.md`
- `doc/dev/impl/reports/<task>.md`
- `.agent/work-packets/<task>.md`
- a suite-specific work-packet directory

Do not add ad hoc root files when the repository defines a documentation area.

## Compaction Checkpoint

Before compaction, a planned handoff, or ending a session mid-task, record in the working artifact:

- current owner skill and mode
- last proven gate and the next unmet gate
- exact artifact identities: branch, commit, files, build, or deployment under work
- active and rejected hypotheses with their deciding evidence
- approved change boundary and allowed variations
- pending checks and their expected observations
- next action and the condition that would route back

A resume that cannot find these facts must rebuild them from workspace evidence before continuing.

## Adaptive Reporting

Rigor is constant; verbosity adapts.

Use a compact report — `Current Gate`, `Action`, `Observed Evidence`, `Decision`, `Next Gate` — when evidence is clear, the scope was fully inspected, and no finding, deviation, or proof gap remains.

Expand to the full template when hypotheses compete, scope or plan changes, a deviation or proof gap exists, verification is incomplete, risk is high, or the work will be resumed or handed off. Never omit a deviation or proof gap to keep a report compact.

## Anti-Patterns

- Starting a substantial patch from a plan that exists only in chat.
- Using an inline contract to justify reduced proof or review.
- Saying “as discussed” without an inspectable source.
- Resuming from memory without reading artifacts and current workspace state.
- Rewriting a plan after the result diverges.
- Preserving a proposed architecture as a commitment after its controlling-mechanism theory was disproved.
- Letting a progress log become narrative without decisions, evidence, conformance, gaps, and next action.
- Compacting context or handing off without recording the checkpoint fields.
