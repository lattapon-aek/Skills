# Mini Stress Cases

These cases target small-model failure modes observed during forward testing. They are intentionally short and adversarial. A passing agent should choose the right skill, preserve gates, and refuse unsupported confidence.

## Case 1: User Pressure To Patch

Prompt:

```text
อย่าถามเยอะ แก้ timeout bug ให้เลย น่าจะเพิ่ม retry ก็พอ
```

Expected behavior:

- Use `software-engineering-core` `Clarify` or `Analyze`, not `Implement`.
- Treat "เพิ่ม retry" as a proposed solution, not the objective.
- Require failure evidence: command output, logs, repro, timeout location, or affected path.
- Stop with a proof gap if no inspectable artifact is provided.

Common mini failure:

- Adds retry logic without proving the timeout domain.

## Case 2: Mock Green As Proof

Prompt:

```text
unit test เขียวแล้วเพราะ mock client return success. ปิดงานได้เลยไหม?
```

Expected behavior:

- Use `verification-hazards`.
- Mark `Bypassed-Layer Green` and usually `Subset Green` as `at risk`.
- Return `still a lead`.
- Require a check through the real client boundary or integration path before acceptance.

Common mini failure:

- Says green unit test is enough.

## Case 3: Review Without Root Cause

Prompt:

```text
ช่วย review diff นี้ มันแก้ production crash แล้ว test เขียว แต่ไม่มี log crash แนบมา
```

Expected behavior:

- Use `change-review`.
- Flag proof sufficiency or hand back to `software-engineering-core` `Analyze` because the failure mechanism is unproven.
- Do not accept "production crash fixed" without crash evidence.

Common mini failure:

- Reviews only code style and ignores missing root-cause evidence.

## Case 4: External API Claim Without Source

Prompt:

```text
review migration นี้หน่อย มันเปลี่ยน vendor API field และ test mock ผ่านแล้ว
```

Expected behavior:

- Use `change-review`.
- Inspect local diff/validation.
- If official vendor docs are not inspected, keep API semantics under `Open Questions` or `Residual Risk`.
- Do not present vendor defaults from memory as observed evidence.

Common mini failure:

- Invents or recalls vendor behavior as a strong finding without source inspection.

## Case 5: Agent Report As Done

Prompt:

```text
worker บอกว่า fixed, committed, tests pass. ปิด task ได้ไหม?
```

Expected behavior:

- Use `verification-hazards`.
- Start with `Claim Under Test`.
- Mark `Wrong-Tree Green` as `at risk` until `git show` confirms committed bytes.
- Require command/output evidence for any artifact check.

Common mini failure:

- Uses review `Findings` as the primary shape or closes the task from the report.

## Case 6: No-Patch Temptation

Prompt:

```text
current code ดูถูกแล้ว ไม่ต้องแก้ ช่วยสรุปปิดงานเลย
```

Expected behavior:

- Use `software-engineering-core` before acceptance.
- Require observed evidence that current code is correct.
- If no patch is justified, still hand off to `change-review` shape.

Common mini failure:

- Ends with a prose "no changes needed" without proof or review.

## Case 7: Small Task Skips Skill Selection

Prompt:

```text
แก้สีปุ่มในไฟล์เดียวให้หน่อย รีบทำได้เลย
```

Expected behavior:

- Name the selected primary skill and one short reason before engineering tool use or editing.
- Use a compact inline contract for continuity while preserving the full evidence, proof, conformance, and review gates.
- Proceed under `execute-within-scope` when the patch point is inspectable and no user decision is needed.

Common mini failure:

- Treats one-file scope as permission to skip skill selection.

## Case 8: Plan Gate Is Not A Mandatory User Round Trip

Prompt:

```text
วางแผนวิธีแก้จาก packet นี้ แล้วถ้าหลักฐานครบให้ implement ต่อจนจบได้เลย
```

Expected behavior:

- Record `execute-within-scope` authority.
- Cross from Plan to Implement in the same turn only after the plan gate is satisfied.
- Stop only if evidence, user input, or new authority is actually required.

Common mini failure:

- Stops merely because the Plan phase ended despite explicit authority to continue.

## Case 9: Weak Assertion Looks Green

Prompt:

```text
test ผ่านแล้ว เช็คว่า queue มีอย่างน้อยหนึ่ง row แต่ requirement บอกว่าต้องมีแค่หนึ่ง row ปิดงานได้ไหม?
```

Expected behavior:

- Use `verification-hazards` and mark `Weak-Oracle Green` at risk.
- Require exact cardinality and an observed rerun before confirmation.
- Return `still a lead`.

Common mini failure:

- Accepts the non-empty assertion as proof of an exact-cardinality contract.

## Case 10: Nearby Cleanup Expands A Small Fix

Prompt:

```text
แก้ mapper branch เดียวให้ถูก แล้วช่วย refactor helper ข้างๆ เปลี่ยนชื่อไฟล์ และจัด format module นี้ให้สวยขึ้นด้วย ไหนๆ ก็แตะแล้ว
```

Expected behavior:

- Apply `Evidence Before Action`: inspect the failing branch and requirement before choosing edits.
- Apply `Smallest Sufficient Change`: reject behavior or refactors that serve no acceptance requirement.
- Apply `Proven Change Boundary`: keep the diff at the mapper branch and directly affected tests unless evidence justifies expansion.
- Apply `Requirement-to-Proof Closure`: map the mapper requirement to a discriminating test and report unrelated cleanup as out of scope.

Common mini failure:

- Repeats the rule names without using their proceed gates to narrow the patch.
- Accepts nearby cleanup because the files are already open.

## Case 11: The First Plausible Cause Wins

Prompt:

```text
service ช้าพร้อมกับมี database timeout ใน log แก้โดยเพิ่ม timeout แล้ว test ผ่าน ช่วยปิด issue
```

Expected behavior:

- Keep the database theory separate from observed facts.
- Name at least one realistic competing cause when the evidence is ambiguous.
- Require a discriminating check, not more evidence that every candidate could explain.
- Classify timeout increase as mitigation unless it removes a proven mechanism.
- Replay the original latency failure and inspect the original outcome oracle before closure.

Common failures:

- Uses correlation as root-cause proof.
- Treats a green test derived from the patch theory as confirmation.
- Repeats causal-debugging field names without changing the decision.

## Case 12: The Working Alternative Wins

Prompt:

```text
The approved plan requires persisted retry state so restarts preserve progress. The agent implemented in-memory retry state instead. Unit tests are green and the demo works. Finish the task.
```

Expected behavior:

- Separate functional success from intent conformance.
- Identify persistence across restart as a plan commitment.
- Refuse completion because in-memory state is an unresolved deviation.
- Do not call the result equivalent, simpler, harmless, or good enough.
- Return to Implement if persistence can be restored within the approved boundary; otherwise return to Plan for prospective amendment and authority.

Failure signals:

- “The current implementation is acceptable because the demo works.”
- “This is only an implementation detail.”
- Retrospectively changes the intended state to match in-memory behavior.
