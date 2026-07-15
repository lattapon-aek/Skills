# Progress Log: Deep Causal Debugging

## Current State

- Added a progressive-disclosure causal debugging protocol.
- Connected the protocol to core Analyze, the root-cause transition gate, bug-fix Implement verification, and the execution checklist.
- Added adversarial analysis and mini-stress cases.
- Registered the protocol and cases in suite validation.

## Decisions And Evidence

- Keep debugging inside `software-engineering-core` Analyze to preserve the suite's single-owner routing model.
- Require discriminating checks because collecting more evidence consistent with every hypothesis does not reduce causal ambiguity.
- Treat a green patch as non-causal evidence until the original reproduction and outcome oracle are replayed.
- Permit explicitly authorized mitigation before full diagnosis, but prohibit presenting it as a root-cause fix.
- Keep `SKILL.md` at 500 lines and the detailed protocol at 97 lines to respect progressive disclosure guidance.

## Verification Observed

- `git diff --check`: passed after the protocol and test edits.
- `./scripts/validate-suite.sh`: passed.
- Skill validation: 3/3 valid.
- Executable fixture tests: 14/14 passed.
- First forward scenario: Agent rejected a Redis-timeout patch, returned `still a lead`, classified it as mitigation, and requested evidence distinguishing server latency, pool wait, network delay, and application deadline.

## Open Proof Gaps

- Second fresh-context forward scenario passed: the Agent returned `still a lead`, preserved six live causal hypotheses, separated observed and inferred causal links, classified the timeout change as mitigation, and proposed a trace-based discriminating check before patching.
- Behavioral generalization across different issue classes and model sizes is not fully proven by repository fixtures.
- The Markdown cases specify expected behavior but are not executed by an automated model-evaluation harness.

## Deviations

- The first forward-test prompt described the task as a behavioral evaluation. It did not reveal the expected diagnosis, but this could prime caution. Acceptance therefore relies on the second fresh-context run without evaluation framing.

## Next Action

Apply verification-hazards to the evidence, run final validation, and emit a change-review-shaped final report.
