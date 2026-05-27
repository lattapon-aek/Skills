# Orchestration Cases

## Case 1: Incident-Driven Fix

Request:

```text
ช่วยแก้ปัญหา payment status ให้หน่อย ตอนนี้ dashboard โชว์ failed ทั้งที่ provider capture สำเร็จ ผมมี incident bundle อยู่ที่ suites/software-engineering/tests/skill-flow/sample-app/incidents/payment-retry และโค้ดที่เกี่ยวข้องน่าจะอยู่แถว suites/software-engineering/tests/skill-flow/sample-app/src/payments อยากได้ fix ที่แคบที่สุด แต่ต้องพิสูจน์ให้ได้ว่าปัญหาหายจริง แล้วช่วย review งานตัวเองปิดท้ายด้วย
```

Expected flow:

- `task-intake`
- `root-cause-analysis`
- `change-implementation`
- `change-review`

## Case 2: Design-Then-Implement

Request:

```text
ช่วยวางแผนว่าจะย้าย OpenAI integration ใน suite นี้ไป Responses API ยังไงดี ตอนนี้ objective ชัดแล้วว่าอยากลดการพึ่ง Chat Completions แต่ยังไม่ควรแก้ code ทันที สุดท้ายถ้าเลือกแนวทางได้แล้วค่อย implement และ review ปิดท้าย
```

Suggested local evidence:

- `suites/software-engineering/tests/change-implementation/sample-app/src/openai/client.ts`
- `suites/software-engineering/tests/change-implementation/sample-app/src/openai/support-assistant.ts`
- `suites/software-engineering/tests/change-implementation/sample-app/src/openai/support-assistant.test.ts`

Suggested review proof:

- `suites/software-engineering/tests/change-review/scenario-3/proposed.diff`
- `suites/software-engineering/tests/change-review/scenario-3/validation.txt`

Expected flow:

- `task-intake`
- `solution-planning`
- `change-implementation`
- `change-review`

Suggested final review shape:

- `Findings`
- `Open Questions`
- `Ruled-out Concerns`
- `Residual Risk`
