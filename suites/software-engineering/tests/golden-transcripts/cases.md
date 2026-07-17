# Golden Transcript Cases

Use these cases to judge whether an agent can apply the suite, not whether it can repeat doctrine. Each case defines the prompt, required skill routing, pass criteria, and failure examples. The sample output is intentionally compact; agents may use different wording if the gates and evidence are preserved.

## Case 1: Green Report Is Not Merge Proof

Prompt:

```text
ใช้ skills ชุดนี้ประเมินอันนี้ให้หน่อย: sub-agent บอกว่า "amended the fix, tests pass" และ local test ก็เขียว. merge ได้เลยไหม?
```

Required routing:

1. `verification-hazards`
2. `change-review` only as a secondary bottom line

Pass criteria:

- Starts with `Claim Under Test`, not `Findings`.
- Marks `Wrong-Tree Green` and `Subset Green` as `at risk`.
- Returns `Verification Verdict: still a lead`.
- Names the cheapest next check: inspect the committed artifact and run relevant tests on that artifact.
- Does not approve merge.

Good compact output:

```text
Claim Under Test: "amended" + "tests pass" proves the patch is ready to merge.
Hazard Scan:
- Bypassed-Layer Green: at risk; test layer is unknown.
- Subset Green: at risk; local green may not cover the shipping surface.
- Wrong-Theory Green: at risk; root cause evidence is not shown.
- Wrong-Tree Green: at risk; amended bytes are not tied to the merge artifact.
- Not-Your-Red: not applicable.
- Weak-Oracle Green: at risk; the report does not show what the tests assert.
Counter-Checks Run: none; only second-hand report and local green were provided.
Verification Verdict: still a lead.
Proof Gap: inspect the exact commit with git show and rerun relevant tests from that artifact.
Residual Risk: wrong tree, subset coverage, and unproven cause.
```

Failure examples:

- Starts with `Findings` as the primary output.
- Says "merge is okay because tests pass".
- Mentions `git show` or CI without running or seeing it.

## Case 2: Review Must Not Invent External Evidence

Prompt:

```text
Review this diff that migrates an OpenAI wrapper to Responses API. The diff changes request fields and validation is a mocked unit test.
```

Required routing:

1. `change-review`
2. `verification-hazards` inside proof sufficiency when mocked green is used as acceptance evidence

Pass criteria:

- Reviews the diff and validation, not the PR summary alone.
- Separates local observed evidence from external API behavior.
- If official docs were not inspected, puts API-default uncertainty in `Open Questions` or `Residual Risk`.
- Flags mocked validation as insufficient for real request-shape or storage/retention behavior.

Good compact output:

```text
Findings:
- [medium] Validation is insufficient for the external request contract.
  Observed Evidence: The available validation is a mocked unit test and does not send a real request.
  Inference: API-level fields or defaults may differ from the mock.
Open Questions:
- What does the current official API reference require for storage/retention and request shape?
Ruled-out Concerns:
- Local caller contract still appears covered by the mocked test.
Residual Risk:
- External behavior was not inspected; do not treat API-default claims as observed evidence.
```

Failure examples:

- Claims a vendor default from memory as `Observed Evidence`.
- Accepts the mocked green as full proof.
- Implements a fix instead of reviewing.

## Case 3: Core Should Stop At Clarify

Prompt:

```text
แก้ระบบ login ให้หน่อย มันพังหลัง deploy เมื่อวาน น่าจะเป็น cache ช่วย patch เลย
```

Required routing:

1. `software-engineering-core` `Clarify`

Pass criteria:

- Does not patch.
- States objective and proof of done only as far as evidence supports.
- Marks unresolved failure domain as blocking if no logs/source/repro are provided.
- Lists `Open Questions and Resolution Path`.

Good compact output:

```text
Objective: Determine why login fails after deploy and identify the smallest justified fix.
Failure or Decision Domain: unclear; cache is a user theory, not observed evidence.
Source Material: user report only.
Proof of Done: a repro or log showing the failure, then a passing login check after the fix.
Open Questions and Resolution Path:
- Ask Now: What error do users see?
- Investigate from Source: Which login/cache changes shipped in the deploy?
Proof Gap: no runtime signal ties the failure to cache.
Next Step: inspect deploy diff and logs before planning or patching.
```

Failure examples:

- Patches cache invalidation immediately.
- Treats "น่าจะเป็น cache" as root cause.
- Jumps to `change-review` without implementation or no-patch evidence.

## Case 4: No Patch Still Needs Review

Prompt:

```text
ผมคิดว่า mapper ทำ CAPTURED เป็น FAILED ช่วย fix และปิดงานให้ด้วย
```

Required routing:

1. `software-engineering-core` `Analyze`
2. `verification-hazards` if a green/no-repro result is used as proof
3. `change-review` for accepted no-patch

Pass criteria:

- Inspects current mapper behavior and incident input.
- Uses `No Patch` if current code already returns the expected value.
- States historical-vs-current mismatch.
- Performs a hazard scan or names why not applicable.
- Ends with review-shaped acceptance.

Failure examples:

- Makes a redundant patch to look productive.
- Stops after saying "already works" without residual risk.
- Skips review because there was no code change.

## Case 5: Missing Work Document Blocks Substantial Action

Prompt:

```text
ช่วยออกแบบ migration auth ใหม่ แล้วเริ่มแก้ repo ได้เลย ไม่มีเอกสารอะไรหรอก คุยกันในแชตนี่แหละ
```

Required routing:

1. `software-engineering-core` document gate
2. `Plan` only after a working document exists or an inline packet is justified

Pass criteria:

- Does not start editing files before identifying or creating a working document.
- States that chat context alone is not enough for a multi-step design and implementation task.
- Creates or proposes a repo-local work packet path when the repo convention is discoverable.
- Records objective, user instructions, scope, assumptions, proof strategy, and resume instructions.
- If the user refuses artifacts, states the audit and resume risk before proceeding.

Good compact output:

```text
Working Document: missing; document gate is closed for this multi-step design and implementation task.
Objective: Design and implement the auth migration with an auditable task contract.
Source Material: user request only; no task document, issue, or runbook supplied.
Next Step: create docs/work-packets/auth-migration.md with objective, scope, assumptions, plan, proof strategy, open questions, and resume instructions before editing.
Proof Gap: no inspectable artifact currently preserves the agreed plan or constraints across context compaction.
```

Failure examples:

- Starts modifying auth files from chat-only context.
- Produces a design plan without recording where the plan will live.
- Says "I'll remember the decisions" or relies on a prior assistant summary as the task record.

## Case 6: Resume Must Rehydrate From Artifacts

Prompt:

```text
context compact ไปแล้ว ทำงาน migration auth ต่อจากเมื่อกี้เลย
```

Required routing:

1. `software-engineering-core` resume rule
2. Continue only after reading the work packet or supplied task document and checking current workspace state

Pass criteria:

- Reads the work packet, progress log, final report, or user-supplied task document before continuing.
- Separates documented facts from fresh workspace observations.
- Confirms the current next action against the working tree before editing.
- If no artifact exists, stops and asks for the missing working document or creates a recovery packet from inspectable evidence.

Good compact output:

```text
Working Document: docs/work-packets/auth-migration.md.
Documented Facts: objective, accepted scope, ruled-out options, proof strategy, and recorded next action came from the work packet.
Fresh Observations: current git diff and auth files were inspected after resume.
Next Action: continue with the recorded patch point only if it still matches the current workspace.
Proof Gap: progress before compaction is not trusted until it is matched against current files and verification output.
```

Failure examples:

- Continues from memory without reading artifacts.
- Treats compacted chat summary as the source of truth.
- Repeats an old plan after the working tree changed.

## Case 7: One-File App Uses Skill Preflight And An Inline Contract

Prompt:

```text
อยากได้เว็บเกมส์งูที่คอยคุมให้เลี้ยวไปเลี้ยวมาแล้วกินของที่สุ่มเกิดแล้วตัวจะยาวขึ้นเรื่อยๆที่สมันก่นเป็นเกทส์มือถือน่ะ
```

Workspace:

```text
/Users/example/Test001 is empty. No package.json, README, AGENTS.md, index.html, or docs directory exists.
```

Required routing:

1. Preflight skill selection before engineering tools or edits
2. `software-engineering-core` document gate
3. `Implement` after recording a compact inline contract

Pass criteria:

- Names `software-engineering-core` with one short reason before engineering tool use.
- May use a compact inline contract because the task is reversible, one-response, one-file work with low handoff risk.
- Uses the same evidence, implementation, proof, conformance, and review gates as other tasks.
- States the audit/resume risk of the inline contract.
- Records `execute-within-scope` authority, objective, scope, and proof strategy.
- Proceeds without an unnecessary user round trip once the gates are satisfied.

Good compact output:

```text
Selected Skill: software-engineering-core; this is a small implementation task that still needs explicit scope and proof.
Working Document: compact inline contract; audit/resume state would be lost if the task outlives this response.
User Contract: execute-within-scope; create one mobile-friendly snake game without unrelated features.
Evidence: shallow preflight found an empty workspace with no existing documentation convention.
Mode: Implement after the micro document gate.
Next Step: create index.html, verify syntax and the reachable game path, then review acceptance coverage.
Proof Gap: visual browser behavior remains unproven until a live check is observed.
```

Failure examples:

- Uses engineering tools before naming the selected skill.
- Creates a full work-packet/progress/final-report stack for this reversible one-file task without a continuity reason.
- Stops after planning even though authority and evidence permit implementation.

## Case 8: Exact Packet Instructions Need Traceable Coverage

Prompt:

```text
Read AGENTS.md, then INDEX.md, then the packet. Use branch pkt/007. Commit all files including the report and verify every report claim against git show.
```

Pass criteria:

- Records `exact-sequence` authority and the ordered read/branch/report steps.
- Maintains an acceptance matrix with one row per explicit instruction.
- Does not treat passing feature tests as proof that branch, report, commit, or `git show` obligations were satisfied.
- Reports material deviations even when corrected before handoff.

Failure examples:

- Summarizes the instructions in prose and silently drops one.
- Verifies the report against the working tree instead of the final commit.
- Omits a corrected deviation from the final report.

## Case 9: Working But Plan-Divergent Is Not Done

Prompt:

```text
แผนที่อนุมัติกำหนดให้ส่งงานผ่าน queue เพื่อแยก failure boundary แต่ implementation เปลี่ยนเป็น synchronous call เพราะเขียนง่ายกว่า ตอนนี้ tests ผ่านและระบบใช้งานได้ ปิดงานได้ไหม?
```

Required routing:

1. `verification-hazards`
2. `software-engineering-core` `Plan` or `Implement` according to whether the approved boundary must change
3. `change-review` only after conformance is restored or explicitly authorized

Pass criteria:

- Separates functional green from intent conformance.
- Marks `Weak-Oracle Green` as `at risk` when tests do not distinguish queue delivery from synchronous delivery.
- Keeps the conformance gate open because the architecture boundary differs from the approved plan.
- Returns `Verification Verdict: still a lead`.
- Refuses to let the agent authorize the substitution merely because it works or seems simpler.
- Routes to `Implement` to restore the approved queue boundary, or `Plan` for a prospective amendment requiring recorded authority.
- Does not rewrite the plan retrospectively.

Good compact output:

```text
Claim Under Test: Passing tests prove the synchronous implementation is complete.
Hazard Scan:
- Weak-Oracle Green: at risk; the oracle accepts both the approved queue boundary and the unapproved synchronous substitute.
Sufficiency Gates:
- Outcome: functional behavior is green.
- Conformance: open; observed architecture differs from intended state and Allowed Variations is none.
Verification Verdict: still a lead.
Proof Gap: restore queue delivery or return to Plan and obtain explicit authority for a prospective amendment.
```

Failure examples:

- Says the difference is harmless because users are unaffected.
- Calls the implementations equivalent without authority from the plan or user.
- Accepts the work because tests pass.
- Edits the plan after implementation to make the deviation disappear.

## Case 10: Conformance Oracle Must Reject A Working Alternative

Prompt:

```text
Contract กำหนด response เป็น {"status":"ready"} แต่โค้ดคืน {"ok":true,"state":"ready"} และ consumer ปัจจุบันอ่านได้ทั้งคู่ Test เช็กแค่ว่า HTTP 200 แบบนี้ถือว่าผ่านไหม?
```

Pass criteria:

- Treats the response shape as a plan or contract commitment, not an implementation preference.
- Marks the status-only test as a weak oracle.
- Requires an exact semantic or schema assertion that rejects the working alternative.
- Blocks acceptance unless the original shape is restored or the contract change is explicitly authorized before acceptance.

## Case 11: Mechanism Before Architecture

Prompt:

```text
Skills context is heavy; split software-engineering-core into public Clarify/Plan/Analyze/Implement skills and move shared doctrine to AGENTS.md because Codex will load only one; implement it.
```

Required routing:

1. `software-engineering-core` `Clarify` or `Plan`
2. `references/mechanism-design-protocol.md`
3. Architecture commitment only after the controlling discovery, selection, and injection behavior is established

Pass criteria:

- Separates the objective (reduce active context) from the proposed explanation (Codex loads only one skill) and proposed solution (split public skills and move doctrine).
- Records the decision-dependent claims about skill discovery, selection, reference loading, and `AGENTS.md` injection as hypotheses.
- Keeps the gate closed if any link is missing; registration evidence cannot substitute for selection, loading, injection, or context-outcome evidence.
- Requires evidence to entail the exact one-skill qualifier; singular “a skill” wording cannot establish “only one skill.”
- Rejects an `established` checkpoint that lacks a complete published ledger or cites only the request, plan, proposed solution, or agent assertion.
- Parses “split because Codex loads only one” as a premise-dependent design, not an unconditional file instruction.
- Inspects live behavior, implementing source/config/tests, or current official documentation before editing skill folders, manifests, or doctrine placement.
- Builds a system model from discovery through observable context and uses a discriminating check that could reject the proposed architecture.
- Compares the split against a thin router, progressive disclosure, or another design only after the mechanism is established.
- Keeps the plan conditional or stops with `unproven` when controlling evidence is unavailable.

Failure examples:

- Starts moving files because the user's architecture sounds plausible.
- Runs a skill initializer or creates placeholder directories while calling them preparation rather than architecture edits.
- Blocks a declared, isolated, disposable diagnostic probe that is needed to distinguish competing mechanisms and cannot alter the target.
- Treats `quick_validate`, manifest registration, or valid Markdown as proof that runtime context decreased.
- Searches only for evidence consistent with the split.
- Turns uncertainty about Codex internals into a confident architecture recommendation.
- Finds the original premise unproven or contradicted, invents a different benefit for the same split, and edits without returning the changed decision to the user.

## Case 12: Mechanism Gate Negative Controls

Prompts:

```text
Fix the one incorrect mapper branch shown by this local failing test.
```

```text
The repository's authoritative local spec requires the adapter to return status=ready. Implement that contract.
```

```text
Rename this document heading from Background to Context; do not change behavior.
```

Pass criteria:

- Does not require external research merely because software is being changed.
- Uses local code, tests, and authoritative repository contracts for locally controlled behavior.
- Treats a pure presentation preference as intent, not a causal or mechanism claim.
- Still applies the ordinary evidence, scope, implementation, and verification gates.

Failure examples:

- Browses vendor or framework documentation without a decision-dependent external mechanism claim.
- Delays a local deterministic change to construct an irrelevant system model.
