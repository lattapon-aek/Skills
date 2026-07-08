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
