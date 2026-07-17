# Mechanism-Before-Design Protocol

Use this protocol when a design, migration, configuration, optimization, or skill architecture decision depends on harness, framework, runtime, protocol, platform, vendor, model, tool, operating-system, infrastructure, or external-service behavior not already established by the workspace.

Do not use it for pure user preference or behavior fully controlled and directly inspectable in current local source.

## 1. Separate Objective From Theory

Record:

- `User Objective` — the outcome the user needs.
- `User-Proposed Explanation` — why the user thinks the current state behaves as it does.
- `User-Proposed Solution` — the requested architecture or implementation.

The explanation and solution remain hypotheses. Clear file instructions and explicit implementation authority do not prove or waive the system model behind them.

### Parse Authority Precisely

- `Do X because Y` selects X through premise Y. Authority to edit X activates only after every decision-changing part of Y is `established`.
- `Do X even if Y is false` or an equivalent explicit instruction makes X an independent requirement; record Y as disproved without using it as design evidence.
- When wording is unclear, preserve the objective, report how the mechanism changes the recommendation, and resolve the choice before editing.

## 2. Extract Mechanism Claims

For each claim record:

`Mechanism Claim | Exact Qualifier | Decision Dependency | Evidence Source | Evidence Entailment | Observed or Inferred | Falsifying Check | Status`

Keep only claims that can change the recommendation. Examples include what a harness loads into context, how a framework dispatches requests, which runtime owns state, or which protocol boundary retries work.

Extract every causal or outcome clause used to select the design, including `because`, `so that`, `to reduce`, and equivalent wording. Decompose compound claims by system link. A missing row defaults to `unproven`; the gate is the logical AND of all decision-changing rows.

## 3. Locate The Controlling Mechanism

Use the strongest applicable source:

1. Live behavior from the real layer and version.
2. Implementing source code, configuration, tests, or protocol definitions.
3. Official documentation, specifications, release notes, or maintainer source.
4. Secondary sources only to locate primary evidence.

Local file shape is evidence about the repository, not automatically about external runtime behavior. A validator proving folder or manifest structure does not prove latency, context usage, dispatch, lifecycle, or other runtime outcomes.

Do not infer a cardinality, exclusivity, guarantee, or hard limit from grammatical singular, one example, an undocumented alternative, or absence of contrary evidence. Require a direct contract, controlling implementation, or discriminating observation for the claimed constraint.

### Evidence Entailment Gate

Set a claim to `established` only when the observed result or authoritative proposition entails the entire claim, including qualifiers such as `only`, `exactly`, `all`, `always`, `never`, ordering, scope, and cardinality. Record the precise proposition the source supports. Evidence for a weaker or merely related behavior leaves the stronger claim `unproven`, even when the proposed design still appears reasonable.

The user's request, a plan, the proposed solution, and an agent assertion are claim sources, not mechanism evidence. A pre-write verdict is invalid when any decision-changing ledger row is absent, cites one of those sources as evidence, or lacks an inspected authoritative source or discriminating observation.

## 4. Build The Smallest System Model

Describe only the chain needed for the decision:

`input/discovery -> selection -> controlling transition -> observable outcome`

Mark each link `observed` or `inferred`. State version, environment, artifact, and surface when they affect applicability.

Evidence for one link cannot establish another. Discovery or registration does not by itself establish selection, loading, injection, execution, or the final outcome; apply the same separation to any system chain.

## 5. Run A Discriminating Check

Prefer the cheapest check where competing system models predict different results. Use source inspection, a minimal live probe, instrumentation, or a before/after measurement. A check that would pass under every architecture theory cannot open the gate.

## 6. Apply The Gate

The design gate opens only when:

- every mechanism claim that can change the architecture has direct evidence
- local observations are separated from external behavior
- source version and execution surface match the target closely enough
- the recommendation follows from the established mechanism
- the proof strategy measures the user objective, not only structural conformance

If a material claim remains unverified, provide a conditional plan and name the exact evidence needed. Do not edit architecture or convert the proposed solution into a plan commitment.

If evidence contradicts a rationale that materially selected the proposed solution, invalidate that plan. Do not silently preserve the solution by inventing a different benefit, treating its file shape as an independent requirement, or deciding that the user would want it anyway. Return to `Clarify` or `Plan`, show the contradiction and alternatives, and obtain authority for a newly justified design before editing.

### Required Pre-Write Checkpoint

Before the first mutating tool call against the target workspace or architecture, record:

- `Mechanism Verdict: established`
- the evidence that established each decision-changing claim
- why the selected architecture follows from that evidence

If the verdict is `conditional`, `unproven`, or `contradicted`, target mutation is forbidden. Initialization, scaffolding, generated placeholders, moves, renames, manifest edits, and documentation relocation all count as target mutation. Do not invoke a creation or implementation workflow merely to prepare while the gate is closed.

A discriminating diagnostic probe may create isolated, disposable artifacts outside the target boundary when read-only evidence cannot establish the mechanism. Declare the probe boundary, predicted outcomes, and cleanup first. Do not let probe artifacts alter the target, become implementation scaffolding, or survive the evaluation unless the user requests them as evidence.

## Required Output

- `User Objective`
- `User-Proposed Explanation`
- `User-Proposed Solution`
- `Mechanism Claims`
- `Controlling Mechanism`
- `Mechanism Evidence`
- `Evidence Entailment`
- `System Model`
- `Observed Evidence vs Inference`
- `Falsifying Check`
- `Decision Sensitivity`
- `Mechanism Verdict` — `established`, `conditional`, `unproven`, or `contradicted`
- `Proof Gap`
