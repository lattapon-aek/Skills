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
4. Read that mode's direct reference.
5. Diagnose or implement within a proven boundary.
6. Observe functional behavior.
7. Compare observed state with intended state.
8. Challenge proof through `verification-hazards` when a result or report is being trusted.
9. Use `change-review` before accepting a concrete patch, result, or no-patch conclusion.

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

## Skills

### `software-engineering-core`

Use for most engineering work:

- `Clarify` — objective, contract, domain, intended state, and proof of done
- `Plan` — options, boundary, commitments, allowed variations, and proof strategy
- `Analyze` — incident evidence, causal chain, competing hypotheses, discriminating checks, and root-cause gate
- `Implement` — assumption revalidation, narrow patch, original-reproduction replay, conformance check, and proof

Mode detail lives in direct references under `skills/software-engineering-core/references/`.

### `verification-hazards`

Use before trusting a test, CI run, benchmark, staging result, rollout signal, suspicious red, or agent report. Scan:

1. `Bypassed-Layer Green`
2. `Subset Green`
3. `Wrong-Theory Green`
4. `Wrong-Tree Green`
5. `Not-Your-Red`
6. `Weak-Oracle Green`

Then establish Layer, Surface, Cause, Artifact, Baseline, Outcome, and Conformance. Return `confirmed` only when every applicable gate passes; otherwise return `still a lead` and the cheapest next check.

### `change-review`

Use for a concrete diff, PR, working tree, commit, implemented result, or justified no patch. Review:

- functionality and root-cause closure
- intent conformance and plan fidelity
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

## Enforce Selection With `AGENTS.md`

Installing skills makes them available but does not guarantee implicit selection. Projects that require this suite should include a compact policy like:

```md
## Required Software-Engineering Workflow

For software-engineering work, use `agents-skills:software-engineering-core` before planning, debugging, editing, or verification. Name the selected skill and reason before the first engineering tool call.

Record the user contract, intended state, plan commitments, allowed variations, and proof obligations in a user-supplied document, repo-local work packet, or compact inline contract appropriate only to continuity risk. Task size does not reduce execution rigor.

Do not accept a result merely because it works. Compare observed state with intended state; an unapproved material deviation blocks completion and must be corrected or returned to Plan for prospective amendment.

Use `agents-skills:verification-hazards` before trusting green/red output or an agent report, and `agents-skills:change-review` before accepting every concrete patch or justified no-patch conclusion.
```

## Reporting Conventions

- Separate `Observed Evidence` from `Inference`.
- Keep historical incident state separate from current workspace state.
- Map each user requirement and plan commitment to expected state, observed state, status, and evidence.
- Record material deviations when they occur, including corrected deviations.
- Treat missing proof and unresolved conformance as blockers, not omitted rows.
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

Coverage includes premature patching, symptom fixes, competing hypotheses, environment failures, wrong-layer and wrong-tree greens, weak oracles, unsourced external claims, context resume, instruction tracking, and working-but-plan-divergent results.

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
