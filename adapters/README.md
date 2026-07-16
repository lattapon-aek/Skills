# Adapters

Platform-specific install paths for the software-engineering suite. The adapters are scripts and commands, not subfolders here.

## Available Targets

- Claude Code: `scripts/link-software-engineering-skills.ps1` links the shipped skills into `~/.claude/skills/`
- Codex: `scripts/link-codex-skills.ps1` links the shipped skills into `~/.codex/skills/`
- skills CLI: `npx skills add https://github.com/lattapon-aek/Skills` for a portable install

Keep the core doctrine in `suites/software-engineering/` and treat adapters as packaging only.
