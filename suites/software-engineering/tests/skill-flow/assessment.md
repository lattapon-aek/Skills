# Software Engineering Skill Flow Assessment

Manual harness and observed results for the current software-engineering skill suite.

## Harness

1. Inspect the skill docs in `suites/software-engineering/skills/`.
2. Run the `software-engineering-core/flows` fixture as the end-to-end clarify/analyze/implement/review scenario.
3. Run the focused fixtures for `software-engineering-core` and `change-review`.
4. Use sub-agents for bounded reports when available so core modes and review behavior are evaluated independently.
5. Validate the local code paths with Node tests or small simulations when the fixture supports it.

## Observed Results

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

## Commands Used

- `node --test suites/software-engineering/tests/software-engineering-core/flows/sample-app/src/payments/retry-status-mapper.test.ts`
- `node --test suites/software-engineering/tests/software-engineering-core/analysis/sample-app/src/payments/status-mapper.test.ts`
- `node --input-type=module` simulations for the login, orders, and invoice fixtures
- `sed -n ...` and `nl -ba ...` on the relevant skill docs and fixture files

## Residual Risk

- There is still no dedicated automated harness that drives an agent through all four phases and captures a transcript.
- The current assessment is therefore evidence-based, but partially manual.
