# Software Engineering Core Tests

Fixtures for forward-testing the single `software-engineering-core` skill across its internal modes.

## Modes Covered

- `planning/`: design, migration, and boundary-decision cases
- `analysis/`: incident, bug, runtime, tooling, and failure-domain cases
- `implementation/`: narrow patch and verification cases
- `flows/`: end-to-end orchestration through multiple core modes and final review

## Goal

Verify that one skill can:

- clarify the real objective
- classify the right failure or decision domain
- choose the narrowest justified mode
- prove conclusions before mode transitions
- hand off accepted outcomes to `change-review`
