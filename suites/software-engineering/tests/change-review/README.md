# Change Review Tests

Fixtures for testing the `change-review` skill against realistic diffs, surrounding code, and validation output.

## Scenario 1

- `pull-request.md`: stated objective of the change
- `proposed.diff`: the patch under review
- `base/`: surrounding files that the review should inspect
- `validation.txt`: claimed verification output

## Goal

Verify that review catches:

- correctness regressions hidden behind a plausible objective
- missing or weakened proof
- impact beyond the changed lines
- concerns that were considered but correctly ruled out

## Scenario 2

- a wider-looking diff that is still behavior-safe
- validation output is strong
- review should avoid inventing findings and instead surface ruled-out concerns and residual risk
