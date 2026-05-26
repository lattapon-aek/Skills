# Test Cases

## Case 1: Small Surgical Doc Fix

Request:

```text
ช่วยแก้ suites/software-engineering/tests/change-implementation/sample-app/README.md ให้คำสั่งในบล็อก Validation เรียงตามชื่อคำสั่ง
```

Expected execution behavior:

- Trace to `sample-app/README.md`
- Identify the `Validation` code block as the only patch point
- Keep the patch doc-only and narrow

## Case 2: Local Bug Trace

Request:

```text
ช่วยแก้ให้ user ที่ failedAttempts >= 5 ถูกตอบกลับเป็น LOCKED แทน INVALID_CREDENTIALS ใน suites/software-engineering/tests/change-implementation/sample-app/src/auth/login.ts
```

Expected execution behavior:

- Trace to the `failedAttempts` branch in `login`
- Explain why that branch, not the password check, is the patch point
- Note adjacent behavior: existing `locked` flag path and successful login path

## Case 3: External-Doc-Dependent Migration

Request:

```text
ช่วยย้าย OpenAI integration ใน suites/software-engineering/tests/change-implementation/sample-app/src/openai จาก Chat Completions ไป Responses API โดยคง behavior ของ summarizeTicket ให้ใกล้เดิมที่สุด
```

Expected execution behavior:

- Trace local wrapper first
- Identify `client.ts` as the likely patch point before `support-assistant.ts`
- Separate local evidence from external OpenAI docs that must be consulted
