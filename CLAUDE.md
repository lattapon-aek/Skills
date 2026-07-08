# Repository Guidelines

This repository packages software-engineering skills for reuse across AI agents.

## What to Read First

- `README.md`
- `suites/software-engineering/README.md`
- `AGENTS.md`

## Installed Skills

- `software-engineering-core`
- `change-review`
- `verification-hazards`

## Local Claude Setup

For Claude Code, link the shipped skills into the local skill directory:

```powershell
.\scripts\link-software-engineering-skills.ps1
```

This creates links from the repo into `~/.claude/skills/` by default.

## Working Rules

- Keep changes inside `suites/software-engineering/` unless the repo-level install or docs need updating.
- Preserve the evidence-first workflow.
- Do not weaken `change-review`; it is the final acceptance gate.
- When adding or changing skills, update the manifest and the suite README together.

## Validation

- Validate changed skills before shipping them.
- Run at least one representative `node --test` fixture after workflow changes.
