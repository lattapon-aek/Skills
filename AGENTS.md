# Repository Guidelines

## Project Structure & Module Organization

This repository is organized as a single suite under `suites/software-engineering/`.

- `skills/`: `software-engineering-core`, `change-review`, and `verification-hazards` (a verification lens for catching false-green results)
- `references/`: shared doctrine and orchestration guidance
- `tests/`: fixture-driven stress tests, with `software-engineering-core/` for core modes, `change-review/` for acceptance review, and `verification-hazards/` for false-green scenarios
- `scripts/new-skill.ps1`: scaffold for new skills

Keep new suite content inside `suites/software-engineering/`; avoid adding ad hoc files at the repo root.

## Build, Test, and Development Commands

- `python "C:\Users\lattapon.kea\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\suites\software-engineering\skills\software-engineering-core`
  Validates the core workflow skill. Replace the path with `change-review` when needed.
- `node --test suites/software-engineering/tests/software-engineering-core/flows/sample-app/src/payments/retry-status-mapper.test.ts`
  Runs a representative end-to-end fixture test.
- `node --test suites/software-engineering/tests/change-review/scenario-3/base/src/openai/support-assistant.test.ts`
  Runs a focused migration/review proof fixture.
- `./scripts/validate-suite.sh`
  Runs skill validation, representative fixtures, registration checks, and stale routing scans.
- `.\scripts\new-skill.ps1 -Name my-skill -DisplayName "My Skill" -ShortDescription "..." -DefaultPrompt "Use $my-skill ..."`
  Scaffolds a new skill.

## Coding Style & Naming Conventions

Use Markdown for docs and ASCII by default. Keep skill names lowercase and hyphenated, for example `software-engineering-core`. Each skill directory should contain `SKILL.md`, optional `agents/openai.yaml`, and optional `references/`.

Write short, directive prose. Prefer evidence-first wording and phase-based naming. Do not hardcode narrow case-specific rules into doctrine files.

## Testing Guidelines

Tests are fixture-based, not framework-heavy. Add new cases under the matching suite in `suites/software-engineering/tests/`. Prefer small, realistic artifacts over synthetic placeholders. Use `golden-transcripts/` for expected routing/output-shape examples and `mini-stress/` for small-model failure modes.

Name scenario folders and fixtures descriptively, for example `scenario-3/` or `artifacts/npm-sandbox-repro/`. Validate changed skills and run at least one relevant `node --test` fixture before submitting changes.

## Commit & Pull Request Guidelines

Recent commits use short imperative subjects, for example `Refine software engineering suite workflow`. Follow that style: one concise summary line, no trailing period.

PRs should describe:
- what changed
- which skills or fixtures were affected
- how the change was validated
- any remaining proof gaps or risks

## Agent-Specific Instructions

Preserve the suite’s doctrine: identify the real failure domain, separate observed evidence from inference, and prove outcomes before calling work complete. End accepted work with a `change-review`-shaped summary, including justified `no patch` outcomes.

Before the first engineering tool call or file edit, inspect the available skills, name the selected primary skill with one short reason, and only then begin work. Do not skip this preflight for small, single-file, visual, experimental, or greenfield tasks.
