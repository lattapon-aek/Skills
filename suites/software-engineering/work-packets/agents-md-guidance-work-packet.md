# Work Packet: AGENTS.md Skill Enforcement Guidance

## Objective

Document how users should instruct repository agents through `AGENTS.md` so installed skills are selected for file-changing software-engineering work instead of being skipped as optional tools.

## User Instructions

- Add README documentation that users can give to their agent or paste into their own `AGENTS.md`.
- Explain how to make agents use the software-engineering skills consistently.
- Address the observed failure mode where an agent skipped the skill because it considered the edit small.

## Source Documents

- User-provided transcript in the current conversation.
- `suites/software-engineering/README.md`
- `README.md`
- `suites/software-engineering/references/context-continuity.md`
- `suites/software-engineering/skills/software-engineering-core/SKILL.md`

## Current Assumptions

- Skill installation alone cannot guarantee automatic selection in every agent session.
- Repo-level `AGENTS.md` or global instructions are the reliable enforcement layer.
- The suite README is the best primary place for copy-paste policy guidance.

## Scope

- Update README documentation only.
- Include a copy-paste `AGENTS.md` snippet.
- Include guidance for Codex and general agent usage.

## Out of Scope

- Changing agent runtime behavior.
- Editing user project `AGENTS.md` files outside this repo.
- Adding a separate website or generated docs.

## Decisions

- Put detailed guidance in `suites/software-engineering/README.md`.
- Add a short pointer from the root `README.md`.
- Use explicit wording that any file-changing software-engineering work must use `agents-skills:software-engineering-core`.

## Plan

1. Add an `Enforce Skill Use With AGENTS.md` section to the suite README.
2. Add a root README pointer to that section.
3. Run validation.

## Proof Strategy

- `git diff --check`
- `./scripts/validate-suite.sh`

## Open Questions

- None blocking.

## Resume Instructions

Read this work packet and current diff before continuing.
