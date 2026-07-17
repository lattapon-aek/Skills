# Final Report: Suite Readiness Improvements

## Objective

Close the reviewed gaps in current-policy behavioral evidence, Markdown portability, mutation-aware behavioral proof, and entrypoint budget headroom.

## Intended And Observed State

| Area | Intended State | Observed State | Status |
| --- | --- | --- | --- |
| Live behavioral evidence | 32 current cases under canonical policy | before and after runs completed 32/32 with zero missing | conforms |
| Markdown portability | no machine-specific local links | 29 local links resolve; 11 Windows paths replaced | conforms |
| Mutation oracle | explicit file changes cannot hide behind final prose | JSONL/stderr sidecars graded; good/bad event and rejected-patch controls discriminate | conforms |
| Context budget | practical headroom retained | 3,538/3,750 total; each entrypoint has at least 50 words headroom | conforms |

## Files Touched

- Validation: `scripts/validate-suite.sh`, `check-markdown-links.py`, `check-skill-architecture.py`
- Behavioral harness: runner, README, cases, event/stderr fixtures, assessment
- Portability: the two OpenAI full-flow READMEs
- Runtime entrypoint: concise `change-review/SKILL.md`
- Continuity: work packet and this report

## Decisions

- Keep live agent evaluation outside deterministic `validate-suite.sh`; it is slow and runtime-dependent.
- Preserve strict transcript assertions even where semantically sound answers miss literal output-contract wording.
- Treat `file_change` events and rejected patches as mutation attempts; do not infer all shell commands from text.
- Enforce budget headroom rather than relying on a one-time reduction.

## Verification

- Before run: 14/32 pass, 18 fail, 0 missing.
- After run: 14/32 pass, 18 fail, 0 missing; 32 JSONL and 32 stderr sidecars captured.
- Five forbidden-file-change cases: zero observed file-change or rejected-patch violations.
- `python3 suites/software-engineering/scripts/check-markdown-links.py`: 29 links pass.
- Broken-link negative control: exit 1 with the missing target identified.
- Event parser counter-check: final agent message extracted and `file_change` rejected.
- Behavioral self-test: 32 cases valid, 14 fixture transcripts graded after the final rejected-patch pair was added.
- `./scripts/validate-suite.sh`: passed, including three skill validations and 14/14 Node tests.
- `git diff --check`: passed.

## Behavioral Evidence

The total pass count stayed 14/32. Routing and unsupported-claim metrics improved in the single after run; shape and false-acceptance metrics worsened. Three cases flipped each direction. This is not sufficient to attribute behavioral change to the patch. The durable improvement is proof quality: the harness now records whether the agent attempted an explicit file change.

## Acceptance Coverage

| Commitment | Observed Result | Status | Evidence |
| --- | --- | --- | --- |
| Run current 32-case baseline first | completed before functional edits | conforms | 14/32 baseline report |
| Repair and guard local links | 11 repaired; validator added | conforms | 29-link pass plus negative control |
| Add tool-event oracle | JSONL/stderr parsing and discriminating fixtures | conforms | self-test and live 32-case sidecars |
| Restore budget headroom | review entrypoint 1,120 to 1,028 words; enforced minima | conforms | architecture check at 3,538 words |
| Preserve ownership and doctrine | three public skills and routing unchanged | conforms | quick validation and inspected diff |

## Conformance

Verdict: `conforms`.

No public skill, routing owner, output field, or mechanism gate was removed. The live matrix was run in the requested order, and unfavorable results were retained.

## Deviations

None observed.

## Proof Gaps And Residual Risk

- One run per condition cannot separate model variance from small doctrine effects.
- The event oracle recognizes Codex `file_change` events and denied patches, not every possible mutating shell command or provider schema.
- The full matrix has no per-case timeout; one case took roughly 2.5 minutes.
- Current-policy implicit routing remains weak overall at 3/10, despite being better than the before run's 2/10.

## Verification Hazards

- `Bypassed-Layer Green`: clear for the scoped claim; the matrix drove the actual Codex runtime and the checker/event parser ran directly. Arbitrary shell mutation remains outside the event oracle.
- `Subset Green`: at risk for generalization; only Codex CLI `0.144.5`, `gpt-5.6-sol`, low reasoning, and this policy surface were exercised.
- `Wrong-Theory Green`: clear; actual Codex JSONL shapes were probed before implementation and 32 live captures exercised the parser.
- `Wrong-Tree Green`: clear; validation and live runs used the current working tree reached by the installed skill symlinks. The acceptance target is the working tree, not `HEAD`.
- `Not-Your-Red`: not applicable; no deterministic red is attributed to this patch, and balanced behavioral flips are retained as variance rather than regressions.
- `Weak-Oracle Green`: clear for broken links and explicit file changes because negative controls fail. At risk for universal agent quality because transcript checks remain wording-sensitive.

Verification Verdict: `confirmed` for the four scoped readiness improvements; `still a lead` for general runtime readiness or cross-model behavior.

## Change Review

- Findings: none blocking in the scoped diff.
- Instruction Compliance: the requested sequence was followed; the before matrix preceded functional edits, no commit/push was performed, and unfavorable evidence remains recorded.
- Intent Conformance: `conforms`; all four intended outcomes are present without changing public skill ownership or routing.
- Mechanism Validity: `established` for local link resolution, Codex event capture, and word-budget enforcement on the inspected runtime.
- Deviations: none observed.
- Proof Gap: cross-model behavior, arbitrary shell mutation classification, repeated-sample stability, and per-case timeouts remain open but were not substituted for the scoped deliverables.
- Verdict: `accept`.

## Follow-Up State

The four requested readiness improvements are implemented. Future work should treat routing quality and per-case timeout support as separate planned changes rather than silently expanding this patch.
