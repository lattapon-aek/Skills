# Work Packet: Skill Runtime Context Refactor

## Objective

Reduce activated skill context without weakening the suite's evidence, causal-debugging, proof-challenge, intent-conformance, or acceptance gates.

## User Instructions

- Keep the three public skills: `software-engineering-core`, `verification-hazards`, and `change-review`.
- Keep the full applicable workflow for all engineering work.
- Do not introduce size-based rigor tiers or a lightweight path that skips gates.
- Make mode-specific detail load through direct references instead of keeping every procedure in each `SKILL.md`.
- Treat a working but plan-divergent result as incomplete unless the variation was pre-authorized or the plan is explicitly amended.
- Preserve the current dirty working tree as the implementation baseline.

## Authority Mode

`execute-within-scope`

## Required Sequence

1. Preserve and inspect the current working-tree baseline.
2. Refactor core and its direct mode references.
3. Refactor verification hazards and change review.
4. Reconcile shared doctrine, orchestration, continuity, README, and metadata.
5. Add architecture/context validation and behavioral fixtures.
6. Run full validation, challenge the proof, and complete change review.

## Source Documents

- `AGENTS.md`
- `suites/software-engineering/skills/software-engineering-core/SKILL.md`
- `suites/software-engineering/skills/verification-hazards/SKILL.md`
- `suites/software-engineering/skills/change-review/SKILL.md`
- `suites/software-engineering/references/context-continuity.md`
- `suites/software-engineering/references/four-principles.md`
- `suites/software-engineering/references/orchestration-policy.md`
- Current fixture and golden-transcript suites

## Current Assumptions

- The current uncommitted tree contains intended prior suite improvements and must not be discarded.
- The main context cost is the full body of each activated `SKILL.md`; direct references should contain mode-specific or expanded detail.
- A shorter entrypoint must still contain enough routing and hard gates to prevent skipped modes or silent plan drift.

## Scope

- The three skill entrypoints and their direct references
- Shared suite doctrine and orchestration references
- Skill UI metadata and suite README
- Validation scripts and fixture-driven behavioral tests

## Out of Scope

- New public skills
- Size-based execution rigor tiers
- Skipping proof or review for small tasks
- Installer redesign or unrelated repository cleanup

## Decisions

- Keep one primary owner at a time: core owns work, hazards challenges proof, review owns acceptance.
- Make core a mode router with mandatory invariants and direct references.
- Keep the six verification hazards; treat plan-divergent green as a weak-oracle/outcome-conformance failure rather than adding a seventh hazard.
- Add an `Intent-to-Outcome Conformance Gate` across plan, implementation, verification, and review.
- Default `Allowed Variations` to `none`; an agent cannot authorize its own material deviation.

## Plan

1. Consolidate duplicated analysis guidance into the causal-debugging protocol.
2. Move detailed Clarify, Plan, Analyze, and Implement procedures out of core's entrypoint.
3. Compress hazards and review while retaining their complete gates and output contracts.
4. Make continuity categories affect artifact durability only, never reasoning rigor.
5. Add deterministic budgets, direct-reference checks, and stale-link checks.
6. Add conformance and selective-reference routing cases.

## Proof Strategy

- Validate all skill frontmatter with `quick_validate.py` through `./scripts/validate-suite.sh`.
- Run all repository TypeScript fixtures.
- Enforce entrypoint word/line budgets and direct-reference integrity.
- Scan for deleted/stale references and prohibited size-based gate bypasses.
- Inspect the final diff and compare it to every plan commitment.
- Challenge the green validation result through all six verification hazards.

## Acceptance Matrix

| Commitment | Type | Source | Expected State | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| Keep three public skills | architecture | user | Same three skill entrypoints and ownership | satisfied | Three entrypoints remain and blind runs used the expected ownership chain |
| Reduce activated context | performance | approved plan | Entrypoints meet enforced budgets | satisfied | Architecture validator observed 3,421 total entrypoint words, down from 8,689 |
| Preserve full applicable workflow | behavior | user | No size-based gate bypass | satisfied | Core, continuity, orchestration, README, validator, and fixtures state that task size never lowers applicable gates |
| Preserve deep causal debugging | behavior | user | Root-cause gate remains explicit and tested | satisfied | Causal protocol retained the gate; blind Redis run returned unproven cause to Analyze |
| Block silent plan drift | behavior | user | Unapproved material deviation blocks completion | satisfied | Queue and schema blind runs returned still-a-lead and blocked acceptance despite functional green |
| Use direct progressive disclosure | architecture | approved plan | Mode detail lives in directly linked references | satisfied | Core routes directly to four mode protocols; blind causal run loaded causal protocol while conformance runs did not load unrelated mode protocols |
| Preserve dirty baseline | execution | user | No reset/revert of existing work | satisfied | No reset, checkout, revert, or destructive command used; pre-existing files remain in the working tree |
| Validate and review | proof | repository instructions | Full suite green plus hazards and review | satisfied | Full suite passed, runtime paths resolved, hazard scan confirmed the tested surface, and change review found no blocking issue |

## Deviations

None observed against the approved refactor plan. A stale validation assertion for the renamed Preflight heading was corrected before the successful full run and retained in this audit trail.

## Open Questions

- None blocking. Exact word budgets may be tightened only if the complete gate contract remains readable and fixtures continue to pass.

## Resume Instructions

Read this packet, inspect the current working tree, read the progress log if present, and resume from the first open acceptance row. Never assume `HEAD` represents the current baseline.
