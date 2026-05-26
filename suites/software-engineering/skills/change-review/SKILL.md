---
name: change-review
description: Review repository changes with an evidence-first, impact-aware workflow. Use when an agent must inspect a diff, pull request, patch set, or working tree and report correctness risks, regressions, root-cause gaps, and missing proof before changes are accepted.
---

# Change Review

## Intent

Review from evidence, not from taste. Prioritize correctness, proof, and impact over style commentary.
Stay in review mode: inspect the change, trace its behavior, assess impact, and report findings. Do not silently drift into implementation, broad redesign, or speculative debugging unless the review must explicitly explain why the change is unsafe.

## Four Principles

Apply these principles while reviewing:

### 1. Think Before Coding

- Confirm the intended requirement before judging the diff.
- Surface ambiguity and alternative interpretations instead of overclaiming.

### 2. Simplicity First

- Flag unnecessary complexity when a smaller change would have solved the same problem.
- Treat speculative abstraction as review risk, not design sophistication.

### 3. Surgical Changes

- Check whether every changed area traces back to the stated objective.
- Flag orthogonal edits and unrelated cleanup that increase risk.

### 4. Goal-Driven Execution

- Check whether success was defined concretely.
- Prefer reviews grounded in tests, repro steps, and validation output over aesthetic opinion.

## Clarify Until Clear

- Confirm the intended requirement or change objective before judging the diff.
- If the expected behavior is unclear, state that uncertainty and limit conclusions accordingly.
- If critical review context is missing, say what is missing and how it limits confidence instead of overclaiming.

## When Not To Use

- Do not use this skill as a substitute for `task-intake` when the request itself is still unclear.
- Do not use this skill as a substitute for `root-cause-debugging` when the main problem is still proving why a failure happens.
- Do not use this skill as a substitute for `change-implementation` when the task is to make the change rather than assess it.

## Source Of Truth

Use the best available evidence during review:

- Read the actual diff and the surrounding code paths that determine behavior.
- Check tests, configs, logs, and validation output when they affect the conclusion.
- Search external sources when the change depends on framework semantics, API contracts, standards, version changes, or vendor behavior not established by the repo alone.
- Prefer official docs, primary references, and maintainer-owned sources first.
- Do not infer safety from naming or code style alone.
- Separate observed evidence from inference. Make it clear when a finding is directly proven by the diff or surrounding code, and when it is a higher-confidence risk inference.

## Review Sufficiency

Before issuing a strong finding, try to establish all of these:

- the intended objective of the change is understood well enough to judge correctness
- the relevant diff and nearby code paths have been inspected
- any tests, logs, or validation output that materially affect the conclusion have been checked or explicitly noted as missing
- any external behavior that materially affects the conclusion has an authoritative source
- the impact path is concrete enough to explain who or what can break

If these are not true, reduce confidence, narrow the finding, or move the gap into `Open Questions` or `Residual Risk`.

## Scope Narrowing

- Focus first on correctness, regressions, missing verification, unsafe assumptions, and hidden impact.
- Ignore style nits unless they hide a real maintenance or behavior risk.
- Prefer the smallest defensible finding that matches the evidence.

## Review In Parts

1. Confirm what the change is supposed to do.
2. Inspect the actual diff and the surrounding implementation.
3. Check whether the code can actually do what the change claims.
4. Look for broken adjacent behavior, hidden regressions, and missing edge handling.
5. Check whether the verification is sufficient.
6. Assess whether the change is appropriately sized and scoped.

## Blast Radius Review

- Trace the likely impact path for each meaningful change: callers, downstream consumers, contracts, data shape, config, tests, runtime behavior, and operational expectations.
- Do not stop at the changed lines if the risk clearly propagates through nearby code paths.
- If the likely impact path is unclear, say so instead of pretending the review is complete.

## Impact And Tradeoffs

- Explain who or what is affected by each finding.
- Flag when a small local change hides a larger unresolved design or root-cause issue.
- Mention when a broader change would have been safer or more honest than the current patch.

## Output

- Report findings before summaries.
- Order findings by severity.
- Reference files and explain impact.
- Cite external sources when a finding depends on them.
- Distinguish `Observed Evidence` from `Inference` inside findings when the risk is not directly executed or proven.
- Include concerns you considered but ruled out when that context materially helps the user trust the review.
- If no findings are present, say so explicitly and mention residual risk or test gaps.

## Proof Gap Rule

- State what the available diff, code, tests, and validation output already prove.
- State what is still unverified, uninspected, or ambiguous.
- State what additional evidence would be needed to raise confidence or close the review gap.

Use:

- `Findings`
- `Open Questions`
- `Ruled-out Concerns`
- `Residual Risk`

## Phase Handoff

- Hand back to `task-intake` if the intended objective of the change is still too unclear to review correctly.
- Hand back to `root-cause-debugging` if the review identifies an unresolved failure mechanism that still needs diagnosis.
- Hand back to `change-implementation` if the review identifies concrete changes that must be made before acceptance.

## Reference

Use [references/review-template.md](references/review-template.md) for a compact review format.
Use [../../references/four-principles.md](../../references/four-principles.md) for the shared doctrine and rationale.
