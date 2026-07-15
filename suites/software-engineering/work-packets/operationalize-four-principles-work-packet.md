# Work Packet: Operationalize The Four Principles

## Objective

Replace four vague value headings with four operational rules that tell an agent when the rule applies, what action it requires, what gate permits progress, and what behavior counts as a violation.

## User Instructions

- Improve the current headings because they feel broad and unclear.
- Preserve the original intent while making agent behavior concrete.

## Authority Mode

`execute-within-scope`

## Required Sequence

1. Inspect the current principle definitions and all active references.
2. Define concrete replacement names and behavioral contracts.
3. Update the shared doctrine first, then each skill and user-facing documentation.
4. Add regression coverage and stale-name validation.
5. Validate and review the final working tree.

## Source Documents

- `suites/software-engineering/references/four-principles.md`
- the three shipped skill entrypoints
- `suites/software-engineering/README.md`
- current work packet and review findings from the preceding suite-improvement task

## Current Assumptions

- The user wants implementation, not only naming suggestions.
- The existing `four-principles.md` path remains stable for compatibility.
- The rules should stay shared across all three skills.

## Scope

- Rename the four principles to operational rules.
- Define trigger, required action, proceed gate, and violation signal for each.
- Update active skill and README references.
- Add regression coverage and stale-name validation.
- Keep the doctrine concise enough for skill context.

## Out of Scope

- Renaming the `four-principles.md` file.
- Changing skill ownership or adding a fourth skill.
- Committing or pushing the working tree.

## Decisions

- `Think Before Coding` becomes `Evidence Before Action`.
- `Simplicity First` becomes `Smallest Sufficient Change`.
- `Surgical Changes` becomes `Proven Change Boundary`.
- `Goal-Driven Execution` becomes `Requirement-to-Proof Closure`.
- Use the same four field labels for each rule: `Trigger`, `Required Action`, `Proceed Gate`, `Violation Signal`.

## Plan

1. Rewrite the shared reference.
2. Update all three skill entrypoints and suite documentation.
3. Add a mini-stress case and validation scans.
4. Run skill validation, executable fixtures, stale scans, and a blind forward test.
5. Review instruction compliance, proof sufficiency, and residual risk.

## Proof Strategy

- `rg` must find no active use of the four old headings.
- `./scripts/validate-suite.sh` must pass.
- A blind agent response must apply the new rule names to a realistic over-broad patch request.
- The final diff must remain inside the documented scope and pass `git diff --check`.

## Acceptance Matrix

| Requirement | Source | Status | Evidence |
| --- | --- | --- | --- |
| Replace vague headings | user | satisfied | shared reference and all active references use the four operating rules |
| Make behavior concrete | user | satisfied | every rule defines Trigger, Required Action, Proceed Gate, and Violation Signal |
| Preserve original intent | inferred constraint | satisfied | evidence, minimality, scope, and proof intent retained in operational form |
| Add regression and stale coverage | suite contract | satisfied | mini-stress case 10 and validation stale-name scan |
| Validate and review | suite contract | satisfied with residual risk | validation passed and blind behavior narrowed scope; cross-model consistency remains unproven |

## Deviations

`none observed`

## Open Questions

- None blocking. The requested concern is specific enough to proceed with operational names and gates.

## Resume Instructions

Read this packet, inspect the current diff because it contains uncommitted prior suite improvements, and modify only the active doctrine/docs/tests/validation needed for this task. Preserve all preceding user changes.
