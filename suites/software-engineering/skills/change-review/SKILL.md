---
name: change-review
description: Review repository changes with an evidence-first, impact-aware workflow. Use when an agent must inspect a diff, pull request, patch set, or working tree and report correctness risks, regressions, root-cause gaps, and missing proof before changes are accepted.
---

# Change Review

## Intent

Review from evidence, not from taste. Prioritize correctness, proof, and impact over style commentary.
Stay in review mode: inspect the change, trace its behavior, assess impact, and report findings. Do not silently drift into implementation, broad redesign, or speculative debugging unless the review must explicitly explain why the change is unsafe.
Golden rule: every accepted end state needs an explicit review artifact. That includes self-review after implementation and review of a justified `no patch` conclusion.

## Four Principles

Apply the shared doctrine from [../../references/four-principles.md](../../references/four-principles.md). In review context:

- `Think Before Coding` — confirm the intended requirement before judging the diff; surface ambiguity instead of overclaiming
- `Simplicity First` — flag unnecessary complexity when a smaller change would have solved the same problem
- `Surgical Changes` — check that every changed area traces back to the stated objective; flag orthogonal edits
- `Goal-Driven Execution` — check whether success was defined concretely; prefer reviews grounded in tests and validation output over aesthetic opinion

## Clarify Until Clear

- Confirm the intended requirement or change objective before judging the diff.
- If the expected behavior is unclear, state that uncertainty and limit conclusions accordingly.
- If critical review context is missing, say what is missing and how it limits confidence instead of overclaiming.

## When Not To Use

- Do not use this skill as a substitute for `software-engineering-core` when the request still needs clarification, planning, diagnosis, or implementation.

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

## Review Rubric

Judge the change primarily on:

- `Functionality`: does the change actually do what it claims
- `Code Health`: is the result maintainable and free of unnecessary complexity
- `Complexity`: could a smaller change have solved the same problem
- `Blast Radius`: what callers, contracts, or runtime paths could break
- `Proof Sufficiency`: did the tests, logs, or validation actually prove the claim

## Blast Radius Review

- Trace the likely impact path for each meaningful change: callers, downstream consumers, contracts, data shape, config, tests, runtime behavior, and operational expectations.
- Do not stop at the changed lines if the risk clearly propagates through nearby code paths.
- If the likely impact path is unclear, say so instead of pretending the review is complete.

## Impact And Tradeoffs

- Explain who or what is affected by each finding.
- Flag when a small local change hides a larger unresolved design or root-cause issue.
- Mention when a broader change would have been safer or more honest than the current patch.
- Prefer findings grounded in facts and observed behavior over opinion about style or taste.

## Output

- Report findings before summaries.
- Order findings by severity using these levels:
  - `critical` — change is incorrect or will cause failures in likely code paths
  - `high` — significant risk to correctness, safety, or reliability
  - `medium` — notable concern that warrants attention but does not block acceptance
  - `low` — minor observation with a real behavior implication
  - `note` — context or tradeoff that does not require action
- Reference files and line numbers for each finding.
- Cite external sources when a finding depends on them.
- Distinguish `Observed Evidence` from `Inference` inside findings when the risk is not directly executed or proven. Place these as sub-items directly under the finding they support.
- Include concerns you considered but ruled out when that context materially helps the user trust the review.
- If no findings are present, say so explicitly and mention residual risk or test gaps.
- Use the full review structure even when reviewing your own work or a `no patch` outcome. Do not collapse the final phase into a prose-only status update.
- If local and external evidence conflict, surface the conflict explicitly under the finding rather than silently resolving it.

## Proof Gap Rule

- State what the available diff, code, tests, and validation output already prove.
- State what is still unverified, uninspected, or ambiguous.
- State what additional evidence would be needed to raise confidence or close the review gap.

Use:

- `Findings`
- `Open Questions`
- `Ruled-out Concerns`
- `Residual Risk`

When reviewing a `no patch` outcome:

- `Findings` should say whether any justified code change is still required
- `Ruled-out Concerns` should record candidate fixes or explanations that were checked and rejected
- `Residual Risk` should capture what the current evidence still does not prove

## Phase Handoff

Hand back to `software-engineering-core` when any of the following is true:

- The intended objective cannot be inferred from the diff, ticket, or surrounding context — route to core `Clarify`
- The failure mechanism the change claims to fix is asserted but not demonstrated by evidence — route to core `Analyze`
- The diff contains no executable result and it is not possible to determine whether the approach works — route to core `Implement`

When handing back, state which mode to resume and what specific information that mode needs to close the gap. Do not hand back without a concrete reason and a clear next action.

## Reference

Use [references/review-template.md](references/review-template.md) for a compact review format.
Use [../../references/four-principles.md](../../references/four-principles.md) for the shared doctrine and rationale.
