# Work Packet: History-Derived Skill Improvements

## Objective

Improve the software-engineering suite so it addresses observed collaboration failures: skipped skill selection, lost user instructions, unnecessary phase stops, weak test oracles, report/commit drift, silent deviations, and excessive ceremony for small work.

## User Instructions

- Apply the improvements recommended in the preceding analysis.
- Preserve the suite split: core owns work, verification-hazards challenges proof, and change-review accepts results.
- Keep changes inside `suites/software-engineering/` unless repository-level validation or enforcement documentation must change.

## Authority Mode

`execute-within-scope`

## Required Sequence

1. Read the applicable skills and repository instructions.
2. Record the work contract before doctrine edits.
3. Update doctrine, metadata, tests, and validation consistently.
4. Run validation and challenge the green result.
5. Review the final diff before acceptance.

## Source Documents

- `AGENTS.md`
- `suites/software-engineering/README.md`
- `suites/software-engineering/references/context-continuity.md`
- `suites/software-engineering/references/orchestration-policy.md`
- the three shipped `SKILL.md` files
- history-derived failure patterns summarized by the user-approved analysis

## Current Assumptions

- No fourth skill is required.
- Existing skill names and ownership boundaries remain stable.
- The user authorized implementation but did not request a commit or push.

## Scope

- Add a preflight skill-selection contract.
- Add user-contract and authority-mode fields to core work.
- Distinguish phase gates from mandatory user round trips.
- Add acceptance coverage and deviation reporting.
- Add a weak-oracle verification hazard and applicable-gate semantics.
- Add proportional continuity tiers without weakening packet-driven work.
- Add regression scenarios and validation coverage for the new contracts.
- Keep UI metadata and suite documentation consistent.

## Out of Scope

- Creating a new skill.
- Building a provider-backed model evaluation service.
- Committing, pushing, or publishing changes.
- Modifying runtime skill links outside this repository.

## Decisions

- Use a compact `User Contract` rather than a new skill.
- Use `plan-only`, `execute-within-scope`, `ask-before-edit`, and `exact-sequence` as authority modes.
- Add `Weak-Oracle Green` as hazard 6 and `Outcome` as its sufficiency gate.
- Allow same-turn phase progression when all gates are closed and authority permits it.
- Use continuity tiers: micro, standard, and high-risk.

## Plan

1. Update shared orchestration and context-continuity doctrine.
2. Update core, verification-hazards, and change-review contracts.
3. Update templates, agent metadata, and suite documentation.
4. Add history-derived assessment cases and validation scans.
5. Run skill validation, all executable fixtures, and targeted contract scans.
6. Challenge the green result and perform final change review.

## Proof Strategy

- Run `./scripts/validate-suite.sh`.
- Run every `*.test.ts` fixture, not only the representative subset.
- Run direct searches for the new selection, authority, acceptance, deviation, and weak-oracle contracts.
- Inspect the final diff and verify no unrelated files changed.
- Forward-test the revised suite with an independent agent on a bounded history-derived scenario.

## Acceptance Matrix

| Requirement | Source | Status | Evidence |
| --- | --- | --- | --- |
| Add enforced skill-selection preflight | approved analysis | implemented | orchestration policy, AGENTS.md, suite README |
| Add user contract and authority modes | approved analysis | implemented | core skill and templates |
| Allow same-turn phase progression when authorized | approved analysis | implemented | core and orchestration policy |
| Add acceptance matrix and deviations | approved analysis | implemented | core, review, templates |
| Add Weak-Oracle Green | approved analysis | implemented | hazard skill, catalog, tests |
| Add proportional continuity tiers | approved analysis | implemented | context continuity and docs |
| Add history-derived regression cases | approved analysis | implemented | golden, mini-stress, hazard, and flow cases |
| Strengthen validation | approved analysis | implemented | full test discovery and contract scans in validate-suite.sh |
| Run proof and final review | suite contract | satisfied | suite validation passed, blind rerun passed, and final diff review recorded in the final report |

## Deviations

- No provider-backed automated transcript service was added; the repository has no provider-neutral execution harness. Structured scenarios and deterministic validation were strengthened instead, with an independent forward test planned for this run.
- The first blind forward test used `Baseline` instead of the exact `Not-Your-Red` hazard label. The output contract was tightened and a fresh blind rerun passed with all six exact labels.

## Open Questions

- None blocking. Provider-backed automated transcript evaluation remains a future enhancement; this patch will add structured scenarios and stronger static/executable validation without external service dependencies.

## Resume Instructions

Read this packet, inspect `git status` and the current diff, then continue from the first incomplete plan item. Do not trust a prior validation summary without rerunning the relevant command on the current tree.
