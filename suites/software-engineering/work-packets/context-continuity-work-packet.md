# Work Packet: Context Continuity Discipline

## Objective

Make context continuity a default software-engineering suite behavior so agents preserve user instructions, plans, decisions, evidence, and proof gaps in workspace artifacts instead of relying only on the conversation context window.

## User Instructions

- If a prompt or task lacks a working document, the agent should notice and ask or inform the user before starting substantial work.
- Every meaningful work session should have a start document and an end summary.
- Planning and design decisions should have a document trail.
- Long-running work must survive context compaction and remain auditable by the user.
- User-supplied documents should be treated as the primary work context when present.

## Source Documents

- `AGENTS.md`
- `suites/software-engineering/skills/software-engineering-core/SKILL.md`
- `suites/software-engineering/references/orchestration-policy.md`
- `suites/software-engineering/README.md`
- `suites/software-engineering/tests/golden-transcripts/cases.md`

## Current Assumptions

- This should be suite-level behavior, not an optional standalone skill.
- Small one-turn questions may use inline context notes, but work that edits files or spans multiple steps needs file artifacts.
- The new behavior should add discipline without requiring heavy documents for trivial tasks.

## Scope

- Add a shared context-continuity reference.
- Add work-packet, progress-log, and final-report templates.
- Wire the document gate into `software-engineering-core`, orchestration policy, and suite README.
- Add golden transcript cases that make missing documents and resume behavior testable.

## Out of Scope

- Building an automated transcript runner.
- Changing runtime memory systems outside this repository.
- Rewriting existing skill modes beyond the document gate integration.

## Decisions

- Use `Context Continuity` as the shared doctrine name.
- Use `Document Gate` as the operational gate before substantial action.
- Keep artifacts inside `suites/software-engineering/` to follow repo structure.

## Plan

1. Add `references/context-continuity.md`.
2. Add core templates under `software-engineering-core/references/`.
3. Update core skill and orchestration policy to require the document gate.
4. Update suite README and golden transcript cases.
5. Run suite validation and inspect the diff.

## Proof Strategy

- Run `./scripts/validate-suite.sh`.
- Inspect `git diff --check`.
- Review the final diff for scope and consistency.

## Open Questions

- None blocking; artifact storage path can be adapted by each downstream repo.

## Resume Instructions

Read this work packet first, then inspect current git diff and continue from the first incomplete plan item.
