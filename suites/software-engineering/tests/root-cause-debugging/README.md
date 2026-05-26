# Root Cause Debugging Tests

Focused fixtures for forward-testing the `root-cause-debugging` skill on real files in this repository.

## Goals

- Verify that the agent reproduces or simulates the failure before claiming a root cause.
- Verify that the agent traces from the visible symptom to the exact fault location.
- Verify that the agent separates second-hand reports from directly observed evidence.
- Verify that the agent refuses to call the bug fixed until the failing path is proven to work.

## Fixtures

- `sample-app/src/auth/login.ts`: a local bug where the visible symptom is a wrong error reason
- `sample-app/src/orders/status-summary.ts`: a data-path bug where the failure should be reduced to a small input case
- `sample-app/src/billing/invoice-total.ts`: a misleading-log case where rounding looks suspicious but the real defect is in discount application order
- `sample-app/incidents/payment-status/`: an incident bundle with logs and payloads that should be inspected before simulation

## Suggested Cases

1. Reproduce the login failure and trace the exact branch that returns the wrong reason.
2. Build a small order fixture that simulates the reported count mismatch, then trace the filter that introduces it.
3. Use a small invoice simulation to rule out a misleading rounding hypothesis and trace the real defect.
4. Start from an incident log bundle, extract the real failing signal, and only then simulate the code path.
