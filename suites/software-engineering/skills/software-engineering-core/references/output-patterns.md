# Output Patterns

Use these compact patterns when the full mode output would be too heavy for the task. Keep them evidence-first.

## Small Clear Implementation

- `Objective`: Implement the specific requested behavior.
- `Evidence`: Files, tests, docs, or runtime behavior inspected before editing.
- `Mode`: `Implement`.
- `Change`: The narrow patch point and why it is sufficient.
- `Verification`: Commands or runtime checks run and observed.
- `Proof Gap`: Anything still unverified.
- `Residual Risk`: Adjacent behavior or environment not covered by the check.
- `Review`: Summarize findings, ruled-out concerns, and residual risk before acceptance.

## Current Code Already Correct

- `Objective`: Validate the reported behavior against the current workspace.
- `Evidence`: The reported input, relevant code path, and observed test or simulation result.
- `Mode`: `Analyze` leading to `No Patch`.
- `No Patch`: Current code already produces the expected result, or the reported failure cannot be reproduced with available evidence.
- `Ruled-out Hypotheses`: Candidate fault locations checked and rejected.
- `Verification`: Test, simulation, log inspection, or runtime check that supports the no-change conclusion.
- `Proof Gap`: Historical environment, production state, or missing input that could still explain the original report.
- `Review`: Use `change-review` shape for the accepted no-patch result.

## Unclear Request

- `Objective`: State the most likely objective, if one can be stated.
- `Evidence`: Direct user statements and any shallow source scan used for routing.
- `Mode`: `Clarify`.
- `Open Questions and Resolution Path`: Mark each as `Ask Now`, `Investigate from Source`, `Investigate Externally`, or `Assume Explicitly`.
- `Ruled-out Interpretations`: Include only when there are plausible alternate readings.
- `Proof Gap`: The fact that blocks safe planning, diagnosis, or implementation.
- `Next Step`: Ask or inspect only what is needed to open the next gate.
