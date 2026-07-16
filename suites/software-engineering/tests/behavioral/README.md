# Behavioral Evaluation Harness

Machine-gradable behavioral cases for the suite. Each case in `cases.json` pairs a prompt from `golden-transcripts/`, `mini-stress/`, or `verification-hazards/` with deterministic transcript assertions and metric tags, so suite changes can be measured instead of eyeballed.

## Grade Existing Transcripts

Save each agent answer as `<case-id>.md` (or `.txt`) in one directory, then:

```bash
python suites/software-engineering/scripts/run-behavioral-eval.py --transcripts <dir> --report report.json
```

Missing transcripts are reported but only fail the run with `--require-all`. Exit code 1 means at least one graded case failed.

## Drive An Agent Directly

`--agent-cmd` runs a shell command per case; `{prompt_file}` is replaced with a UTF-8 file containing the prompt, and stdout becomes the transcript:

```bash
# Claude Code
python suites/software-engineering/scripts/run-behavioral-eval.py \
  --agent-cmd 'claude -p "$(cat {prompt_file})"' --out transcripts/

# Codex CLI
python suites/software-engineering/scripts/run-behavioral-eval.py \
  --agent-cmd 'codex exec "$(cat {prompt_file})"' --out transcripts/
```

Use `--case-id <id>` (repeatable) to run a subset. On Thai-locale Windows run with `PYTHONUTF8=1`.

The agent under test must have the suite skills installed; the prompts assume the skills are selectable. Grade the same transcript set before and after a doctrine change to compare metrics.

## Check Semantics

- `must_start_with` — plain prefix of the first non-empty content line (markdown markers stripped)
- `must_include` / `must_include_any` / `must_not_include` — Python regexes, case-sensitive unless `(?i)`
- `ordered` — regexes whose first matches must appear in strictly increasing positions

Assertions target the suite's output contracts (exact hazard labels, `Claim Under Test` first, `still a lead`, field names), not wording style. Keep negatives conservative: a `must_not_include` that can match a correct answer is worse than no check.

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
```

Validates `cases.json` (required fields, unique ids, compilable regexes) and grades the `fixtures/` transcripts: every `<case-id>.good.md` must pass and every `<case-id>.bad.md` must fail. This is the grader's own discriminating oracle and runs inside `./scripts/validate-suite.sh`. When adding or tightening a case, add or update a fixture pair for it.

## Limits

Deterministic assertions grade output shape and stated decisions, not tool activity. A transcript that *claims* to stop at Clarify while the live agent actually edited files would still pass `gt-03`; catching that requires grading real tool-use transcripts or an LLM judge, both out of scope for this phase. Treat metric shifts as signals for manual review, not as proof by themselves.
