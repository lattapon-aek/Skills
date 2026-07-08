---
name: verification-hazards
description: Proof-challenge lens for software-engineering results and go/no-go gates. Use when a test, probe, CI run, benchmark, red/green status, staging result, partial rollout, or agent report says a change works, fails, is done, or was amended, and the agent must decide whether that observation actually exercised the shipping behavior on the real layer, full surface, proven cause, committed artifact, and stable baseline before review. Also use as the primary output for approve, ship, merge, accept, close, go/no-go, or production-run questions whose safety depends on a green result or report.
---

# Verification Hazards

## Intent

"Verified means observed output" is necessary but not sufficient. The observation itself can be false: it can run on a bypassed layer, cover only a subset, confirm a wrong theory, inspect the wrong artifact, or measure an unstable baseline. This skill names the five ways a green (or red) result lies and gives the cheapest counter-check for each.

Golden rule: a passing result is a claim about the shipping behavior, not proof of it. Before you elevate green to `Observed Result`, confirm the observation touched the same layer, surface, cause, artifact, and baseline that production uses.

This skill is a lens, not a mode. It sharpens the `Verification`, `Observed Result`, and `Proof Gap` fields of `software-engineering-core` and the `Proof Sufficiency` rubric of `change-review`. Apply it at every verification gate; do not replace the core workflow with it.

## Suite Role

This skill owns proof skepticism. It does not clarify the task, design the fix, diagnose the root cause from scratch, or review the whole diff. It asks one question: "Can this result be trusted as proof of the claimed behavior?"

Use it only after there is a concrete claim under test:

- a green or red command result
- a CI status
- a benchmark or probe
- a sub-agent or executor report
- a "done", "fixed", "amended", or "tests pass" claim

Return either `confirmed` or `still a lead`. If it is still a lead, name the exact next gate: back to `software-engineering-core` `Analyze`, back to `software-engineering-core` `Implement`, or forward to `change-review` with the open proof gap.

If the user asks "approve?", "merge?", "ship?", "accept?", "close the task?", "is this done?", "go/no-go?", or "can we run this in production?" based mainly on a green run, staging result, partial rollout, benchmark, smoke test, or agent report, this skill is the primary output. Use the fields in `Output` before any review-shaped summary. Do not answer only with `Findings` unless there is an actual diff or accepted result already under `change-review`.

## Must Obey

- Do not trust "done", "fixed", "amended", "tests pass", or "CI green" without a hazard scan.
- Do not use `Findings` as the primary output; start with `Claim Under Test`.
- Do not answer a proof-gated approve/ship/merge/accept/production-run question with a prose verdict first; the first heading must be `Claim Under Test`.
- Do not claim a command-based counter-check passed unless the command and observed output are stated.
- Do not diagnose or patch here; hand back to the correct core mode when proof fails.

## When To Use

- A test, probe, or benchmark is green and you are about to call the work done.
- A staging result, partial deployment, unit test, smoke test, or integration test is being used to justify production approval, shipment, merge, acceptance, or closure.
- CI is red (or green) and you must decide whether the result is about your change.
- A sub-agent, executor, sandbox, or teammate reports "done", "fixed", or "amended".
- A feature is gated by a trigger, telemetry input, state transition, or timeout you cannot see in a unit test.
- A fix rests on a root-cause theory you have not yet observed failing.

## When Not To Use

- Do not use this skill to shape a vague request, choose an approach, or diagnose an unknown failure from scratch — use `software-engineering-core`.
- Do not use this skill just because engineering work is happening; use it only when a result or report is being treated as proof.
- Do not use it as the final acceptance artifact — hand the confirmed (or still-gapped) result to `change-review`.

## Four Principles

Apply the shared doctrine from [../../references/four-principles.md](../../references/four-principles.md). In verification context:

- `Think Before Coding` — name what the green result actually exercised before trusting it; state the assumption the test encodes.
- `Simplicity First` — pick the cheapest counter-check that closes the specific gap; do not build a full harness when one `git show` or one second tick settles it.
- `Surgical Changes` — verify the exact artifact and layer that ships, not an adjacent copy.
- `Goal-Driven Execution` — define, before running, which observation would prove the shipping behavior and which would only prove the test's own setup.

## The Five Hazards

Each hazard is a way an observation lies, the tell that exposes it, and the counter-check that closes it. Cheapest sufficient check wins.

### 1. Bypassed-Layer Green

The test exercises a mock, shim, direct handler call, or injected state — not the real trigger, transport, or transition that production uses. It is green because the bypassed path has none of the constraints the real path imposes.

- Tell: the test calls the effect directly (`flush()`, the handler, a setter) instead of firing the event that would call it; a probe sleeps or grants on the client side of a boundary the real code crosses; a stateful behavior is asserted after injecting the state rather than after driving the transition.
- Counter-check: exercise the same entry layer production uses. For anything gated by a trigger, telemetry value, timeout, deadline, or state machine, run an end-to-end pass through the real trigger (a "live capstone"). For a hold, latch, or debounce that must survive re-evaluation, run a **second tick** after the trigger and confirm it still holds — do not set the state directly.
- Cheapest proof: one real-trigger run, or one extra evaluation cycle, that reaches the same code the bypass skipped.

### 2. Subset Green

You ran a slice that structurally cannot reach the failing case: a packet/module subset, a compile-only build, local-only when the break is CI-only, or a sandbox that cannot bind sockets, spawn processes, or touch the filesystem the failing test needs.

- Tell: green came from a command narrower than the full surface; the environment that produced green is known to be unable to run part of the suite; "passes locally" without a CI check.
- Counter-check: run the full suite in the target environment — CI, the real (not fake) provider/adapter, and the race detector where concurrency matters. Know exactly what your sandbox structurally cannot run, and run those parts in an environment that can. Check CI every time, not just local gates.
- Cheapest proof: the full-suite result from the environment that actually ships the code, plus an explicit note of anything the local/sandbox run could not cover.

### 3. Wrong-Theory Green

The fix is built on an unconfirmed root-cause theory. The offline test passes because it encodes the same wrong assumption the fix does, so both agree with each other and neither touches reality.

- Tell: the root cause was inferred, never observed failing; the repro was constructed from the theory rather than from the live failure; a prior "fix" for the same symptom already bounced.
- Counter-check: instrument or reproduce the **actual** live failure and let the observed signal name the cause before authoring the fix. Read the real error, the real stream, the real process state (log the failing value, `grep` the raw stream, `lsof` the live process) rather than theorizing about a rendered or summarized view. A plausible theory you have not seen fail is a lead, not a diagnosis.
- Cheapest proof: one observation of the real failure that the theory predicts — and that a competing theory would not.

### 4. Wrong-Tree Green

The artifact you verified is not the one that ships. The fix passed in a working tree that was never committed, an uncommitted file is invisible to the worktree or executor that runs it, a build-machine path or stray file leaked into the diff, or a required companion change (a count, a manifest, a registration) was skipped.

- Tell: "amended" or "committed" asserted without inspecting the commit; a worktree/executor built from a branch that lacks the local change; a diff that references a path only the author's machine has; a green run whose environment differs from the committed state.
- Counter-check: verify ground truth, not the claim. Inspect the committed content directly (`git show HEAD:<file>`), scan the diff for leaked absolute paths and stray files, and re-run the full suite from a clean checkout of exactly what ships. Treat any "done/fixed/amended" report from a sub-agent, sandbox, or other environment as a lead until the committed artifact confirms it.
- Cheapest proof: the shipping artifact read from the commit (not the working tree) reproducing the green result.

### 5. Not-Your-Red

A red result you did not cause: a pre-existing flake, environment contention, or a timing/throughput sensitivity that mimics a deterministic regression. Attributing it to your change sends you fixing the wrong thing.

- Tell: the failure is intermittent, timing-shaped, or resource-shaped; it names a subsystem your change did not touch; it can pass 3/3 in isolation yet fail under load.
- Counter-check: reproduce the **baseline** before blaming the diff. Run the parent commit under the same stress the failure appeared under — high repeat count, constrained parallelism, resource contention, the CI-like environment. Isolate contention first (kill leaked servers/processes, re-run in isolation) before trusting a FAIL.
- Cheapest proof: the same failure (or its absence) on the untouched parent under matched stress, distinguishing pre-existing flake from a real regression.

## Cross-Cutting Rule: A Report Is A Lead

The evidence hierarchy already treats a user report as a lead, not proof. Extend that to every second-hand green: an executor's "tests pass", a sandbox's exit code, a teammate's "it works", your own memory of a prior run. Each is a lead that points at where to look, not a substitute for observing the shipping behavior yourself. When the producer of a result cannot run the layer/surface/environment that ships, the gap is yours to close.

## Verification Sufficiency Gate

Before elevating any green to `Observed Result`, confirm all five:

- `Layer` — the observation exercised the real trigger/transport/transition, not a bypass.
- `Surface` — the run covered the full shipping surface in the target environment, or the uncovered part is named.
- `Cause` — for a fix, the root cause was observed failing, not only theorized.
- `Artifact` — the verified code is the committed/shipping artifact, not an uncommitted or adjacent copy.
- `Baseline` — a red result was checked against the untouched baseline under matched stress before being attributed to the change.

If any is not established, the result stays a lead. State the open one in `Proof Gap` and name the cheapest check that would close it.

## Output

Report against the five hazards, then hand off. Start with these fields in this order:

- `Claim Under Test` — the green/red result and what it is being taken to prove.
- `Hazard Scan` — one line per hazard: `clear`, `at risk`, or `not applicable`, with the tell that decided it.
- `Counter-Checks Run` — the checks performed and their observed output; separate `Observed Evidence` from `Inference`.
- `Verification Verdict` — `confirmed` (all five gates pass) or `still a lead` (one or more open).
- `Proof Gap` — what is now proven, what is still unproven, and the cheapest next check for each open gap.
- `Residual Risk` — what could still differ between the observation and the shipping behavior.

Do not use `Findings` as the primary heading in this skill. `Findings` belongs to `change-review`; use it only after the hazard verdict is handed to review.

For any command-based counter-check, include the command and the observed output summary. Do not write "`git show` matched", "`git diff` was empty", or "tests pass" unless the command was run and the relevant output is stated.

Keep it terse for small claims; do not collapse the hazard scan into prose.

## Phase Handoff

- Route back to `software-engineering-core` `Analyze` when a counter-check exposes an unproven root cause (hazard 3) — the failure mechanism needs diagnosis, not more verification.
- Route back to `software-engineering-core` `Implement` when a counter-check shows the shipping artifact differs from the verified one (hazard 4) — the real change still has to land.
- Hand every confirmed or still-gapped verdict to `change-review` for the acceptance artifact; a `still a lead` verdict must be surfaced there, not hidden behind a green summary.

## Reference

- [references/hazard-catalog.md](references/hazard-catalog.md) — each hazard expanded with concrete field-tested patterns and the specific counter-check that caught it.
- [../../references/four-principles.md](../../references/four-principles.md) — shared evidence doctrine.
- [../../references/orchestration-policy.md](../../references/orchestration-policy.md) — routing across core and review.
