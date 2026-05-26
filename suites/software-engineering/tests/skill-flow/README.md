# End-To-End Skill Flow Tests

Fixtures for running a single agent through `task-intake`, `root-cause-debugging`, `change-implementation`, and `change-review` on one real task.

## Scenario

- `sample-app/incidents/payment-retry/`: incident bundle from the failure point
- `sample-app/src/payments/retry-status-mapper.ts`: live defective mapper
- `sample-app/src/payments/retry-status-mapper.test.ts`: focused regression proof

## Goal

Verify how one agent behaves end-to-end when:

- the task begins with a user request and incident artifacts
- the incident may or may not still reproduce in the current workspace
- the agent must clarify scope, debug from evidence, implement a narrow fix, and prove the issue is gone
- the agent must then review the resulting change or no-change outcome for remaining risk and proof gaps

## Covered Flow

1. `task-intake`
2. `root-cause-debugging`
3. `change-implementation`
4. `change-review`

This suite is meant to test not only each phase in isolation, but also the handoff quality between:

- objective shaping -> diagnosis
- diagnosis -> implementation
- implementation -> verification
- verification -> final review
