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
