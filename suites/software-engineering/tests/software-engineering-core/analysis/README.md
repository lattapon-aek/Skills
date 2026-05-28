# Core Analysis Mode Tests

Focused fixtures for forward-testing the `software-engineering-core` skill in `Analyze` mode on real files in this repository.

## Goals

- Verify that the agent reproduces or simulates the failure before claiming a root cause.
- Verify that the agent traces from the visible symptom to the exact fault location.
- Verify that the agent separates second-hand reports from directly observed evidence.
- Verify that the agent refuses to call the bug fixed until the failing path is proven to work.
- Verify that the agent does not assume the issue lives in application code when the evidence points to tooling, runtime, sandbox, orchestration, or system-resource problems instead.

## Fixtures

- `sample-app/src/auth/login.ts`: a local bug where the visible symptom is a wrong error reason
- `sample-app/src/orders/status-summary.ts`: a data-path bug where the failure should be reduced to a small input case
- `sample-app/src/billing/invoice-total.ts`: a misleading-log case where rounding looks suspicious but the real defect is in discount application order
- `sample-app/incidents/payment-status/`: an incident bundle with logs and payloads that should be inspected before simulation
- `artifacts/npm-sandbox-repro/package.json`: a minimal dependency-install repro that helps distinguish application failures from sandbox, network, cache, or tooling failures

## Suggested Cases

1. Reproduce the login failure and trace the exact branch that returns the wrong reason.
2. Build a small order fixture that simulates the reported count mismatch, then trace the filter that introduces it.
3. Use a small invoice simulation to rule out a misleading rounding hypothesis and trace the real defect.
4. Start from an incident log bundle, extract the real failing signal, and only then simulate the code path.
5. Start from a tooling/runtime incident and prove whether the failure is in application code or in the surrounding execution environment.
