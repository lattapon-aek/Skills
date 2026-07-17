# AI Agent Software-Engineering Skills

An evidence-first suite for agents that must understand the objective, diagnose failures causally, implement within an approved boundary, prove the observed result, and reject working-but-unintended outcomes.

## Install

```powershell
npx skills add https://github.com/lattapon-aek/Skills --skill software-engineering-core --skill verification-hazards --skill change-review
```

Adapters:

- Claude Code: `scripts/link-software-engineering-skills.ps1`
- Codex: `scripts/link-codex-skills.ps1`
- skills CLI: `npx skills add ...`

## Runtime Architecture

The suite keeps three public skills with separate ownership:

```text
software-engineering-core
        ↓ concrete proof claim
verification-hazards
        ↓ confirmed or still-gapped verdict
change-review
```

- `software-engineering-core` owns Clarify, Plan, Analyze, Implement, and justified no patch.
- `verification-hazards` challenges whether a green/red result or report proves shipping behavior and approved intent.
- `change-review` owns final acceptance of a concrete result.

Each `SKILL.md` is a compact runtime entrypoint. Core loads the direct protocol for the selected mode; expanded hazard patterns and output templates load only when their trigger applies. This progressive disclosure reduces activated context without reducing the gates an applicable task must pass.

## Full Applicable Workflow

Task size does not change execution rigor. Every task must pass every gate that applies:

1. Record user contract and authority.
2. Establish objective, intended state, source material, and proof of done.
3. Select the evidence-justified core mode.
4. Establish any controlling mechanism the architecture decision depends on.
5. Read the applicable direct reference.
6. Diagnose or implement within a proven boundary.
7. Observe functional and mechanism behavior.
8. Compare observed state with intended state.
9. Challenge proof through `verification-hazards` when a result or report is being trusted.
10. Use `change-review` before accepting a concrete patch, result, or no-patch conclusion.

Continuity artifact choice affects only audit and resume durability. An inline contract never authorizes weaker analysis, verification, conformance, or review.

## Intent-To-Outcome Conformance

Functional success and plan fidelity are independent requirements.

Before implementation, freeze:

- `Intended State`
- `Plan Commitments`
- `Observable Conformance Criteria`
- `Allowed Variations` — default `none`
- `Forbidden Substitutions`
- `Plan Amendment Authority`

After implementation, compare intended and observed state. Use:

- `conforms`
- `authorized deviation`
- `unresolved deviation`

An unresolved material deviation blocks completion even when tests pass and the system remains usable. The agent may restore the approved state within scope, or return to Plan and amend the working document prospectively. It may not authorize its own material deviation or rewrite the plan after the fact.

## Mechanism Before Design

A clear user-proposed architecture is not automatically a proven plan. When a recommendation depends on harness, framework, runtime, protocol, platform, vendor, model, tool, or infrastructure behavior not established by local source, separate the objective from the proposed explanation and solution. Inspect implementing source, official contracts, or live behavior before committing the architecture.

Structural validation proves structure. It does not by itself prove context usage, dispatch, lifecycle, compatibility, performance, or another runtime outcome. Mechanism-dependent work uses the direct `mechanism-design-protocol.md` reference and keeps the edit gate closed while a decision-changing claim remains conditional or unproven.

## Skills

### `software-engineering-core`

Use for most engineering work:

- `Clarify` — objective, contract, domain, intended state, and proof of done
- `Plan` — options, boundary, commitments, allowed variations, and proof strategy
- `Mechanism Before Design` — conditional system-model evidence before architecture commitment
- `Analyze` — incident evidence, causal chain, competing hypotheses, discriminating checks, and root-cause gate
- `Implement` — assumption revalidation, narrow patch, original-reproduction replay, conformance check, and proof

Mode detail lives in direct references under `skills/software-engineering-core/references/`.

The entrypoint also carries the preflight rule, suite routing (earliest unmet gate, no gate re-entry without new evidence), and the adaptive reporting rule, so they load at runtime instead of relying on repository policy files alone.

### `verification-hazards`

Use before trusting a test, CI run, benchmark, staging result, rollout signal, suspicious red, or agent report. Scan:

1. `Bypassed-Layer Green`
2. `Subset Green`
3. `Wrong-Theory Green`
4. `Wrong-Tree Green`
5. `Not-Your-Red`
6. `Weak-Oracle Green`

Then establish Layer, Surface, Cause, Artifact, Baseline, Outcome, and Conformance. Return `confirmed` only when every applicable gate passes; otherwise return `still a lead` and the cheapest next check.

The entrypoint names its required input packet (claim, intended state, artifact identity, commands and outputs, known gaps); a missing field is named and recovered or returned, never assumed. The same `still a lead` verdict is never handed back twice without new evidence.

### `change-review`

Use for a concrete diff, PR, working tree, commit, implemented result, or justified no patch. Review:

- functionality and root-cause closure
- intent conformance and plan fidelity
- mechanism validity and whether the plan follows the actual controlling system
- code health and smallest sufficient change
- blast radius and rollback
- proof sufficiency and oracle strength
- instruction compliance and acceptance coverage
- deviations and residual risk

Return `accept`, `accept with authorized deviation`, or the exact owner and mode that must resume.

## Shared References

- [references/four-principles.md](references/four-principles.md) — evidence, scope, proof, and intent-conformance gates
- [skills/software-engineering-core/references/context-continuity.md](skills/software-engineering-core/references/context-continuity.md) — working documents, resume safety, and prospective plan amendments (ships inside the core skill so installed copies stay self-contained)
- [references/orchestration-policy.md](references/orchestration-policy.md) — ownership, routing, and handoff packets
- [references/agents-enforcement-policy.md](references/agents-enforcement-policy.md) — canonical copy-paste repo policy that activates selection and mechanism precedence before skill loading

## Enforce Selection With `AGENTS.md`

Installing skills makes them available but does not guarantee implicit selection or mode precedence. Copy the canonical block from [references/agents-enforcement-policy.md](references/agents-enforcement-policy.md) into the target repository's root `AGENTS.md`. It covers preflight selection, premise-dependent authority, the fail-closed mechanism checkpoint, intent conformance, proof challenge, and final review without duplicating the full skill bodies.

Emit only the copy block for automation or a temporary evaluation workspace:

```bash
python suites/software-engineering/scripts/check-agents-policy.py --emit
```

## Reporting Conventions

- Separate `Observed Evidence` from `Inference`.
- Keep historical incident state separate from current workspace state.
- Map each user requirement and plan commitment to expected state, observed state, status, and evidence.
- Record material deviations when they occur, including corrected deviations.
- Treat missing proof and unresolved conformance as blockers, not omitted rows.
- Keep user-proposed explanations and solutions as hypotheses until decision-changing mechanisms are established.
- Preserve ruled-out interpretations, options, hypotheses, approaches, and concerns in their owning mode.

## Tests

Fixture suites live under `tests/`:

- `software-engineering-core/` — mode behavior and end-to-end flows
- `verification-hazards/` — false-green and proof-sufficiency cases
- `change-review/` — concrete acceptance reviews
- `golden-transcripts/` — routing and output contracts
- `internet-derived/` — public incident patterns
- `mini-stress/` — small-model failure modes
- `skill-flow/` — observed suite-level assessments
- `behavioral/` — machine-gradable cases and the transcript grading harness

Coverage includes premature patching, symptom fixes, competing hypotheses, environment failures, wrong-layer and wrong-tree greens, weak oracles, unsourced external claims, context resume, instruction tracking, and working-but-plan-divergent results.

To measure agent behavior against the suite, grade transcripts with the behavioral harness:

```bash
python suites/software-engineering/scripts/run-behavioral-eval.py --transcripts <dir>
```

See [tests/behavioral/README.md](tests/behavioral/README.md) for agent-driving mode, metrics, and check semantics.

## Validation

Prerequisites:

- Node.js 23.6+ (native TypeScript type stripping), or 22.6+ with `--experimental-strip-types`. The fixtures import `.ts` files directly and use `import.meta.dirname`.
- `quick_validate.py` from the skill-creator toolkit. The validator looks in `$CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py` (default `~/.codex/...`); point `SKILL_VALIDATE_PY` at your copy if it lives elsewhere.

Run:

```bash
./scripts/validate-suite.sh
```

The suite validator checks skill frontmatter, TypeScript fixtures, registration, direct-reference integrity, entrypoint budgets, required routing contracts, and stale doctrine.

Individual Windows validation:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\suites\software-engineering\skills\software-engineering-core
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\suites\software-engineering\skills\verification-hazards
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\suites\software-engineering\skills\change-review
```

## Add A Skill

```powershell
.\scripts\new-skill.ps1 -Name my-skill -DisplayName "My Skill" -ShortDescription "What it does" -DefaultPrompt "Use $my-skill to help with this task."
```

Keep new suite content under `suites/software-engineering/` and validate it before review.
