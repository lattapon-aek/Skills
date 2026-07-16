---
name: verification-hazards
description: Challenge whether software-engineering proof can be trusted. Use when a test, CI run, probe, benchmark, staging result, rollout signal, red/green status, or agent report is being used to claim work succeeds, fails, conforms, is done, or is safe to approve, merge, ship, close, or run in production.
---

# Verification Hazards

## Role

Own proof skepticism, not diagnosis, implementation, or final acceptance. A passing or failing observation remains a lead until it is tied to the shipping layer, complete surface, demonstrated cause, intended artifact, stable baseline, discriminating outcome, and approved intent.

Use this skill when there is a concrete claim under test:

- a test, probe, build, CI result, benchmark, smoke test, or runtime observation
- a staging, canary, partial rollout, monitoring, or production signal
- an agent, teammate, sandbox, or executor report such as “done”, “fixed”, “amended”, or “tests pass”
- an approve, merge, ship, accept, close, go/no-go, or production-run decision based on such evidence

Do not use it to shape an unclear task, diagnose an unknown failure from scratch, author a patch, or replace `change-review`.

## Must Obey

- Start proof-gated approval answers with `Claim Under Test`, not a prose verdict or `Findings`.
- Treat every second-hand result as a lead until its artifact and observation are inspected.
- State commands and observed output summaries for command-based counter-checks.
- Scan all six hazards in the required order; mark non-applicable hazards with a reason.
- Do not call a result confirmed while functional behavior or intent conformance remains unproven.
- Do not diagnose or patch here; route the failed gate to the correct core mode.

## Required Input

Expect from the requesting owner: the claim under test, the intended state with plan commitments and allowed variations, the exact acceptance artifact identity, the commands and observed outputs behind the claim, and known gaps. When an input is missing, name it, treat the affected gate as unproven, and either run the cheapest check that recovers it or return the request with the missing field named. Never fill a missing input from assumption.

## The Six Hazards

1. `Bypassed-Layer Green` — the observation used a mock, shim, direct call, injected state, or shortcut instead of the real production trigger, transport, or transition.
2. `Subset Green` — the run covered a slice or environment that cannot reach the failing or shipping surface.
3. `Wrong-Theory Green` — the fix and test encode an unobserved root-cause theory and agree with each other without touching the actual failure.
4. `Wrong-Tree Green` — the verified bytes, config, build, commit, or deployment are not the artifact being accepted.
5. `Not-Your-Red` — a red result is a baseline flake, environmental failure, contention effect, or unrelated break misattributed to the change.
6. `Weak-Oracle Green` — the assertion cannot distinguish the required result from a plausible incorrect or plan-divergent result.

Read [references/hazard-catalog.md](references/hazard-catalog.md) when a hazard is `at risk`, applicability is unclear, or a concrete tell and counter-check must be selected. Do not load the catalog merely to repeat definitions already sufficient for a clear scan.

## Verification Sufficiency Gate

Before elevating a result to proof, establish every applicable gate:

- `Layer` — the real trigger, transport, transition, or production entry path was exercised.
- `Surface` — the run covered the shipping surface and target environment, or names what remains uncovered.
- `Cause` — a claimed fix is tied to an observed failure mechanism, not only a theory-built reproduction.
- `Artifact` — the observed code, config, build, commit, or deployment is the named acceptance target.
- `Baseline` — an attributed red was compared with an untouched baseline under materially matched conditions.
- `Outcome` — the oracle proves the required behavior and rejects plausible incorrect behavior.
- `Conformance` — observed state matches the approved intended state, plan commitments, architecture boundary, output contract, and allowed variations.

`Cause` applies to fixes that claim a diagnosed mechanism. `Baseline` applies when attributing a red or instability to the change. `Artifact` must name the current target rather than assuming it is always `HEAD`.

### Intent-Conformance Counter-Check

Functional green is insufficient when the implementation differs from the approved plan. Compare:

- `Intended State`
- `Observed State`
- `Plan Commitments`
- `Allowed Variations` — default `none`
- `Deviations` and their authority source

Name one working but nonconforming implementation. If the current assertion would also pass that implementation, mark `Weak-Oracle Green: at risk` and keep the verdict `still a lead`.

Only `conforms` or an explicitly `authorized deviation` may pass the conformance gate. An agent's opinion that an alternative is equivalent, harmless, simpler, or better is not authority. An `unresolved deviation` blocks confirmation even when every functional test is green.

## Counter-Check Rule

Run the cheapest check that can change the verdict. Typical checks include:

- drive the real trigger or an additional state-machine tick
- run the full relevant surface in the target environment
- inspect the actual failure signal and compare competing causal predictions
- inspect the exact working tree, commit, build, or deployment being accepted
- reproduce the untouched baseline under matched stress
- strengthen the oracle until a plausible wrong or plan-divergent implementation fails

Do not claim a counter-check passed if it was not observed. If the environment cannot run the required layer or surface, retain the gap rather than generalizing from a smaller run.

## Output Contract

Use these fields in order:

- `Claim Under Test` — the result and what it is being taken to prove.
- `Hazard Scan` — all six hazard names in order, each `clear`, `at risk`, or `not applicable`, with the deciding tell or applicability reason.
- `Sufficiency Gates` — Layer, Surface, Cause, Artifact, Baseline, Outcome, and Conformance.
- `Counter-Checks Run` — exact checks and observed output; separate `Observed Evidence` from `Inference`.
- `Verification Verdict` — `confirmed` only when all applicable gates pass; otherwise `still a lead`.
- `Proof Gap` — what is proven, what remains open, and the cheapest next check.
- `Residual Risk` — what could still differ from the shipping or intended behavior.

Do not substitute gate labels for the six hazard names. Keep the scan compact, but never collapse it into an unsupported prose verdict.

## Handoff

- Return to core `Analyze` when cause is unproven or incident evidence contradicts the theory.
- Return to core `Plan` when observed state materially diverges from the approved intent or the plan must change.
- Return to core `Implement` when the shipping artifact is missing the change or the oracle must be strengthened.
- Hand confirmed and still-gapped verdicts to `change-review`; never hide an open hazard behind a green summary.
- Do not return the same `still a lead` verdict to the same mode twice without new evidence; surface the blocking fact as a stop condition instead of looping.
