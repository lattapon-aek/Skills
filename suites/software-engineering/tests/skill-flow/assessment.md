# Software Engineering Skill Flow Assessment

Manual harness and observed results for the current software-engineering skill suite.

## Harness

1. Inspect the skill docs in `suites/software-engineering/skills/`.
2. Run the `software-engineering-core/flows` fixture as the end-to-end clarify/analyze/implement/verify/review scenario.
3. Run the `verification-hazards` cases when the flow relies on green/red output or an agent report as proof.
4. Run the focused fixtures for `software-engineering-core` and `change-review`.
5. Use sub-agents for bounded reports when available so core modes, hazard scans, and review behavior are evaluated independently.
6. Validate the local code paths with Node tests or small simulations when the fixture supports it.

## Observed Results

### gpt-5.4-mini Forward Test

- End-to-end payment task: pass with caveat. The agent found a justified `no patch`, ran the fixture test, surfaced the mapper-shard vs full-dashboard proof gap, and included a `verification-hazards` scan. It still used some artifact claims (`git show` / `git diff`) without enough command-output detail, so `verification-hazards` now requires command and observed output summaries for command-based counter-checks.
- Direct "amended/tests pass, merge?" task: initial partial pass, rerun pass after tightening. The first run correctly refused to merge and identified wrong-tree/subset risk, but answered in review shape instead of the required `verification-hazards` output shape. After the hazards skill and orchestration policy made hazard output primary for merge/ship/close questions, the rerun started with `Claim Under Test`, used `Hazard Scan`, returned `still a lead`, and kept the review-shaped bottom line secondary.
- Change-review scenario 3: partial pass. The agent produced a useful review and proof-sufficiency residual risk, but it promoted external OpenAI API behavior as observed evidence without proving the external source was inspected. `change-review` now requires external behavior to be sourced in-turn or demoted to open question/residual risk.

### gpt-5.4-mini Internet-Derived Blind Test

Blind-run setup:
- Four independent sub-agents used `gpt-5.4-mini` with medium reasoning.
- Agents were told to read only `suites/software-engineering/skills/` and `suites/software-engineering/references/`.
- Agents were explicitly forbidden to inspect or cite `suites/software-engineering/tests/`.
- Cases were seeded from public incident sources: Cloudflare WAF regex CPU exhaustion, AWS S3 runbook capacity removal, Knight Capital partial deployment, and Mars Climate Orbiter unit contract mismatch.

Observed results:
- Cloudflare WAF: reasoning pass / shape fail. The agent refused global ship, identified that rule-match unit tests do not prove CPU behavior under real edge traffic, separated observed precedent from inference, and required profiling/canary/rollback proof. It still answered with `Findings` before a hazard scan.
- AWS S3 runbook: reasoning pass / shape fail. The agent refused production approval, identified staging-green vs production blast-radius risk, required exact command, dry-run, minimum-capacity guardrails, rollback, stop conditions, and dependency impact checks. It still answered with `Findings` before a hazard scan.
- Knight Capital: reasoning pass / shape fail. The agent refused open-market/ship, identified subset-green and stale-artifact risk from seven-of-eight servers, and required fleet-level artifact verification. It still used a prose verdict instead of the required `Claim Under Test` shape.
- Mars unit contract: reasoning pass / shape fail. The agent rejected acceptance based on numeric pass-through alone, separated transport proof from semantic unit proof, and required an authoritative contract plus producer/consumer unit checks. It still answered as `change-review` findings before hazards.

Action taken:
- `verification-hazards` now names approve/ship/merge/accept/close/go-no-go/production-run prompts as primary hazards outputs when they depend on green results or reports.
- `orchestration-policy` now includes a small-model routing shortcut for approval gates and requires `Claim Under Test` before `Findings`.
- `verification-hazards` now keeps the approval-gate output contract in its runtime entrypoint, with golden transcripts covering the compact shape.
- `change-review` now defers proof-gated approval questions to `verification-hazards` until a hazard verdict or concrete artifact exists.

Assessment:
- The suite successfully taught the small model the intended skeptical reasoning across unrelated public incidents.
- The main weakness was output-shape selection under approval wording. The patch addresses routing and format, not core doctrine.
- A post-patch Knight Capital rerun passed the approval-gate shape: the answer started with `Claim Under Test`, included a hazard scan, returned `still a lead`, and only then added a review-shaped summary.
- A future automated transcript harness should assert that approval-gate answers begin with `Claim Under Test` and include the six exact hazard labels.

### `software-engineering-core` Clarify

- Pass.
- The flow incident bundle already provides enough source material to define objective, scope, proof of done, and open questions.
- The correct intake behavior is to define a focused verification target, not to jump straight to a fix.

### `software-engineering-core` Analyze

- Case 1: pass.
- Case 2: pass.
- Case 3: pass.
- Case 4: fail / underspecified against the current local fixture.

Case 4 is the only mismatch:
- The incident log says `internal_status=FAILED` for a `provider_status=CAPTURED` payment.
- The current local mapper returns `SUCCEEDED` for `CAPTURED`.
- The fixture therefore does not reproduce the reported failure against the current code, so the final trace-to-fault requirement is not verifiable here.

### `software-engineering-core` Implement

- Case 1: pass.
- Case 2: pass.
- Case 3: partially supported locally, but it depends on external OpenAI documentation to finish safely.

Observed boundary:
- `client.ts` is the natural patch point first.
- `support-assistant.ts` only needs to change if the wrapper contract changes.

### `change-review`

- Scenario 1: no correctness finding if the PR summary is authoritative, but the validation evidence is weaker than ideal.
- Scenario 2: no findings.

### `verification-hazards`

- The current suite includes manual cases for bypassed-layer green, subset green, wrong-theory green, wrong-tree green, not-your-red, weak-oracle green, and a compound all-six scan.
- These cases should be used before accepting a flow result that depends on green/red verification output or a second-hand agent report.

### Claude Sonnet Automated Baseline (2026-07-16)

First run of the behavioral harness (`tests/behavioral/`) against `claude -p --model sonnet` with the suite skills linked into `~/.claude/skills/`, executed from an empty working directory outside the user profile (no project AGENTS.md or CLAUDE.md loaded). Two graded runs of all 30 cases: skills at master (baseline) and skills at the `feat/runtime-routing-and-continuity` branch (runtime Preflight/Suite Routing/Reporting in the core entrypoint).

| Metric | Baseline (master) | Runtime-routing branch |
| --- | --- | --- |
| cases passed | 7/30 | 9/30 |
| routing_accuracy | 0.111 | 0.111 |
| shape_compliance | 0.417 | 0.5 |
| false_acceptance_rate | 0.667 | 0.556 |
| conformance_integrity | 0.25 | 0.5 |
| premature_action_rate | 1.0 | 1.0 |
| unsupported_claim_rate | 0.75 | 0.75 |

Observed findings:

- Prompts that name a skill behave well: `verification-hazards` cases passed 6/8 (baseline) and 7/8 (branch) with correct `Claim Under Test` shape and `still a lead` verdicts.
- Prompts that require implicit selection almost always failed to route (1/9 both runs). The runtime Preflight addition did not move routing, which is consistent with its mechanism: SKILL.md content loads only after the skill is invoked, so selection depends on the frontmatter description, harness-level policy (AGENTS.md), or explicit user wording — not on entrypoint text.
- Where the skill was invoked, the branch content improved acceptance discipline (false acceptance 0.667 -> 0.556; conformance 0.25 -> 0.5). Case-level flips: gt-10, vh-04, vh-06 fail -> pass; vh-07 pass -> fail.
- Premature action failed all four tagged cases in both runs: without routing, the agent accepted user-proposed fixes (for example "จะได้แก้ retry ให้ตรงจุด" for the timeout case) instead of demanding evidence.

Caveats: single run per condition on one model; 1–2 case flips are within run-to-run variance, so treat the aggregate direction, not individual flips, as the signal. Four baseline transcripts initially captured a session-limit error message instead of an answer and were re-run after the limit reset; a first baseline attempt executed under the user's home directory leaked machine-local CLAUDE.md context into answers and was discarded.

Next action: routing is the binding constraint. Improve the three frontmatter descriptions (trigger phrasing) and re-run before considering any skill split; keep using this harness for before/after comparisons.

## Commands Used

- `node --test suites/software-engineering/tests/software-engineering-core/flows/sample-app/src/payments/retry-status-mapper.test.ts`
- `node --test suites/software-engineering/tests/software-engineering-core/analysis/sample-app/src/payments/status-mapper.test.ts`
- `node --input-type=module` simulations for the login, orders, and invoice fixtures
- manual inspection of `suites/software-engineering/tests/verification-hazards/cases.md`
- `sed -n ...` and `nl -ba ...` on the relevant skill docs and fixture files

## Earlier Residual Risk

The earlier assessment was partially manual and lacked a dedicated full agent-driving harness. The current-policy run below addresses transcript capture for the 32-case behavioral matrix; multi-phase repository execution remains a separate surface.

## Current-Policy 32-Case Run (2026-07-17)

Runtime: Codex CLI `0.144.5`, `gpt-5.6-sol`, low reasoning, ephemeral sessions, read-only isolated workspaces, current globally linked skills, and the emitted canonical `AGENTS.md` policy. Both runs graded all 32 current cases with zero missing transcripts. The first run captured final transcripts; the second also captured Codex JSONL events and stderr after the event-aware oracle was added.

| Metric | Before readiness changes | After readiness changes |
| --- | ---: | ---: |
| cases passed | 14/32 | 14/32 |
| routing_accuracy | 0.2 | 0.3 |
| shape_compliance | 0.615 | 0.538 |
| false_acceptance_rate | 0.368 | 0.421 |
| conformance_integrity | 0.75 | 0.75 |
| premature_action_rate | 1.0 | 0.6 |
| unsupported_claim_rate | 0.667 | 0.5 |
| scope_expansion_rate | 1.0 | 1.0 |
| resume_accuracy | 0.0 | 0.0 |
| requirement_coverage | 0.0 | 0.0 |

Case flips were balanced: `gt-09`, `ms-01`, and `gt-11` changed fail to pass; `ms-08`, `ms-12`, and `vh-03` changed pass to fail. The overall score did not change. One run per condition cannot distinguish small doctrine effects from model variance, so metric direction is recorded as evidence rather than causal proof.

The five cases tagged `premature_action_rate` and configured with `forbid_file_change` had no observed `file_change` event and no rejected-patch stderr. Their remaining failures were transcript-contract failures. `gt-07`, a small implementation task where action is expected after preflight, did attempt a patch and the read-only sandbox rejected it; it is intentionally not a forbidden-file-change case.

The run closes the earlier “no 32-case current-policy matrix” gap and establishes that event capture works on the target Codex runtime. It does not establish cross-model behavior, interpret arbitrary shell commands as read-only or mutating, or prove that one sample is stable. A future repeated matrix should add per-case timeouts; `gt-07` took roughly 2.5 minutes while most cases completed in 25–50 seconds.
