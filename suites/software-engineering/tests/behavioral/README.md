# Behavioral Evaluation Harness

Machine-gradable behavioral cases for the suite. Each case in `cases.json` pairs a prompt from `golden-transcripts/`, `mini-stress/`, or `verification-hazards/` with deterministic transcript assertions and metric tags, so suite changes can be measured instead of eyeballed.

## Grade Existing Transcripts

Save each agent answer as `<case-id>.md` (or `.txt`) in one directory, then:

```bash
python suites/software-engineering/scripts/run-behavioral-eval.py --transcripts <dir> --report report.json
```

Missing transcripts are reported but only fail the run with `--require-all`. Exit code 1 means at least one graded case failed.

## Drive An Agent Directly

`--agent-cmd` runs a shell command per case and captures stdout as the transcript. Without `{prompt_file}` in the template, the prompt is piped to the command's stdin — the portable form, since the template runs through the platform shell (cmd.exe on Windows, where `$(cat ...)` does not work):

```bash
# Claude Code (prompt via stdin; add "cd /d <empty-dir> &&" on Windows to control the agent cwd)
python suites/software-engineering/scripts/run-behavioral-eval.py \
  --agent-cmd 'claude -p --model sonnet' --out transcripts/

# Codex CLI on a POSIX shell (prompt via file)
python suites/software-engineering/scripts/run-behavioral-eval.py \
  --agent-cmd 'codex exec "$(cat {prompt_file})"' --out transcripts/
```

With `{prompt_file}` in the template, it is replaced by the path of a UTF-8 file containing the prompt instead. The template also supports `{case_id}`, `{run_index}`, and `{workspace}`. Use `--case-id <id>` (repeatable) to run a subset. On Thai-locale Windows run with `PYTHONUTF8=1`.

For Codex JSONL, add `--json-events` to the harness and `--json` to `codex exec`. The harness writes the final agent message as the transcript and retains `<case-id>.events.jsonl`, `<case-id>.stderr.txt`, and `<case-id>.run.json`. Cases with `forbid_file_change: true` fail on an observed `file_change` event, a read-only sandbox message showing that a patch was attempted and rejected, or a filesystem delta captured from an isolated workspace. This prevents a final answer that merely claims it did not edit from masking an earlier mutation.

Each agent process has a 180-second timeout by default. Set `--timeout-seconds N` to change it or `--timeout-seconds 0` to disable it. A timeout terminates the process tree, retains partial artifacts, and produces `timeout`; another nonzero command exit produces `error`. Neither condition is retried or collapsed into an ordinary assertion failure.

The agent under test must have the suite skills installed; the prompts assume the skills are selectable. Grade the same transcript set before and after a doctrine change to compare metrics.

## Check Semantics

- `must_start_with` — plain prefix of the first non-empty content line (markdown markers stripped)
- `must_include` / `must_include_any` / `must_not_include` — Python regexes, case-sensitive unless `(?i)`
- `ordered` — regexes whose first matches must appear in strictly increasing positions
- `forbid_file_change` — fail on a structured file-change call or rejected patch attempt

Assertions target the suite's output contracts (exact hazard labels, `Claim Under Test` first, `still a lead`, field names), not wording style. Keep negatives conservative: a `must_not_include` that can match a correct answer is worse than no check.

Regex entries may be plain strings or objects with an explicit dimension:

```json
{"pattern": "(?i)git show", "dimension": "evidence"}
```

The dimensions are `decision`, `shape`, `evidence`, and `tool`. Plain regex strings default to `decision`; `must_start_with` and `ordered` default to `shape`; `forbid_file_change` belongs to `tool`. An overall case still passes only when every applicable check passes. Dimension summaries are diagnostic and do not weaken that strict oracle.

## Isolated Workspace Oracle

Use a caller-owned template when a case may run with workspace-write access:

```bash
python suites/software-engineering/scripts/run-behavioral-eval.py \
  --agent-cmd 'codex exec --json -s workspace-write -C {workspace} -' \
  --json-events \
  --workspace-template eval-template/ \
  --out transcripts/
```

The harness copies the template for every case and repeat, snapshots it before and after the command, writes `<case-id>.filesystem.json`, then removes the copy. Use `--keep-workspaces` to retain copies or `--workspace-root` to place them outside the output directory. The harness never grants write access to the source template.

## Repeated Matched Runs

Use `--repeat N` with `--agent-cmd` to retain independent `run-01/`, `run-02/`, and later artifacts:

```bash
python suites/software-engineering/scripts/run-behavioral-eval.py \
  --agent-cmd 'agent-command' --repeat 3 --out transcripts/ --report report.json
```

Report schema v2 keeps each run's cases, metrics, and dimensions. It adds per-case `stable_pass`, `stable_fail`, `stable_timeout`, `stable_error`, or `flaky` classification plus mean/min/max aggregates. A single-run report retains the former top-level `cases` and `metrics` fields for consumers that do not yet read `runs`.

## Metrics

Cases are tagged; a metric aggregates the pass/fail of its tagged cases.

| Metric | Meaning (value) |
| --- | --- |
| `routing_accuracy` | correct skill/mode selection (pass share) |
| `shape_compliance` | required output contract shape (pass share) |
| `premature_action_rate` | patched or acted before evidence (failure share) |
| `false_acceptance_rate` | accepted or confirmed despite an open gate (failure share) |
| `unsupported_claim_rate` | presented unverified claims as evidence (failure share) |
| `scope_expansion_rate` | expanded the change boundary without justification (failure share) |
| `resume_accuracy` | rehydrated from artifacts before continuing (pass share) |
| `requirement_coverage` | explicit instructions tracked to coverage (pass share) |
| `conformance_integrity` | separated working from intended state (pass share) |

Metrics ending in `_rate` report failure share (lower is better); the rest report pass share (higher is better).

## Self-Test

```bash
python suites/software-engineering/scripts/run-behavioral-eval.py --self-test
python suites/software-engineering/tests/behavioral/test_behavioral_eval.py
```

The self-test validates `cases.json` (required fields, unique ids, known dimensions, compilable regexes) and grades the `fixtures/` transcripts plus any matching event/stderr sidecars: every `<case-id>.good.md` must pass and every `<case-id>.bad.md` must fail. The deterministic unit tests cover dimension independence, snapshots, descendant cleanup, an event-free shell mutation, and repeat stability. Both run inside `./scripts/validate-suite.sh`. When adding or tightening a case, add or update a fixture pair for it.

## Limits

Deterministic assertions grade output shape, stated decisions, explicit file-change events retained by `--json-events`, and final filesystem state in harness-owned workspaces. A process can still mutate a file and restore its original bytes before the final snapshot without a recognized event, and arbitrary provider event schemas are not interpreted. POSIX process-group cleanup is tested locally; the Windows `taskkill` branch requires Windows evidence. Treat metric shifts as signals for manual review, not as proof by themselves.
