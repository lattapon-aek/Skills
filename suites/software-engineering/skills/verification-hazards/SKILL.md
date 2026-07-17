---
name: verification-hazards
description: Challenge whether software-engineering proof can be trusted. Use when a test, CI run, probe, benchmark, staging result, rollout signal, red/green status, or agent report is being used to claim work succeeds, fails, conforms, is done, or is safe to approve, merge, ship, close, or run in production.
---

# Verification Hazards

## Role

Own proof skepticism, not diagnosis, implementation, or acceptance. Use for a concrete claim based on tests, probes, CI, benchmarks, runtime/rollout signals, agent reports, or evidence-backed approval decisions. The observation remains a lead until tied to layer, surface, cause, artifact, baseline, outcome, and intent. Do not clarify tasks, diagnose from scratch, patch, or replace `change-review` here.

## Must Obey

- Start proof-gated approval answers with `Claim Under Test`, not a prose verdict or `Findings`.
- Treat every second-hand result as a lead until its artifact and observation are inspected.
- State commands and observed output summaries for command-based counter-checks.
- Scan all six hazards in the required order; mark non-applicable hazards with a reason.
- Do not call a result confirmed while functional behavior or intent conformance remains unproven.
- Do not diagnose or patch here; route the failed gate to the correct core mode.

## Required Input

Require the claim, intended state, commitments, allowed variations, exact artifact, observed commands/output, and known gaps. Name missing input, keep its gate unproven, and run the cheapest recovery check or return it; never fill it from assumption.

## The Six Hazards

1. `Bypassed-Layer Green` — the observation used a mock, shim, direct call, injected state, or shortcut instead of the real production trigger, transport, or transition.
2. `Subset Green` — the run covered a slice or environment that cannot reach the failing or shipping surface.
3. `Wrong-Theory Green` — the fix, design, and test share an unobserved cause or mechanism theory. Name architecture/runtime instances `Wrong-Mechanism Green` in this row.
4. `Wrong-Tree Green` — the verified bytes, config, build, commit, or deployment are not the artifact being accepted.
5. `Not-Your-Red` — a red result is a baseline flake, environmental failure, contention effect, or unrelated break misattributed to the change.
6. `Weak-Oracle Green` — the assertion cannot distinguish the required result from a plausible incorrect or plan-divergent result.

Read [references/hazard-catalog.md](references/hazard-catalog.md) when a hazard is `at risk`, applicability is unclear, or a concrete tell and counter-check must be selected. Do not load the catalog merely to repeat definitions already sufficient for a clear scan.

## Verification Sufficiency Gate

Before elevating a result to proof, establish every applicable gate:

- `Layer` — real production trigger or transition exercised.
- `Surface` — shipping surface and target environment covered; gaps named.
- `Cause` — fix tied to observed mechanism, not a theory-built reproduction.
- `Artifact` — observed bytes or deployment are the acceptance target.
- `Baseline` — attributed red compared with an untouched matched baseline.
- `Outcome` — oracle rejects plausible wrong behavior.
- `Conformance` — observed state matches intent, commitments, boundaries, contract, and allowed variations.

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

### Mechanism Counter-Check

Structural green does not prove a runtime or architecture claim. For context, dispatch, lifecycle, performance, compatibility, or similar system behavior, inspect the controlling implementation, official contract, or live outcome. If structural checks pass under competing system models, mark `Wrong-Theory Green: at risk` with the `Wrong-Mechanism Green` pattern and keep the verdict `still a lead`.

## Counter-Check Rule

Run the cheapest verdict-changing check: drive the real trigger, expand to the target surface, compare causal predictions against the actual signal, inspect the accepted artifact, reproduce a matched baseline, or strengthen the oracle until plausible wrong results fail.

Do not claim a counter-check passed if it was not observed. If the environment cannot run the required layer or surface, retain the gap rather than generalizing from a smaller run.

## Output Contract

Use these fields in order:

- `Claim Under Test` — the result and what it is being taken to prove.
- `Hazard Scan` — all six hazard names in order, each `clear`, `at risk`, or `not applicable`, with the deciding tell or applicability reason.
- `Sufficiency Gates` — Layer, Surface, Cause, Artifact, Baseline, Outcome, and Conformance.
- `Mechanism Validity` — for mechanism-dependent claims, whether observed or authoritative behavior supports the design.
- `Counter-Checks Run` — exact checks and observed output; separate `Observed Evidence` from `Inference`.
- `Verification Verdict` — `confirmed` only when all applicable gates pass; otherwise `still a lead`.
- `Proof Gap` — what is proven, what remains open, and the cheapest next check.
- `Residual Risk` — what could still differ from the shipping or intended behavior.

Do not substitute gate labels for the six hazard names. Keep the scan compact, but never collapse it into an unsupported prose verdict.

## Handoff

- Return to core `Analyze` when cause is unproven or incident evidence contradicts the theory.
- Return to core `Plan` for material intent divergence, a needed plan change, or an unverified controlling mechanism.
- Return to core `Implement` when the shipping artifact is missing the change or the oracle must be strengthened.
- Hand confirmed and still-gapped verdicts to `change-review`; never hide an open hazard behind a green summary.
- Do not return the same `still a lead` verdict to the same mode twice without new evidence; surface the blocking fact as a stop condition instead of looping.
