# Final Report: Behavioral Evaluation Reliability

## Objective

Make behavioral results diagnostically trustworthy by separating decision, shape, evidence, and tool outcomes; bounding agent runtime; observing isolated workspace mutations; and retaining repeated matched runs.

## Intended And Observed State

| Area | Intended State | Observed State | Status |
| --- | --- | --- | --- |
| Dimension grading | independent decision, shape, evidence, and tool results without weakening strict status | check failures carry dimensions; reports include per-case and aggregate dimension results; overall pass remains strict | conforms |
| Runtime bound | one timeout per case with descendant cleanup and retained evidence | default 180 seconds; timeout and error statuses are distinct; POSIX process-group test proves the child is gone | conforms |
| Mutation oracle | exact added, modified, and deleted paths from fresh isolated copies | SHA-256 tree snapshots emit filesystem sidecars and feed `forbid_file_change` | conforms |
| Repeated runs | separate artifacts and stability classification | `--repeat` emits run folders, per-run results, pass frequency, and stable/flaky classes | conforms |

## Files Touched

- Runner: `suites/software-engineering/scripts/run-behavioral-eval.py`
- Case schema: `suites/software-engineering/tests/behavioral/cases.json`
- Deterministic coverage: `suites/software-engineering/tests/behavioral/test_behavioral_eval.py`
- Validation wiring: `scripts/validate-suite.sh`
- Usage and limitations: both suite and behavioral READMEs
- Continuity: work packet and this report

## Verification

- `python3 -m py_compile ...`: runner and test module compile.
- Behavioral self-test: 32 cases valid and 14 good/bad fixtures graded.
- Deterministic tests: 6/6 pass, covering dimension independence, filesystem diffing, descendant termination, distinct command errors, event-free mutation, and repeat stability.
- `./scripts/validate-suite.sh`: passes three skill validations, architecture/policy/link checks, behavioral checks, and 14/14 Node fixtures.
- `git diff --check`: passes.
- Bounded live Codex forward test: 2 cases x 2 repeats, zero timeouts, zero command errors, and four empty filesystem deltas.

## Forward Evidence

The live run retained an unfavorable result rather than normalizing it away:

- `gt-11-mechanism-before-architecture`: `stable_pass`; decision, evidence, and tool passed in both runs.
- `gt-03-core-stops-at-clarify`: `stable_fail`; decision and tool passed in both runs while shape failed in both runs.

This is a useful discriminating outcome. The former binary report would only show a failure; schema v2 identifies a stable output-contract problem without mislabeling the routing decision or mutation behavior.

## Acceptance Coverage

| Commitment | Observed Result | Status |
| --- | --- | --- |
| Keep strict overall pass/fail | any applicable dimension failure still fails the case | conforms |
| Add four diagnostic dimensions | case failures and summaries distinguish all four | conforms |
| Terminate timeout descendants | POSIX child sleeper is absent or zombie after timeout | conforms |
| Detect non-event mutations | shell-created file fails the tool dimension | conforms |
| Isolate writable evaluation | every live case/repeat used a new template copy | conforms |
| Preserve repeated artifacts | two run folders and all sidecars retained | conforms |
| Keep failures visible | stable shape failure remains in report and exit status 1 | conforms |
| Avoid routing or public-skill changes | no skill entrypoint or routing doctrine changed | conforms |

## Verification Hazards

- `Bypassed-Layer Green`: clear for runner behavior; deterministic tests invoke the actual runner functions and CLI, while the bounded probe drives the actual Codex CLI.
- `Subset Green`: at risk only for broad provider and platform generalization; live coverage is Codex on macOS, not every agent or Windows.
- `Wrong-Theory Green`: clear; actual process groups, filesystem bytes, JSONL events, and repeated CLI behavior were observed.
- `Wrong-Tree Green`: clear; validation and review target the current working tree, not `HEAD`.
- `Not-Your-Red`: clear; the stable Clarify red is attributed to missing shape fields in retained transcripts, not to runner failure.
- `Weak-Oracle Green`: clear for the four scoped mechanisms because negative controls fail. Still at risk for universal semantic agent quality because regex checks remain wording-sensitive.

Verification Verdict: `confirmed` for the four scoped reliability mechanisms; `still a lead` for Windows cleanup, arbitrary provider schemas, and cross-model behavioral quality.

## Change Review

- Findings: no blocking finding in the scoped working-tree change.
- Instruction Compliance: required order followed; no routing change, skill split, commit, push, or full cross-model matrix was added.
- Intent Conformance: `conforms`; each approved improvement maps to implementation and observed evidence.
- Mechanism Validity: established through local source inspection, deterministic counter-controls, and a bounded live CLI run.
- Deviations: none.
- Proof Gap: Windows `taskkill` behavior is not locally exercised; final snapshots cannot detect a write restored to identical bytes unless the event schema exposes it.
- Residual Risk: shell template quoting remains the caller's responsibility; very large workspace templates make byte snapshots expensive.
- Verdict: `accept`.
