# Final Report: Skill Runtime Context Refactor

## Objective

Reduce activated skill context while preserving the full evidence, causal-debugging, proof-challenge, intent-conformance, and acceptance workflow.

## What Changed

- Kept the three public skills and their ownership boundaries.
- Reduced the combined entrypoints from 8,689 to 3,421 words.
- Converted core into a runtime router with direct Clarify, Plan, Analyze, and Implement protocols.
- Consolidated duplicated debugging guidance into `causal-debugging-protocol.md`.
- Removed duplicated `analysis-playbook.md` and `output-patterns.md` runtime references.
- Added a blocking intent-to-outcome conformance gate across planning, implementation, proof, and review.
- Made continuity artifact choice independent from execution rigor.
- Added deterministic entrypoint budgets, direct-reference integrity checks, stale-link checks, and conformance fixtures.
- Updated suite documentation, templates, and skill UI metadata.

## Files Touched

- Three skill entrypoints and UI metadata
- Core mode references and artifact templates
- Hazard catalog and review template
- Shared doctrine, continuity, and orchestration references
- Suite README, validation script, architecture validator, fixtures, and work-packet artifacts

Pre-existing dirty-tree changes outside this refactor were preserved; no reset, checkout, revert, or destructive command was used.

## Decisions

- Keep one core skill with internal modes instead of creating more public skills.
- Keep all applicable gates mandatory regardless of task size.
- Treat continuity only as artifact durability and resume safety.
- Keep six verification hazards and include plan-divergent green under `Weak-Oracle Green` plus the Conformance sufficiency gate.
- Default `Allowed Variations` to `none` and prohibit agent-self-authorized material deviations.

## Verification

- `python3 suites/software-engineering/scripts/check-skill-architecture.py`
  - observed: `skill architecture check passed: 3421 entrypoint words`
- `./scripts/validate-suite.sh`
  - observed: all three skills valid
  - observed: architecture check passed
  - observed: 14 Node tests passed, 0 failed
  - observed: structure, registration, and stale routing scans passed
  - observed: `suite validation passed`
- `git diff --check`
  - observed: no output, exit 0
- Runtime discoverability
  - observed: all three skill directories in `/Users/lattapon/.codex/skills` and `/Users/lattapon/.agents/skills` are readable symlinks to this suite

## Blind Forward Tests

- Queue plan divergence: returned `still a lead`, marked conformance open, and refused closure despite functional green.
- Response-schema divergence: marked the HTTP-status-only test a weak oracle and returned to Implement.
- Redis timeout correlation: kept root cause unproven, classified the timeout increase as mitigation, and returned to Analyze.
- Reference selection: the causal run loaded the causal protocol; conformance runs did not load unrelated Plan or Implement protocols.

## Observed Evidence

- Entrypoint sizes are core 1,374 words, hazards 1,018 words, and review 1,029 words.
- Direct links resolve and the validator rejects nested chains and stale deleted references.
- Runtime doctrine contains no size-based permission to skip analysis, proof, conformance, or review.
- Conformance cases exist in golden transcripts, mini-stress cases, and verification-hazards cases.

## Intended State

- Three public roles remain stable.
- Runtime entrypoints are materially smaller.
- Mode details load through direct references.
- Bugs still require causal proof and original-failure replay.
- Functional green cannot override an unapproved plan or contract deviation.
- Every concrete accepted end state still passes proof challenge when applicable and final review.

## Observed State

The current working tree matches the intended architecture and behavior within the validated and blind-tested surface.

## Intent Conformance

`conforms`

No material implementation delta from the approved plan remains open. The validation-heading mismatch was a corrected execution deviation, not a change to intended behavior.

## Acceptance Coverage

| Commitment | Type | Source | Expected State | Observed State | Status | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Three public skills | architecture | user | Core, hazards, review | Same three entrypoints and ownership | satisfied | source inspection and blind routing |
| Lower context cost | performance | approved plan | Combined entrypoints below 4,200 words | 3,421 words | satisfied | architecture validator |
| Full applicable workflow | behavior | user | No size-based gate bypass | Explicitly enforced across runtime doctrine | satisfied | source scan and validator |
| Deep causal debugging | behavior | user | No patch before proven cause | Causal protocol and blind Redis run preserve gate | satisfied | blind forward test |
| Intent conformance | behavior | user | Working-but-divergent result blocks closure | Queue/schema cases returned still-a-lead | satisfied | blind forward tests |
| Progressive disclosure | architecture | approved plan | Mode-specific direct references | Four direct mode protocols and selective read evidence | satisfied | architecture validator and blind paths |
| Validation and readiness | proof | repository instructions | Source valid and runtime resolvable | Full suite green and both skill homes resolve | satisfied | observed commands |

## Deviations

- The first full validation after refactoring stopped at a stale assertion that still expected the old `Preflight Skill Selection` heading. The assertion was updated to the new `Preflight` contract and the full suite rerun passed.
- No material product or plan deviation remains.

## Verification-Hazards Verdict

- `Bypassed-Layer Green` — clear for explicit skill execution: blind agents read and applied the current runtime files; implicit-description selection remains outside this test.
- `Subset Green` — bounded: static validation, all local fixtures, and three blind cases passed; not every model or engineering domain was exercised.
- `Wrong-Theory Green` — clear: context reduction is measured directly and the intended behavioral failures were tested independently.
- `Wrong-Tree Green` — clear for the named acceptance target: validation ran against the current working tree; no commit claim is made.
- `Not-Your-Red` — not applicable: the final suite has no red result.
- `Weak-Oracle Green` — clear within tested cases: blind runs challenged functional-only success and produced the required conformance behavior.
- `Verification Verdict` — `confirmed` for the current working tree and tested surface.

## Change Review

- `Findings`: none blocking.
- `Instruction Compliance`: satisfied; the approved sequence and exclusions were followed.
- `Intent Conformance`: conforms.
- `Proof Gap`: implicit invocation accuracy and broader cross-model generalization are not automated.
- `Residual Risk`: external consumers that deep-link the two removed internal references must update; the repository contains no remaining runtime link to them.
- `Verdict`: accept current working-tree result.

## Remaining Risks

- Blind evaluation used explicit paths rather than testing implicit description-based selection from a completely unmanaged prompt.
- The transcript harness remains manual; agent-reported read paths are not machine-captured traces.
- Entry-point word count is a deterministic context proxy, not tokenizer-specific measurement.

## Resume Or Follow-up Notes

If future usage shows over-strict conformance behavior, adjust `Allowed Variations` semantics explicitly rather than adding a size-based shortcut. If context grows, tighten validator budgets and move examples to direct references without weakening runtime gates.
