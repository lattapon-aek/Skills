# OpenAI Responses Full Flow

Concrete end-to-end fixture for:

`software-engineering-core (Clarify -> Plan -> Implement) -> change-review`

## User Request

```text
ช่วยใช้ software-engineering-core วางแผนว่าจะย้าย OpenAI integration ใน suite นี้ไป Responses API ยังไงดี ตอนนี้ objective ชัดแล้วว่าอยากลดการพึ่ง Chat Completions แต่ยังไม่ควรแก้ code ทันที ถ้าได้แนวทางที่ชัดและปลอดภัยค่อย implement ต่อ แล้ว review งานปิดท้ายด้วย โดยของที่เกี่ยวข้องน่าจะอยู่แถว suites/software-engineering/tests/software-engineering-core/implementation/sample-app/src/openai
```

## Intake / Planning Artifacts

- implementation seam:
  - [client.ts](C:/Users/lattapon.kea/Desktop/Agents%20Skills/suites/software-engineering/tests/software-engineering-core/implementation/sample-app/src/openai/client.ts)
  - [support-assistant.ts](C:/Users/lattapon.kea/Desktop/Agents%20Skills/suites/software-engineering/tests/software-engineering-core/implementation/sample-app/src/openai/support-assistant.ts)
- focused proof target:
  - [support-assistant.test.ts](C:/Users/lattapon.kea/Desktop/Agents%20Skills/suites/software-engineering/tests/software-engineering-core/implementation/sample-app/src/openai/support-assistant.test.ts)
- planning prompts:
  - [planning/cases.md](C:/Users/lattapon.kea/Desktop/Agents%20Skills/suites/software-engineering/tests/software-engineering-core/planning/cases.md)

## Implementation Proof

Run:

```powershell
node --test suites/software-engineering/tests/software-engineering-core/implementation/sample-app/src/openai/support-assistant.test.ts
```

Expected result:

- `pass 1`
- `fail 0`

## Final Review Artifacts

- review intent:
  - [pull-request.md](C:/Users/lattapon.kea/Desktop/Agents%20Skills/suites/software-engineering/tests/change-review/scenario-3/pull-request.md)
- review diff:
  - [proposed.diff](C:/Users/lattapon.kea/Desktop/Agents%20Skills/suites/software-engineering/tests/change-review/scenario-3/proposed.diff)
- surrounding base files:
  - [base/src/openai/client.ts](C:/Users/lattapon.kea/Desktop/Agents%20Skills/suites/software-engineering/tests/change-review/scenario-3/base/src/openai/client.ts)
  - [base/src/openai/support-assistant.ts](C:/Users/lattapon.kea/Desktop/Agents%20Skills/suites/software-engineering/tests/change-review/scenario-3/base/src/openai/support-assistant.ts)
  - [base/src/openai/support-assistant.test.ts](C:/Users/lattapon.kea/Desktop/Agents%20Skills/suites/software-engineering/tests/change-review/scenario-3/base/src/openai/support-assistant.test.ts)
- claimed validation:
  - [validation.txt](C:/Users/lattapon.kea/Desktop/Agents%20Skills/suites/software-engineering/tests/change-review/scenario-3/validation.txt)

## What This Flow Should Prove

- intake can identify the local seam without drifting into implementation
- planning recommends one migration path instead of brainstorming
- implementation stays at the wrapper seam and preserves caller behavior
- final output still ends in a `change-review`-shaped report, not just an implementation summary
