# End-To-End Core Flow Tests

Fixtures for running a single agent through the suite-level orchestration flow on one real task.

## Scenario

- `sample-app/incidents/payment-retry/`: incident bundle from the failure point
- `sample-app/src/payments/retry-status-mapper.ts`: live defective mapper
- `sample-app/src/payments/retry-status-mapper.test.ts`: focused regression proof
- `../implementation/sample-app/src/openai/client.ts`: OpenAI wrapper seam for a narrow migration
- `../implementation/sample-app/src/openai/support-assistant.ts`: caller contract that should stay stable
- `../implementation/sample-app/src/openai/support-assistant.test.ts`: focused implementation proof for the migration path

## Goal

Verify how one agent behaves end-to-end when:

- the task begins with a user request and incident artifacts
- the incident may or may not still reproduce in the current workspace
- the task may require a design or architecture decision before coding starts
- the agent must clarify scope, debug from evidence, implement a narrow fix, and prove the issue is gone
- the agent must then review the resulting change or no-change outcome for remaining risk and proof gaps

## Covered Flow

1. core `Clarify`
2. core `Plan` when design choice is still open
3. core `Analyze`
4. core `Implement`
5. `change-review`

This suite is meant to test not only each phase in isolation, but also the handoff quality between:

- objective shaping -> diagnosis
- objective shaping -> design decision
- design decision -> diagnosis or implementation
- diagnosis -> implementation
- implementation -> verification
- verification -> final review

## Suggested Orchestration Cases

1. Incident-driven bug that goes through `Clarify -> Analyze -> Implement -> change-review`
2. Integration or migration task that goes through `Clarify -> Plan -> Implement -> change-review`

## Full 5-Phase OpenAI Flow

See [openai-responses/README.md](openai-responses/README.md) for a concrete end-to-end fixture that ties together:

- intake and planning inputs
- implementation seam and focused proof
- final review diff and validation artifact
