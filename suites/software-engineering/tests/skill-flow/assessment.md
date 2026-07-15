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

## Commands Used

- `node --test suites/software-engineering/tests/software-engineering-core/flows/sample-app/src/payments/retry-status-mapper.test.ts`
- `node --test suites/software-engineering/tests/software-engineering-core/analysis/sample-app/src/payments/status-mapper.test.ts`
- `node --input-type=module` simulations for the login, orders, and invoice fixtures
- manual inspection of `suites/software-engineering/tests/verification-hazards/cases.md`
- `sed -n ...` and `nl -ba ...` on the relevant skill docs and fixture files

## Residual Risk

- There is still no dedicated automated harness that drives an agent through all four phases and captures a transcript.
- The current assessment is therefore evidence-based, but partially manual.
