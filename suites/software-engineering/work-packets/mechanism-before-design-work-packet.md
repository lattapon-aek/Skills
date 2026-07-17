# Work Packet: Mechanism Before Design

## Objective

Prevent agents from changing software or skill architecture on an unverified model of a harness, framework, runtime, protocol, platform, vendor, or other controlling system.

## User Instructions

- Use the observed failure where agents implemented a public-skill split before researching Codex skill loading as the primary use case.
- Add a conditional mechanism gate without creating another public skill or size-based workflow tier.
- Forward-test with blind sub-agents and require the failing use case to pass.
- After the matched A/B isolated the effective control point, continue by shipping and validating a reusable repo-level enforcement policy.

## Authority Mode

`execute-within-scope`

## Required Sequence

1. Preserve the 0/3 blind baseline.
2. Add the conditional mechanism protocol and runtime routing.
3. Extend proof challenge and acceptance review.
4. Add positive and negative-control fixtures.
5. Validate and rerun blind tests in isolated worktrees.
6. Challenge the green result and complete change review.

## Source Documents

- `AGENTS.md`
- Current three-skill runtime suite
- Existing direct mode references and architecture validator
- Blind evaluation outputs summarized below

## Current Assumptions

- The gap is pre-plan mechanism validation, not causal debugging after a failure.
- Local source, official documentation, maintainer source, or a live probe can each establish a mechanism when they directly control the decision.
- A universal browsing requirement would be an overcorrection.

## Scope

- Core entrypoint and a new direct mechanism reference
- Clarify, Plan, and Implement protocols
- Verification hazards and change review
- Shared operating gates, artifact templates, README, validator, and behavioral cases
- A compact copy-paste `AGENTS.md` policy, repository dogfooding, and deterministic policy validation

## Out of Scope

- New public skills or core modes
- Mandatory internet research for local-only behavior
- Changes to the three-role ownership model
- Weakening intent conformance or causal-debugging gates

## Decisions

- Add `Mechanism-Before-Design` as a conditional cross-mode gate.
- Keep detailed procedure in `references/mechanism-design-protocol.md`.
- Treat a user-proposed system model and architecture as hypotheses until controlling behavior is established.
- Expand `Wrong-Theory Green` with a `Wrong-Mechanism Green` pattern rather than add a seventh hazard.
- Add `Mechanism Validity` to acceptance review so conformance to a bad plan cannot pass.
- Keep the detailed workflow in the skills, but place the fail-closed selection and mechanism precedence rules in a compact repo-level policy because the matched Codex A/B showed that this is the effective instruction layer.

## Intended State

- Architecture work depending on external or uninspected behavior stops before editing until the controlling mechanism is established.
- Local-only work proceeds without unnecessary external research.
- Structural validation is not accepted as proof of runtime improvement.

## Plan Commitments

- Preserve three public skills.
- Keep entrypoint total at or below 3,750 words.
- Require 3/3 blind agents to avoid premature edits on the failing prompt.
- Include negative controls against research overreach.

## Observable Conformance Criteria

- Core directly routes applicable work to the mechanism protocol.
- Clarify separates objective, proposed explanation, and proposed solution.
- Plan cannot commit architecture while a decision-changing mechanism claim is unverified.
- Hazards and review reject structural green built on an unverified system model.
- Validator and fixtures enforce the contract.

## Allowed Variations

None for public-skill count, gate semantics, entrypoint budget, or blind-test threshold.

## Forbidden Substitutions

- Generic “research more” prose without a proceed gate
- Universal browsing for every task
- Treating intent conformance as mechanism validity
- Passing on average when any of the three blind runs edits prematurely

## Plan Amendment Authority

The user must approve any change to the three-skill architecture or blind acceptance threshold.

## Plan

1. Add the direct mechanism protocol and compact core routing.
2. Integrate conditional fields and exit gates into Clarify, Plan, and Implement.
3. Extend Wrong-Theory Green and change-review rubric.
4. Update templates, suite docs, and deterministic validation.
5. Add failing use case, structural-green case, bad-plan review case, and local-only controls.
6. Run full validation and blind evaluation.
7. Ship the reusable harness policy, validate its required contract and size, then repeat the live target case and local-only negative controls.

## Proof Strategy

- `./scripts/validate-suite.sh`
- Architecture budget and direct-link checks
- Static fixture assertions
- Three fresh isolated blind runs on the same raw prompt
- Negative controls reviewed for unnecessary browsing or blocking
- Final verification-hazards scan and change-review verdict

## Acceptance Matrix

| Commitment | Type | Source | Expected State | Observed State | Status | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Preserve three public skills | architecture | user | Same three runtime entrypoints | core, hazards, and review remain the only public skills | conforms | skill directory and registration inspection |
| Add mechanism gate | behavior | blind baseline | No architecture edit before mechanism evidence | canonical root policy produced 3/3 no-mutation target runs with contradicted verdicts | conforms | Codex CLI `0.144.5` canonical-policy accepted run |
| Avoid research overreach | behavior | approved plan | Local-only controls remain direct | preference edit, local lookup, and local script edit proceeded without external research | conforms | negative controls: 3/3 |
| Keep context bounded | performance | approved plan | Entrypoints <= 3,750 words | 3,630 words; repo policy is outside conditional skill-body loading | conforms | architecture and policy validators |
| Blind recovery | evaluation | approved plan | 3/3 pass on acceptance bytes and target harness | canonical-policy target run 3/3; canonical-policy local-only controls 3/3 | conforms | retained evaluation names runtime, target copies, invalid capture, and recurrence boundary |
| Allow bounded probes | behavior | review finding | Isolated diagnostic writes may proceed without target mutation | Node cwd probe created and removed disposable `/tmp` artifacts; target unchanged | conforms | `disposable_probe_control` and retained command/output |
| Validate and review | proof | repository instructions | Full suite green and accepted diff | deterministic suite, live policy evaluation, local controls, writable-layer counter-check, hazards scan, and final review green | conforms | final report and repeated full-suite validation |

## Deviations

None against the approved plan. Several blind iterations failed the new gate and drove prospective doctrine changes before the final accepted run.

## Open Questions

None blocking.

## Resume Instructions

Accepted working-tree result. The deployment contract includes the canonical root `AGENTS.md` policy; do not generalize acceptance to skill-only installs or untested runtimes. Next repository action is an intentional commit/push when requested.
