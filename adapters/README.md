# Adapters

This folder contains platform-specific export helpers for the software-engineering suite.

## Available Targets

- `claude/`: local Claude Code setup via `scripts/link-software-engineering-skills.ps1`
- `codex/`: local Codex setup via `scripts/link-codex-skills.ps1`
- `skills-cli/`: portable install via `npx skills add`

Keep the core doctrine in `suites/software-engineering/` and treat adapters as packaging only.
