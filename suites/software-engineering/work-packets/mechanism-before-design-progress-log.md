# Progress Log: Mechanism Before Design

## Timeline

- 2026-07-16: User approved the targeted mechanism-before-design change.
- 2026-07-16: Created branch `codex/add-mechanism-before-design-gate` and recorded the 0/3 blind baseline.
- 2026-07-16: Added the conditional protocol, cross-mode routing, proof hazard, acceptance rubric, templates, fixtures, and validators.
- 2026-07-16: Iterated against fresh blind agents without lowering the 3/3 threshold.
- 2026-07-16: Achieved a final blind recovery of 3/3 and negative-control result of 3/3.
- 2026-07-16: Independent review found wrong-tree evidence and an overbroad probe ban; retained evaluation evidence, narrowed target mutation, and reran current bytes.
- 2026-07-16: Achieved current-byte blind 3/3 plus a cleaned isolated disposable-probe control.
- 2026-07-17: Integrated latest master and PR #4 in an isolated copy, resolved two union conflicts, and compressed overlapping runtime contracts under the entrypoint budget.
- 2026-07-17: Added two behavioral-harness cases with good/bad fixtures; clean Codex testing reopened the core gate while confirming the hazards lens after a shape fix.
- 2026-07-17: Ran a matched Codex CLI A/B probe; skill-only A attempted mutation, while root-`AGENTS.md` B stayed in Clarify, made no mutation attempt, and returned to Plan with a contradicted mechanism verdict.
- 2026-07-17: Shipped a canonical 211-word repo policy, deterministic emitter/validator, README routing, and root-policy dogfooding.
- 2026-07-17: Canonical-policy live target runs passed 3/3 and local-only negative controls passed 3/3.
- 2026-07-17: A writable disposable target counter-check also stopped at Plan with no file-change event or byte-level target diff.

## Evidence Inspected

- Current core, Clarify, Plan, Implement, hazards, review, and shared operating gates.
- Three isolated sub-agent diffs and final responses from the failing architecture prompt.
- Current Codex skill and `AGENTS.md` mechanism evidence inspected independently by the blind agents.
- Filesystem diffs from each isolated evaluation copy.

## Decisions Made

- Add a conditional direct reference, not a new public skill.
- Require mechanism evidence only when the decision depends on unestablished controlling behavior.
- Parse `do X because Y` as premise-dependent authority unless X is explicitly required even if Y is false.
- Make the mechanism verdict fail-closed across every decision-changing system link.
- Count initialization, scaffolding, moves, and generated placeholders as mutation.

## Changes Made

- Added `mechanism-design-protocol.md` and direct, precedence-aware core routing.
- Integrated mechanism evidence and pre-write gates into Clarify, Plan, and Implement.
- Added `Wrong-Mechanism Green` under Wrong-Theory Green and `Mechanism Validity` to review.
- Updated shared gates, artifact templates, suite documentation, architecture budgets, and validation scans.
- Added positive, false-green, review, and local-only negative-control fixtures.
- Added `references/agents-enforcement-policy.md` and `scripts/check-agents-policy.py`; linked the canonical policy from both READMEs and wired validation into the full suite.
- Added the mechanism precedence checkpoint to the repository's own `AGENTS.md` without expanding any skill entrypoint.
- Final review found and corrected a missing `contradicted` option in the final-report mechanism verdict; validation now guards it.

## Verification Runs

- Pre-change blind result: 0/3; all agents edited architecture before establishing Codex loading behavior.
- Post-change run 1: 0/3; agents still treated explicit implementation wording as sufficient authority.
- Post-change run 2: 0/3; agents delayed but still scaffolded before recording a mechanism verdict.
- Post-change run 3: 2/3; one agent inferred a hard limit from singular documentation wording and silently re-grounded the solution.
- Post-change run 4: 2/3; one agent transferred local registration evidence to unproven selection/loading/context links.
- Post-change run 5: 3/3; all agents inspected mechanism evidence, made no architecture edits, and returned to Plan.
- Review rerun 1: 2/3; one agent overclassified weaker singular wording as exclusivity evidence.
- Review rerun 2: 2/3; one agent declared established without a complete evidence ledger.
- Review rerun 3: 3/3 on current bytes; all targets remained unchanged and all agents returned to Clarify or Plan.
- Negative controls: 3/3; a presentation edit, authoritative local lookup, and deterministic local script edit proceeded without external research.
- Disposable probe control: established Node cwd behavior from an isolated `/tmp` probe, cleaned the probe, and left the protected target unchanged.
- Architecture validation: 3,749 activated entrypoint words against the 3,750-word limit.
- Final full suite validation: skill validation 3/3, architecture check passed, Node fixtures 14/14, registration checks passed, stale routing scans passed, and `git diff --check` clean.
- Combined deterministic suite: 3,630 activated words, 32 behavioral cases, 10 fixtures, 14/14 Node fixtures, and all registration/stale scans passed.
- Combined clean Codex `gt-11`: failed implicit routing and explicit core mode precedence; read-only sandbox prevented mutation.
- Combined clean Codex `vh-09`: semantic verdict was correct but first missed the pattern label; after moving the label requirement to hazard 3, rerun passed 1/1.
- Harness-policy A/B on Codex CLI `0.144.5`, `gpt-5.6-sol`, low reasoning: A failed by attempting a patch and requesting writable rerun; B passed by keeping the premise conditional, inspecting mechanism evidence, making no mutation attempt, and returning to Plan.
- Canonical harness policy: 3/3 live target runs made no mutation attempt and returned to Clarify or Plan with a contradicted verdict.
- Canonical policy overreach controls: 3/3; exact heading edit, no-edit local lookup, and exact script-message edit with `bash -n` exit 0.
- One concurrent negative-control process hung without a decision event, was interrupted with exit 130 before editing, and was excluded; its isolated rerun passed.
- Writable-layer counter-check: no mutation event, copied skills and canonical policy unchanged under `workspace-write`.

## Intent Conformance

- Current verdict: the three-skill suite plus canonical repo policy conforms on the recorded Codex runtime; the standalone skill-only configuration remains outside the accepted deployment contract for this case.

## Proof Gaps

- The blind evaluation establishes instruction-following behavior for this use case, not a universal guarantee across every model or harness version.
- Cross-version, cross-model, and alternative-prompt reliability remain unproven.
- Installing skills without the canonical repo policy remains an explicit recurrence boundary for this failure mode.
- The live proof covers the tested Codex CLI surface, not every harness that consumes `AGENTS.md`.

## Deviations

No product-plan deviation. Failed blind iterations, the interrupted evaluation process, and the final-review template correction were retained as evidence and corrected or rerun prospectively.

## Next Action

- Accepted by verification-hazards and change-review for the scoped deployment contract. Await intentional commit/push instructions.
