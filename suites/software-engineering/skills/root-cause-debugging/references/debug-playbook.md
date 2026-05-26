# Debug Playbook

## Reproduction

- Gather the closest incident evidence first: logs, traces, requests, responses, payloads, timestamps, metrics, and failing inputs
- Exact command or user flow
- Expected behavior
- Actual behavior
- Logs, stack traces, screenshots, or failing assertions
- Prefer a path you can run or simulate yourself instead of relying only on second-hand reports
- Use simulation to explain, narrow, or confirm the incident evidence, not to skip it when it exists

## Isolation

- Start from the point where the failure was observed, then walk outward
- Find the layer where behavior diverges
- Reduce the problem to a small failing case
- Check recent changes, config, and environment assumptions
- Reject hypotheses that are not supported by evidence
- Trace to the exact fault location, not just the visible symptom
- Build a simulation path when a full repro is too heavy but the failure mode can still be recreated in a smaller controlled case
- If logs or traces are missing, state which capture would most improve diagnosis

## Fix

- Only move into a code fix if the task includes fixing and the cause is already proven
- Change the narrowest code path that can explain the failure
- Avoid bundling refactors with the fix
- Add regression coverage when practical
- If the fix is larger than expected, state what evidence forced the scope to grow

## Verification

- Re-run the failing case
- Run focused adjacent checks
- Re-check the same logs, traces, metrics, or runtime signals that first revealed the issue
- Note what was not verified
- Do not call the bug fixed until the original failure is observed to disappear
- If you never observed the failure directly, state that confidence is lower and explain the substitute evidence used
