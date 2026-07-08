# Final Report: AGENTS.md Skill Enforcement Guidance

## Objective

Document how users should configure repository `AGENTS.md` files so agents consistently select the software-engineering skills instead of skipping them for small edits.

## What Changed

- Added an `Enforce Skill Use With AGENTS.md` section to the suite README.
- Added a copy-paste `AGENTS.md` policy snippet.
- Explained that skill installation makes skills available but does not guarantee automatic selection.
- Added a root README pointer to the new policy guidance.
- Added this work packet and final report as audit artifacts.

## Files Touched

- `README.md`
- `suites/software-engineering/README.md`
- `suites/software-engineering/work-packets/agents-md-guidance-work-packet.md`
- `suites/software-engineering/work-packets/agents-md-guidance-final-report.md`

## Decisions

- Put the full copy-paste policy in the suite README because that is the primary entry point for users.
- Keep the root README as a short pointer.
- Recommend both repo-local `AGENTS.md` and global agent instructions for stricter enforcement.

## Verification

- `git diff --check` passed.
- `./scripts/validate-suite.sh` passed.

## Observed Evidence

- Skill validation reported all three skills valid.
- Node fixture output reported 3 passing core tests and 1 passing change-review test.
- Suite validation reported structure, registration, and stale routing scans passed.

## Remaining Risks

- This documents enforcement guidance; actual compliance still depends on users adding the snippet to their project `AGENTS.md` or global instructions.

## Resume Or Follow-up Notes

If stronger enforcement is needed later, add a dedicated install section or script that writes an `AGENTS.md` template into target projects.
