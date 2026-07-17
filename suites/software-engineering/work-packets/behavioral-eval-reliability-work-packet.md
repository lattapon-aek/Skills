# Work Packet: Behavioral Evaluation Reliability

## Objective

Make behavioral results diagnostically trustworthy by separating decision, shape, evidence, and tool outcomes; bounding agent runtime; observing filesystem mutations; and summarizing repeated matched runs.

## User Instructions

- Implement the first four follow-up improvements in the agreed order.
- Do not change routing doctrine or split public skills in this packet.

## Authority Mode

`execute-within-scope`

## Required Sequence

1. Freeze the v2 grading/report contract.
2. Implement dimension-aware grading without weakening strict overall pass/fail.
3. Add per-case timeout and process-tree termination.
4. Add isolated workspace snapshots and mutation grading.
5. Add repeated matched runs and stability summaries.
6. Add deterministic tests, documentation, full validation, and a bounded forward test.

## Source Documents

- `AGENTS.md`
- `suites/software-engineering/tests/behavioral/README.md`
- `suites/software-engineering/tests/behavioral/cases.json`
- `suites/software-engineering/scripts/run-behavioral-eval.py`
- `suites/software-engineering/work-packets/suite-readiness-improvements-final-report.md`

## Current Assumptions

- Strict overall case status remains useful and must not be weakened.
- Check-level dimensions are more diagnostic than inferring quality from case-level metric tags.
- An isolated pre/post byte snapshot is stronger mutation evidence than shell-command classification.
- One agent process per case is the termination boundary; descendants must not outlive a timeout.

## Scope

- Behavioral case schema and runner.
- Structured execution, dimension, filesystem, repeat, and stability reports.
- Deterministic tests and suite validation wiring.
- Usage and limitation documentation.

## Out Of Scope

- Skill routing/frontmatter changes.
- Public skill splits or ownership changes.
- Semantic LLM-as-judge grading.
- Cross-model full 32-case production runs in this packet.
- Commit, push, or PR creation.

## Decisions

- Preserve strict `pass`/`fail`; add dimension results rather than replacing the oracle.
- Allow regex entries to carry an explicit `dimension`; plain strings default to `decision` except inherently structural/tool checks.
- Run workspace-write evaluation only on copies created from a caller-supplied template and addressed through `{workspace}`.
- Record timeouts and command errors as distinct statuses; never retry silently.
- Keep raw per-run artifacts and emit aggregate stability instead of collapsing repeated runs into one answer.

## Intended State

- Reports distinguish `decision`, `shape`, `evidence`, and `tool` results.
- A timed-out case terminates its process tree, retains partial artifacts, and reports `timeout`.
- Each workspace-enabled case runs in a fresh copy and emits an exact added/modified/deleted filesystem diff.
- `forbid_file_change` rejects event attempts, denied patches, and observed filesystem changes.
- `--repeat N` creates separate run artifacts and stable-pass/stable-fail/flaky classifications.

## Plan Commitments

- Do not remove or relax an existing transcript assertion.
- Do not infer filesystem safety only from tool names.
- Do not reuse a writable workspace across cases or repeats.
- Preserve single-run and transcript-only usage.
- Preserve unfavorable run artifacts and execution failures.

## Observable Conformance Criteria

- Existing fixtures retain their expected pass/fail result.
- Dimension summaries identify applicable cases independently of strict overall status.
- A spawned descendant is gone after timeout.
- A shell-created file is detected without a `file_change` event.
- Two synthetic repeats produce a deterministic stability classification.
- Full suite validation remains green.

## Allowed Variations

- Report field naming may vary if schema version and meanings are explicit.
- Windows termination may use `taskkill`; POSIX must use a process group.

## Forbidden Substitutions

- A regex-only shell mutation classifier in place of filesystem snapshots.
- Killing only the parent shell on timeout.
- Retrying timed-out or failed cases and hiding the original result.
- Reclassifying existing failures as passes to improve aggregate scores.

## Plan Amendment Authority

Implementation may refine internal data shapes when deterministic tests expose a need. Any public CLI removal, oracle weakening, or routing change requires a return to Plan.

## Mechanism Evidence

| Claim | Decision Dependency | Source | Observation | Status |
| --- | --- | --- | --- | --- |
| Python supports isolated process sessions and timeout communication | process-tree cleanup | inspected local `subprocess.Popen` signatures | `start_new_session` and `communicate(timeout)` available | established |
| Codex exposes structured events and isolated cwd selection | event/workspace oracle | `codex exec --help` and prior live captures | `--json`, `--cd`, sandbox, ephemeral available | established |
| Current strict status conflates all failed checks | dimension split | inspected `grade()` and `summarize_metrics()` | failures are untyped strings and case status is binary | established |

Mechanism Verdict: established

## Plan

Implement the Required Sequence with deterministic unit coverage before a live bounded forward test.

## Proof Strategy

- Test pure check normalization, dimension summaries, tree snapshots, diffs, and stability aggregation.
- Launch a synthetic parent/child sleeper and verify timeout kills the descendant.
- Run a synthetic JSONL agent against a writable isolated copy and prove a shell-created file fails the tool dimension.
- Run existing self-test, Python unit tests, `validate-suite.sh`, and `git diff --check`.
- Run a two-repeat bounded live case only after deterministic proof is green.

## Acceptance Matrix

| Commitment | Expected State | Observed State | Status | Evidence |
| --- | --- | --- | --- | --- |
| Dimension-aware grading | four independent dimension summaries | strict status retained; decision, shape, evidence, and tool statuses reported independently | conforms | unit test plus 32-case schema self-test |
| Timeout cleanup | distinct timeout; no surviving descendant | synthetic parent and child terminated; case reported timeout without retry | conforms | `test_timeout_terminates_descendant_process` |
| Filesystem oracle | shell mutation detected in isolated copy | event-free shell-created file recorded and rejected; live copies remained unchanged | conforms | unit test plus four live filesystem sidecars |
| Repeated matrix | per-run artifacts and stability summary | two run folders retained; one stable pass and one dimension-specific stable fail classified | conforms | bounded Codex forward report |
| Compatibility | existing self-test and full suite pass | 32 cases/14 fixtures, 6 unit tests, and 14 Node fixtures pass | conforms | `./scripts/validate-suite.sh` |

## Deviations

None observed. The bounded live case failure was an unfavorable model output retained by the harness, not an implementation deviation.

## Open Questions

- None blocking. Windows process-tree termination remains an explicit untested-platform boundary.

## Resume Instructions

Read this packet, inspect current git state, and resume from the first open acceptance row. Never replace missing runtime evidence with a report claim.
