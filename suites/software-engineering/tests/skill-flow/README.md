# End-To-End Skill Flow Tests

Fixtures for running a single agent through the suite-level orchestration flow on one real task.

## Scenario

- `sample-app/incidents/payment-retry/`: incident bundle from the failure point
- `sample-app/src/payments/retry-status-mapper.ts`: live defective mapper
- `sample-app/src/payments/retry-status-mapper.test.ts`: focused regression proof
- `../change-implementation/sample-app/src/openai/client.ts`: OpenAI wrapper seam for planning-first migration
- `../change-implementation/sample-app/src/openai/support-assistant.ts`: caller contract that should stay stable
- `../change-implementation/sample-app/src/openai/support-assistant.test.ts`: focused implementation proof for the migration path

## Goal

Verify how one agent behaves end-to-end when:

- the task begins with a user request and incident artifacts
- the incident may or may not still reproduce in the current workspace
- the task may require a design or architecture decision before coding starts
- the agent must clarify scope, debug from evidence, implement a narrow fix, and prove the issue is gone
- the agent must then review the resulting change or no-change outcome for remaining risk and proof gaps

## Covered Flow

1. `task-intake`
2. `solution-planning` when design choice is still open
3. `root-cause-analysis`
4. `change-implementation`
5. `change-review`

This suite is meant to test not only each phase in isolation, but also the handoff quality between:

- objective shaping -> diagnosis
- objective shaping -> design decision
- design decision -> diagnosis or implementation
- diagnosis -> implementation
- implementation -> verification
- verification -> final review

## Suggested Orchestration Cases

1. Incident-driven bug that goes through `task-intake -> root-cause-analysis -> change-implementation -> change-review`
2. Integration or migration task that goes through `task-intake -> solution-planning -> change-implementation -> change-review`

## Full 5-Phase OpenAI Flow

See [openai-responses/README.md](C:/Users/lattapon.kea/Desktop/Agents%20Skills/suites/software-engineering/tests/skill-flow/openai-responses/README.md) for a concrete end-to-end fixture that ties together:

- intake and planning inputs
- implementation seam and focused proof
- final review diff and validation artifact
