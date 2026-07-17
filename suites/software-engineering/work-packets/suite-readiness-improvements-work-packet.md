# Work Packet: Suite Readiness Improvements

## Objective

Close the four readiness gaps identified in the 2026-07-17 suite review: current-policy behavioral evidence, portable Markdown links, tool-event-aware mutation checks, and entrypoint budget headroom.

## User Instructions

- Apply the improvements in the reviewed order.
- Preserve the three-skill ownership model and evidence-first doctrine.

## Authority Mode

`execute-within-scope`

## Required Sequence

1. Run the current 32-case agent matrix with the canonical `AGENTS.md` policy.
2. Repair the 11 machine-specific Markdown links and add link validation.
3. Add a tool-event oracle for premature mutation.
4. Reduce entrypoint budget pressure without weakening doctrine.
5. Re-run targeted checks, full validation, and the 32-case matrix.
6. Challenge the proof and complete a change-review acceptance pass.

## Source Documents

- `AGENTS.md`
- `suites/software-engineering/README.md`
- `suites/software-engineering/references/agents-enforcement-policy.md`
- `suites/software-engineering/tests/behavioral/README.md`
- `suites/software-engineering/tests/behavioral/cases.json`
- `suites/software-engineering/tests/mechanism-before-design/evaluation.md`
- the three public `SKILL.md` entrypoints

## Current Assumptions

- Codex CLI `0.144.5` and the globally linked current suite are the target runtime for the local matrix.
- The canonical policy must be present in the isolated workspace before the agent starts.
- Transcript-only assertions cannot prove absence of mutation; Codex JSONL tool events can provide a discriminating observation.

## Scope

- Behavioral evaluation runner, cases, fixtures, and documentation.
- Suite-wide local Markdown link validation.
- Portable links in the OpenAI full-flow fixture documentation.
- Concise entrypoint edits that preserve required contracts.
- Auditable baseline and final evidence.

## Out of Scope

- Public skill splits or renames.
- Changes to suite ownership or routing semantics.
- Claims of universal behavior across untested models or harness versions.
- Commit, push, or PR creation.

## Decisions

- Keep live agent evaluation separate from deterministic suite validation because it is slower and runtime-dependent.
- Store final aggregate evidence in the existing assessment/report structure; do not commit raw transient sessions unless they are needed to explain a failure.
- Treat any write-capable tool event in a no-mutation case as failure even if the final transcript claims no edit occurred.

## Intended State

- All repository-local Markdown links resolve from a clean checkout.
- The deterministic validator catches future broken local links.
- Behavioral cases can assert forbidden tool activity from captured JSONL events.
- Current-policy before/after matrices are recorded with exact runtime and recurrence boundaries.
- Every entrypoint has practical word-budget headroom while retaining its required contracts.

## Plan Commitments

- Do not weaken behavioral regex checks to improve scores.
- Do not count sandbox denial as proof that an agent voluntarily respected a mutation gate.
- Keep current public names and routing contracts unchanged.
- Preserve raw observed failures in the report.

## Observable Conformance Criteria

- `./scripts/validate-suite.sh` passes.
- A suite-wide Markdown checker reports zero broken local links.
- Self-test includes a good/bad event-oracle fixture pair.
- The live matrix produces 32 non-missing results before and after the change.
- Word counts remain within limits with more than zero headroom per entrypoint.

## Allowed Variations

- Transcript storage location and report formatting may vary when aggregate results and exact commands remain reproducible.

## Forbidden Substitutions

- Grep-only validation in place of live agent evaluation.
- Final-message claims in place of observed tool events.
- Removing doctrine solely to pass the word budget.

## Plan Amendment Authority

Implementation may amend non-material harness details when observed Codex JSONL shape requires it; any routing, doctrine, or public-contract change returns to Plan.

## Mechanism Evidence

| Claim | Decision Dependency | Source | Observed or Inferred | Falsifying Check | Status |
| --- | --- | --- | --- | --- | --- |
| Codex can run from an isolated workspace | baseline isolation | `codex exec --help` exposes `-C/--cd` and `--skip-git-repo-check` | observed | pilot run starts elsewhere | established |
| Existing runner executes one shell command per case | matrix execution | inspected `run_agent()` | observed | pilot output absent | established |
| Transcript grading cannot observe tool use | event oracle | inspected `grade()` and documented harness limit | observed | tool event changes grade | established |

Mechanism Verdict: established

## Plan

Follow the Required Sequence without combining unrelated cleanup.

## Proof Strategy

- Capture current and final 32-case reports from the same isolated policy workspace and runtime.
- Add deterministic event-oracle fixtures before relying on event grading.
- Run link validation against every suite Markdown file.
- Run quick validation, architecture checks, behavioral self-test, all Node fixtures, and full suite validation.
- Inspect the final diff and challenge Layer, Surface, Cause, Artifact, Baseline, Outcome, and Conformance.

## Acceptance Matrix

| Commitment | Type | Source | Expected State | Observed State | Status | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Current 32-case baseline | sequence | user/review | recorded before functional edits | 14/32, zero missing | complete | baseline report |
| Portable Markdown links | functionality | review | zero broken local links | 29 links resolve | complete | checker plus negative control |
| Tool-event oracle | proof | review | mutation event can fail a case | event and denied-patch controls reject | complete | 14-fixture self-test and live sidecars |
| Budget headroom | maintainability | review | each entrypoint below limit | 3,538 total; at least 50 each | complete | architecture check |
| Final verification | acceptance | suite doctrine | targeted, full, live matrix, hazards, review | full validation and 32-case after run complete | complete | final report |

## Deviations

None observed.

## Open Questions

- None blocking. Per-case timeout and broader shell-mutation classification remain follow-up risks.

## Resume Instructions

Read this packet and the final report, inspect `git status`, then resume only for review findings or explicitly authorized follow-up work.
