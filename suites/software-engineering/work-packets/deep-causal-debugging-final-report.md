# Final Report: Deep Causal Debugging

## Objective

Make the software-engineering suite diagnose issues causally, reject guesses and symptom patches, and prove that the original problem is resolved for the demonstrated reason before acceptance.

## What Changed

- Added a causal debugging protocol with precise diagnostic vocabulary, a causal-chain trace, a hypothesis ledger, discriminating checks, a root-cause gate, corrective-action classification, and post-fix resolution proof.
- Required the protocol from core Analyze for bugs, regressions, incidents, hangs, performance problems, flaky failures, and tooling/environment failures.
- Blocked corrective implementation until the root-cause gate is met while preserving an explicit emergency-mitigation path.
- Required bug fixes to replay the frozen pre-fix reproduction, observe the original outcome oracle, inspect the former divergence point, run an adjacent control, and state the recurrence boundary.
- Added adversarial cases for symptom patches, confirmation bias, retry-based false fixes, wrong-layer unit green, and first-plausible-cause behavior.

## Files Touched

- `suites/software-engineering/skills/software-engineering-core/SKILL.md`
- `suites/software-engineering/skills/software-engineering-core/references/causal-debugging-protocol.md`
- `suites/software-engineering/skills/software-engineering-core/references/implementation-checklist.md`
- `suites/software-engineering/tests/software-engineering-core/analysis/cases.md`
- `suites/software-engineering/tests/mini-stress/cases.md`
- `suites/software-engineering/README.md`
- `scripts/validate-suite.sh`
- this task's work packet, progress log, and final report

The broader dirty working tree also contains preceding user-requested suite improvements. Those changes were preserved and are not claimed as part of this causal-debugging slice.

## Decisions

- Keep debugging in `software-engineering-core` Analyze rather than add a competing top-level skill.
- Put detailed mechanics in a directly linked 97-line reference; keep core `SKILL.md` at 500 lines.
- Require evidence that differentiates hypotheses. Evidence compatible with every live explanation does not establish root cause.
- Treat a successful patch as outcome evidence, not retrospective causal proof.
- Allow mitigation under explicit authority but keep the issue and root-cause proof gap open.

## Verification Hazards

### Claim Under Test

The revised skills cause an Agent to reject a plausible symptom patch and perform causal diagnosis before implementation or issue closure.

### Hazard Scan

- `Bypassed-Layer Green` — clear for instruction behavior: the fresh Agent read and applied the current repository skill; runtime debugging effectiveness remains outside this documentation-only fixture.
- `Subset Green` — at risk: forward proof covers one Redis-latency scenario and one Agent/model context, not every issue class or model size.
- `Wrong-Theory Green` — clear for the scenario: the prompt did not disclose the expected diagnosis; the Agent independently retained competing pool, network, command, dependency, and retry hypotheses.
- `Wrong-Tree Green` — clear for the named target: validation and forward test used the current working tree; no commit or shipping-artifact claim is made.
- `Not-Your-Red` — not applicable: no failure is attributed to this change.
- `Weak-Oracle Green` — clear for the targeted behavior: the acceptance oracle required a no-patch decision, observed/inferred separation, competing hypotheses, a discriminating next check, mitigation labeling, and refusal to close the issue; the fresh output demonstrated each.

### Counter-Checks Run

- `./scripts/validate-suite.sh`: 3/3 skills valid, 14/14 executable fixtures passed, structure/registration/stale scans passed.
- `git diff --check`: passed.
- Fresh-context forward scenario: returned `still a lead`, root cause `unproven`, no corrective patch, timeout change classified as mitigation, causal links labeled observed/inferred, six live hypotheses retained, and a trace-based distinguishing check proposed.

### Verification Verdict

`confirmed` for the targeted Redis-timeout scenario and current working-tree instructions; generalization remains bounded by the stated subset risk.

### Proof Gap

No automated model-evaluation harness executes the Markdown behavioral cases. Cross-model, small-model, intermittent-race, data-corruption, and multi-service incident behavior still require additional forward cases.

## Findings

No blocking findings for this scoped change.

## Instruction Compliance

- Used the skill-creation workflow and progressive disclosure.
- Preserved the suite's evidence-first, single-owner, proof-gated doctrine.
- Created durable work artifacts before editing.
- Added realistic cases and performed a fresh-context forward test.
- Did not commit, push, install, or modify application fixtures.

## Acceptance Coverage

| Requirement | Status | Evidence |
| --- | --- | --- |
| Support real issue debugging | satisfied | Analyze requires the causal protocol for failure work |
| Analyze deeply and avoid invented causes | satisfied | causal chain, hypothesis ledger, and discriminating checks |
| Avoid fixing the wrong point | satisfied | root-cause gate and corrective-action classification |
| Prove the original issue is gone | satisfied | original-reproduction replay and outcome-oracle requirement |
| Reduce repeated repair | satisfied with residual risk | recurrence boundary, adjacent controls, and return-to-Analyze rule |

## Deviations

- The first forward prompt disclosed evaluation framing. It was not used as sole acceptance evidence; a second fresh-context test without that framing was run and passed.

## Open Questions

none blocking

## Ruled-out Concerns

- A separate debugging skill was rejected because it would split ownership and create routing ambiguity.
- A generic instruction such as “analyze deeper” was rejected because it provides no proceed gate or falsifiable behavior.
- Mandatory exhaustive hypothesis lists were rejected; only realistic alternatives with decision-changing checks are required.

## Residual Risk

- Behavioral consistency across models and complex production incidents is not fully proven.
- Markdown cases are specification fixtures, not automated model-grade evaluations.
- The working tree includes earlier uncommitted suite changes, so any future commit should review and scope the full diff intentionally.

## Resume Or Follow-up Notes

Add fresh-context cases for concurrency races, partial data corruption, stale caches, resource exhaustion, and historical-only production incidents if broader behavioral proof is needed. Commit or push only after the user requests it and the full dirty tree is reviewed.
