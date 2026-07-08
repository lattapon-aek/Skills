# Orchestration Policy

Use this policy when one software-engineering task may span multiple phases.

## Suite Contract

This suite exists to make an agent work from evidence instead of confidence. The agent must always know which skill owns the current phase, what evidence is required to move forward, and which gate must receive the result next.

Use exactly one primary owner at a time:

- `software-engineering-core` owns the work: clarify, plan, analyze, implement, or justify no patch.
- `verification-hazards` challenges proof: decide whether a green/red result or agent report is trustworthy.
- `change-review` accepts or rejects the result: inspect the diff, proof, residual risk, and hand back if the result is not ready.

Do not treat these skills as optional style guidance. If a gate applies, run it or state why it does not apply.

## Default Flow

1. `software-engineering-core`
2. `verification-hazards` whenever a green result, CI result, benchmark, agent report, or suspicious red result is about to be trusted
3. `change-review` after a change or justified no-change outcome is ready to be assessed

Not every task requires every core mode. The point is to move forward only when the current evidence justifies the next mode.

## Skill Selection

- Use `software-engineering-core` when the agent still needs to understand, decide, diagnose, edit, or prove a software-engineering result.
- Use `verification-hazards` only when there is a concrete green/red result, benchmark, CI status, test run, agent report, or "done/fixed" claim that is being treated as proof. If the user asks whether to merge, ship, or close based on that claim, start here and use the hazard output fields.
- Use `change-review` only when there is a diff, patch set, working tree, PR, implemented result, or justified `no patch` conclusion ready for acceptance.
- If more than one skill seems relevant, start with the earliest unmet gate in the default flow. Do not jump to review while the objective, diagnosis, patch boundary, or proof is still missing.

Small-model routing shortcut: if the prompt contains `approve`, `ship`, `merge`, `accept`, `close`, `go/no-go`, `open market`, or `run in production` and the reason offered is "tests pass", "staging passed", "some servers are green", "dashboard is green", or "agent says done", choose `verification-hazards` as the primary answer. Start the response with `Claim Under Test`, not `Findings`.

## Routing Rules

- Start in core `Clarify` mode when the request is vague, broad, solution-biased, or missing proof of done.
- During core `Clarify`, a shallow source scan is allowed when routing depends on locating the likely seam, boundary, or owning module. Do not turn that into proof or solution work.
- Route to core `Plan` when the Clarify exit conditions are all met AND the objective is clear but the approach is not yet settled. Do not route to Plan if the failure domain is still unconfirmed.
- Route to core `Analyze` when the Clarify exit conditions are all met AND the failure domain is confirmed by at least one direct user statement or runtime signal — not by inference alone. Do not route to Analyze if two or more domains are equally probable with no distinguishing evidence.
- Route to core `Implement` when the objective, approach, and patch boundary are all clear enough to execute without further diagnosis.
- Route to `verification-hazards` before trusting a green or red result as proof. This is a lens inside the proof step, not a replacement for core diagnosis or implementation.
- Route to `verification-hazards` before any approval, shipment, merge, acceptance, closure, market-open, or production-run decision that depends on green output, staging output, partial rollout output, monitoring output, or a second-hand report.
- Route to `change-review` when the result needs acceptance review, proof-gap review, or residual-risk review.
- Do not end a multi-phase task with implementation or debugging output alone; emit an explicit `change-review`-shaped final report for any accepted patch or justified `no patch` outcome.

## Handoff Packets

When moving between skills, carry only the evidence needed by the next gate:

- Core to hazards: `Claim Under Test`, exact command/report/result, what it is supposed to prove, artifact or branch checked, known gaps.
- Hazards to core: failed hazard, observed tell, cheapest next check, and whether to resume `Analyze` or `Implement`.
- Hazards to review: verdict, confirmed gates, open hazards, residual risk.
- Core to review: objective, diff or no-patch conclusion, evidence inspected, verification run, hazard verdict if applicable, proof gaps.
- Review to core: blocking finding, required mode to resume, exact evidence or patch needed next.

Do not hand off a prose summary without enough source, command, diff, or runtime evidence for the next skill to inspect.

## Escalation Rules

- If the objective is still unclear, go backward to core `Clarify`, not forward into planning or coding.
- If implementation uncovers an unproven failure mechanism, go backward to core `Analyze`.
- If debugging proves the code is already correct in the current workspace, prefer `no patch` and surface the historical-vs-current-state mismatch explicitly.
- If review finds a correctness gap that still lacks diagnosis, go backward to core `Analyze`.
- If review finds a concrete execution gap with a clear fix, go backward to core `Implement`.

Observable thresholds for these rules:

- "still unclear" — the objective cannot be stated in one concrete sentence with a specific, verifiable success condition
- "unproven failure mechanism" — no log, trace, repro, test, or runtime signal directly confirms the suspected root cause; the cause is inferred only
- "code is already correct" — the reported failure cannot be reproduced in the current workspace after direct inspection of the reported code path

## Required Reporting Across Phases

- Keep `Observed Evidence` separate from `Inference`.
- State `Current Workspace State` separately from `Historical Incident State` when they differ.
- Use the skill-specific ruled-out field to show what was considered and rejected:
  - `Clarify` mode: `Ruled-out Interpretations`
  - `Plan` mode: `Ruled-out Options`
  - `Analyze` mode: `Ruled-out Hypotheses`
  - `Implement` mode: `Rejected Approaches`
  - `change-review`: `Ruled-out Concerns`
- State proof gaps explicitly in every mode using the `Proof Gap` field:
  - what is already proven
  - what is not yet proven
  - what next evidence or check would close the gap
- When verification depends on a passing or failing run, include the `verification-hazards` verdict or state why that lens was not applicable.
- If local and external evidence conflict, surface the conflict and resolve it with the most authoritative source available. Do not silently discard either side.

## Execution Loop

For multi-step work, enforce this loop:

1. inspect the facts that can actually be checked
2. confirm the current assumption set against source material or runtime evidence
3. choose the narrowest justified core mode
4. act on one small step
5. observe the result
6. run `verification-hazards` if the observation is being treated as proof
7. re-check impact and proof gaps before moving on

If a fact is inspectable, inspect it instead of guessing. If the current evidence does not justify the next step, route back to the earlier core mode that can close the gap.

## No-Patch Rule

`No patch` is a valid end state when:

- the failure cannot be reproduced in the current workspace after direct inspection of the reported code path
- no evidence in the current code, config, or runtime supports a justified fix
- the agent reports exactly what was checked and what was not checked
- residual risk and remaining proof gaps are stated explicitly

A `no patch` conclusion must still pass through `change-review`. The review should record what was checked, what could not be proven, and what residual risk remains.
