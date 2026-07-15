# Work Packet: Deep Causal Debugging

## Objective

Strengthen the software-engineering suite so an agent investigates an issue causally, avoids patching symptoms or favored theories, and proves that the original failure is gone for the demonstrated reason before accepting the fix.

## User Instructions

- Support issue debugging and problem solving, not only careful execution.
- Make analysis deeper and sharper.
- Do not invent explanations from the first signal encountered.
- Do not apply a plausible patch that leaves the real issue present.
- Reduce repeated repair caused by wrong root-cause attribution.

## Authority Mode

`execute-within-scope`

## Required Sequence

1. Inspect the current Analyze workflow and its tests.
2. Identify operational gaps rather than merely adding stronger adjectives.
3. Add a reusable causal-debugging protocol through progressive disclosure.
4. Connect the protocol to Analyze, Implement, verification, and acceptance.
5. Add cases that distinguish genuine diagnosis from plausible storytelling.
6. Validate the suite and independently forward-test the revised behavior.

## Source Documents

- `suites/software-engineering/skills/software-engineering-core/SKILL.md`
- `suites/software-engineering/tests/software-engineering-core/analysis/cases.md`
- `suites/software-engineering/skills/software-engineering-core/references/implementation-checklist.md`
- `suites/software-engineering/skills/verification-hazards/SKILL.md`
- `suites/software-engineering/references/four-principles.md`
- `scripts/validate-suite.sh`

## Current Assumptions

- The current suite already routes bugs to Analyze and asks for reproduction, fault location, root cause, and ruled-out hypotheses.
- The missing control is a concrete causal investigation protocol and a root-cause proof gate.
- Detailed debugging mechanics belong in a directly linked reference so the core skill stays concise.

## Scope

- Core Analyze workflow and outputs.
- Handoff from diagnosis to implementation.
- Post-fix proof against the original reproduction.
- Debugging tests and suite registration checks.
- README description of Analyze behavior.

## Out of Scope

- Domain-specific debugging playbooks for every language or runtime.
- Adding a fourth top-level skill solely for debugging.
- Changing application fixtures unless a new executable discriminator is necessary.
- Commit, push, release, or installation.

## Decisions

- Keep debugging owned by `software-engineering-core` Analyze rather than introducing routing ambiguity with a separate skill.
- Add a `causal-debugging-protocol.md` reference with mandatory causal gates.
- Distinguish `symptom`, `fault location`, `failure mechanism`, and `root cause`; none are interchangeable.
- Require competing hypotheses and discriminating checks, not a list of decorative possibilities.
- Require pre-fix reproduction, causal intervention where feasible, and post-fix replay of the original reproduction plus adjacent controls.

## Plan

1. Define investigation states and root-cause proof criteria.
2. Require the protocol from Analyze and from bug-fix verification.
3. Add adversarial cases for symptom suppression, confirmation bias, correlation, and issue recurrence.
4. Register the protocol in validation and documentation.
5. Run validators, fixtures, stale checks, blind forward test, proof challenge, and final review.

## Proof Strategy

- Static: skill validation, required-term registration, diff hygiene.
- Behavioral specification: adversarial analysis cases with explicit expected and rejected behavior.
- Forward test: give a blind agent an issue report containing a tempting but unproven fix theory.
- Acceptance: inspect whether the change closes the causal gap without bloating or conflicting with existing suite doctrine.

## Acceptance Matrix

| Requirement | Source | Status | Evidence |
| --- | --- | --- | --- |
| Support issue diagnosis and debugging | User request | satisfied | Analyze now requires `causal-debugging-protocol.md` for issues and incidents |
| Analyze deeply rather than infer from first signal | User request | satisfied | causal chain, hypothesis ledger, and discriminating checks are mandatory |
| Avoid wrong-point fixes | User request | satisfied | Root-Cause Gate blocks corrective patching from an unproven theory |
| Confirm the original problem is actually gone | User request | satisfied | Implement requires original-reproduction replay and the original outcome oracle |
| Reduce repeat fixes | User request | satisfied with residual risk | recurrence boundary and adjacent controls are required; cross-model consistency remains unproven |
| Preserve existing suite doctrine and dirty-tree work | Repository instructions | satisfied | task-scoped edits preserved prior changes; full suite validation passed |

## Deviations

none observed

## Open Questions

none blocking

## Resume Instructions

Read this packet, inspect the current dirty diff before editing overlapping files, and preserve all preceding user-requested suite changes. Continue with the causal protocol, tests, validation, blind forward test, and change-review-shaped final report. Do not commit or push.
