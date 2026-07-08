# Work Packet: Context Continuity File-Edit Follow-up

## Objective

Tighten context continuity so agents must create or identify a file artifact before any file-changing work, including small one-file apps in an empty workspace.

## User Instructions

- The previous behavior still let an agent inspect an empty workspace and create `index.html` immediately after a chat-only game request.
- The expected behavior is that work has an inspectable start document before file edits.

## Source Documents

- User-provided transcript in the current conversation.
- `suites/software-engineering/references/context-continuity.md`
- `suites/software-engineering/skills/software-engineering-core/SKILL.md`
- `suites/software-engineering/tests/golden-transcripts/cases.md`

## Current Assumptions

- The failure happened because the doctrine still allowed an inline work packet for "very small one-turn work" and did not state that file-changing work always needs a file artifact.
- A shallow preflight to find repo instructions or an artifact location can be allowed, but implementation edits must wait until the working document exists.

## Scope

- Tighten context-continuity doctrine.
- Tighten `software-engineering-core` document gate wording.
- Add a golden transcript case matching the empty-workspace one-file game failure.
- Run suite validation.

## Out of Scope

- Building an automated live Codex transcript runner.
- Changing the generated snake game workspace.

## Decisions

- Inline work packets are allowed only for read-only, no-file-change, one-turn work.
- File-changing work requires a repo-local work packet unless the user supplied a working document or explicitly declined artifacts.
- Empty workspaces should use `.agent/work-packets/<task>.md` when no repo convention exists.

## Plan

1. Update context-continuity reference.
2. Update core skill document gate.
3. Add golden transcript case for one-file snake game in an empty workspace.
4. Validate and review.

## Proof Strategy

- `git diff --check`
- `./scripts/validate-suite.sh`

## Open Questions

- None blocking.

## Resume Instructions

Read this packet and inspect the current diff before continuing.
