# Final Report: Mechanism Before Design

## Objective

Prevent agents from changing software or skill architecture on an unverified model of a controlling harness, framework, runtime, protocol, platform, vendor, model, tool, or infrastructure system.

## What Changed

- Added a fail-closed mechanism-before-design protocol and routed core Clarify, Plan, and Implement through it.
- Added `Wrong-Mechanism Green` proof challenge and mechanism validity to final review.
- Added intent, artifact, and report fields needed to preserve mechanism evidence across turns.
- Added deterministic behavioral cases and retained live evaluation evidence.
- Added a canonical 211-word repo-level `AGENTS.md` policy because a matched Codex A/B demonstrated that skill-body doctrine alone did not reliably control explicit solution wording.
- Added `check-agents-policy.py` to validate and emit the canonical policy without loading or duplicating full skill bodies.

## Files Touched

- Runtime contracts: the three existing skill entrypoints and applicable direct references under `suites/software-engineering/skills/`
- Shared doctrine: `references/four-principles.md`, `references/orchestration-policy.md`, and `references/agents-enforcement-policy.md`
- Validation: `scripts/validate-suite.sh`, `scripts/check-skill-architecture.py`, and `scripts/check-agents-policy.py`
- Evaluation: behavioral cases/fixtures, golden transcripts, mini-stress cases, verification-hazard cases, and `tests/mechanism-before-design/evaluation.md`
- Operator guidance: root and suite READMEs plus root `AGENTS.md`
- Continuity: this final report, the work packet, and the progress log

## Decisions

- Preserve the three public skills and four core modes.
- Keep detailed mechanism procedure in one direct core reference.
- Treat `do X because Y` as premise-dependent authority unless X is explicitly required even if Y is false.
- Require repo-level enforcement for the accepted Codex deployment contract; skill-only installation is not accepted for this failure mode.
- Keep the canonical policy bounded and validate its size independently of activated skill-entrypoint budgets.

## Verification

- `./scripts/validate-suite.sh` — passed after implementation and again after final-review correction.
- `git diff --check` — passed.
- `python3 suites/software-engineering/scripts/check-agents-policy.py` — passed at 211 words.
- `python3 suites/software-engineering/scripts/check-agents-policy.py --emit` — emitted a byte-identical policy into all live evaluation workspaces.
- Codex CLI `0.144.5`, `gpt-5.6-sol`, low reasoning — canonical-policy target prompt passed 3/3.
- Canonical-policy local-only negative controls — passed 3/3.
- Writable disposable target counter-check — no file-change event and no byte-level target diff.

## Observed Evidence

- Skill-only matched arm attempted a patch and requested a writable rerun.
- The root-policy matched arm remained in Clarify, recorded a contradicted mechanism verdict, and returned to Plan without a mutation attempt.
- Three canonical-policy acceptance runs repeated the no-mutation behavior.
- A writable run repeated the same decision, ruling out read-only sandbox awareness as the stopping cause for the tested surface.
- A policy that blocked all edits would have failed the negative controls; instead, the presentation and deterministic script edits proceeded exactly and the local lookup remained read-only.

## Intended State

- Mechanism-dependent architecture writes require complete decision-changing evidence and `Mechanism Verdict: established`.
- Local-only deterministic work proceeds without irrelevant external research.
- Structural validation is never promoted to runtime-mechanism proof.
- Public skill count remains three and activated entrypoints remain at or below 3,750 words.

## Observed State

- Canonical policy enforces the target gate on the recorded Codex runtime.
- Local-only controls proceed within exact boundaries.
- Public skill count remains three.
- Activated entrypoints total 3,630 words; canonical repo policy is 211 words.

## Intent Conformance

`conforms`. No public-skill split, size-based workflow tier, universal browsing rule, or weakened causal/conformance gate was introduced.

## Mechanism Validity

- Claim: skill-body instructions alone reliably prevent explicit solution wording from bypassing the mechanism gate.
- Evidence: contradicted by the clean skill-only Codex run.
- Claim: the canonical repo-level policy controls this decision path on the target runtime.
- Evidence: matched A/B, canonical 3/3, and writable no-mutation counter-check.
- `Mechanism Verdict: established` for the recorded Codex CLI `0.144.5` surface and prompt.
- Cross-version, cross-model, cross-harness, and alternative-prompt behavior remain unverified recurrence boundaries.

## Verification Hazards

### Claim Under Test

The complete three-skill suite plus canonical repo policy prevents the demonstrated premature architecture mutation without blocking deterministic local work on the recorded target runtime.

### Hazard Scan

- `Bypassed-Layer Green`: clear — the real Codex CLI path was exercised and the writable counter-check made no mutation event or target diff.
- `Subset Green`: clear for the scoped Codex CLI claim; other harnesses and versions are excluded explicitly.
- `Wrong-Theory Green`: clear — the matched A/B discriminated skill-only from repo-policy control; `Wrong-Mechanism Green` was challenged with live behavior.
- `Wrong-Tree Green`: clear — the canonical block was emitted from the working-tree artifact used by every accepted run, and full validation ran on the same working tree.
- `Not-Your-Red`: clear — the hung concurrent control was excluded, interrupted before editing, and rerun alone; no failure was attributed to the product change.
- `Weak-Oracle Green`: clear — the oracle rejects mutation attempts and writable diffs, while negative controls reject the plausible but nonconforming implementation that blocks every edit.

### Sufficiency Gates

- Layer: real Codex CLI and writable target exercised.
- Surface: scoped to Codex CLI `0.144.5`, `gpt-5.6-sol`, low reasoning.
- Cause: matched A/B varied only repo-level policy in the decisive probe.
- Artifact: current working-tree policy emitted into isolated copied-skill workspaces.
- Baseline: skill-only arm failed; policy arm and repeated runs passed.
- Outcome: no mutation attempt/diff on target case; exact expected behavior on three local controls.
- Conformance: three public skills, bounded context, no universal browsing, and exact policy ownership preserved.

### Verification Verdict

`confirmed` for the scoped claim.

## Acceptance Coverage

| Commitment | Observed State | Status | Evidence |
| --- | --- | --- | --- |
| Preserve three public skills | core, hazards, and review remain public owners | conforms | directory and registration validation |
| Block unproven mechanism-dependent edits | canonical target 3/3 plus writable counter-check | conforms | live event transcripts and target diffs |
| Avoid research overreach | local controls 3/3 | conforms | exact diffs, no-edit lookup, syntax result |
| Keep context bounded | 3,630 entrypoint words; 211-word repo policy | conforms | architecture and policy validators |
| Preserve proof and review gates | hazards and change-review route mechanism validity explicitly | conforms | skill validation and behavioral fixtures |

## Deviations

- Failed blind iterations were retained and corrected prospectively.
- The first parallel B/C transcript capture was not graded because output truncation hid the final decisions; filtered reruns supplied inspectable evidence.
- One concurrent negative-control process hung without a decision event, was interrupted with exit 130 before editing, and was excluded; its isolated rerun passed.
- Final review found the report template omitted the valid `contradicted` verdict; it was corrected and guarded by validation before acceptance.

## Remaining Risks

- Projects that install only the skills but omit the canonical root policy can reproduce the observed failure.
- Other agent harnesses, Codex versions, models, reasoning levels, and prompt phrasings need their own forward-test before receiving the same claim.
- The policy adds 211 always-active words to repositories that adopt it; this is intentional and separately bounded.

## Verdict

`accept` for the working-tree suite with the canonical repo policy as part of the deployment contract.
