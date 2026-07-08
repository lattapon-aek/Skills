# AI Agent Skills

This repository now organizes the software-engineering skills as a single suite.

## Install

Install the portable skill bundle with the open skills CLI:

```powershell
npx skills add https://github.com/lattapon-aek/Skills
```

To install only the shipped software-engineering skills:

```powershell
npx skills add https://github.com/lattapon-aek/Skills --skill software-engineering-core --skill change-review --skill verification-hazards
```

For local Claude Code use, link the shipped skills into the local skill directory:

```powershell
.\scripts\link-software-engineering-skills.ps1
```

For local Codex use, link the shipped skills into the local skill directory:

```powershell
.\scripts\link-codex-skills.ps1
```

Primary entry point:

- [suites/software-engineering/README.md](suites/software-engineering/README.md)

Repo-level structure:

```text
suites/
  software-engineering/
scripts/
  new-skill.ps1
  validate-suite.sh
```

Use the suite README for:

- skill catalog
- shared doctrine
- routing guidance
- stress-test layout
- validation commands
