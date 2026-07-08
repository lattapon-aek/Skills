# Output Patterns

Use these compact patterns when the full mode output would be too heavy for the task. Keep them evidence-first.

## Small Clear Implementation

- `Objective`: Implement the specific requested behavior.
- `Working Document`: User-supplied task document or repo-local work packet for any file-changing work; inline packet only for read-only one-turn work.
- `Evidence`: Files, tests, docs, or runtime behavior inspected before editing.
- `Mode`: `Implement`.
- `Change`: The narrow patch point and why it is sufficient.
- `Verification`: Commands or runtime checks run and observed.
- `Verification Hazards`: Whether the green/red result exercised the shipping layer, surface, cause, artifact, and baseline; name any open hazard.
- `Proof Gap`: Anything still unverified.
- `Residual Risk`: Adjacent behavior or environment not covered by the check.
- `Review`: Summarize findings, ruled-out concerns, and residual risk before acceptance.

## Current Code Already Correct

- `Objective`: Validate the reported behavior against the current workspace.
- `Working Document`: User-supplied task document or repo-local work packet for any file-changing work; inline packet only when no file artifact is needed.
- `Evidence`: The reported input, relevant code path, and observed test or simulation result.
- `Mode`: `Analyze` leading to `No Patch`.
- `No Patch`: Current code already produces the expected result, or the reported failure cannot be reproduced with available evidence.
- `Ruled-out Hypotheses`: Candidate fault locations checked and rejected.
- `Verification`: Test, simulation, log inspection, or runtime check that supports the no-change conclusion.
- `Verification Hazards`: Whether the observed no-change result could be a subset, wrong-layer, wrong-theory, wrong-artifact, or baseline issue.
- `Proof Gap`: Historical environment, production state, or missing input that could still explain the original report.
- `Review`: Use `change-review` shape for the accepted no-patch result.

## Approval Or Ship Gate

Use this when the user asks whether to approve, ship, merge, accept, close, open market, or run in production based on passing tests, staging, partial rollout, green dashboards, or an agent report. This is a `verification-hazards` primary output, not a `change-review` primary output.

- `Claim Under Test`: The exact approval claim and which green result or report is being treated as proof.
- `Working Document`: The PR, packet, release note, runbook, or work packet that defines the approval context; if missing, state that the document gate is still open.
- `Hazard Scan`: One line each for `Bypassed-Layer Green`, `Subset Green`, `Wrong-Theory Green`, `Wrong-Tree Green`, and `Not-Your-Red`; mark each `clear`, `at risk`, or `not applicable`.
- `Counter-Checks Run`: Evidence actually inspected. Separate `Observed Evidence` from `Inference`. If no command or source was inspected, say `none`.
- `Verification Verdict`: `confirmed` only when layer, surface, cause, artifact, and baseline are all established; otherwise `still a lead`.
- `Proof Gap`: What must be checked before approval, shipment, merge, acceptance, closure, market-open, or production run.
- `Residual Risk`: What could still differ between the green observation and the real shipping behavior.
- `Next Gate`: `software-engineering-core Analyze`, `software-engineering-core Plan`, `software-engineering-core Implement`, or `change-review`.

Do not start this pattern with `Findings`. A later review summary may use `Findings` only after the hazard verdict exists.

## Unclear Request

- `Objective`: State the most likely objective, if one can be stated.
- `Working Document`: Existing task source, newly created packet, missing document that must be provided, or inline packet for the clarification step.
- `Evidence`: Direct user statements and any shallow source scan used for routing.
- `Mode`: `Clarify`.
- `Open Questions and Resolution Path`: Mark each as `Ask Now`, `Investigate from Source`, `Investigate Externally`, or `Assume Explicitly`.
- `Ruled-out Interpretations`: Include only when there are plausible alternate readings.
- `Proof Gap`: The fact that blocks safe planning, diagnosis, or implementation.
- `Next Step`: Ask or inspect only what is needed to open the next gate.

## Skill Handoff

- `Current Owner`: `software-engineering-core`, `verification-hazards`, or `change-review`.
- `Working Document`: The artifact the next skill must read before acting.
- `Reason For Handoff`: The gate that is now met or blocked.
- `Evidence Packet`: Commands, diffs, files, logs, reports, and observed outputs the next skill needs.
- `Open Proof Gap`: What the next skill must confirm or reject.
- `Expected Return`: `confirmed`, `still a lead`, `findings`, `no findings`, or a specific core mode to resume.
