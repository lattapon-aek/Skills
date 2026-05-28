# Test Cases

## Case 1: Reproduce Before Claiming Root Cause

Request:

```text
ช่วยใช้ software-engineering-core ในโหมด analyze ดู suites/software-engineering/tests/software-engineering-core/analysis/sample-app/src/auth/login.ts ให้หน่อย มีคนรายงานว่า user ที่ failedAttempts >= 5 ได้ INVALID_CREDENTIALS แทน LOCKED อย่าเพิ่งรีบแก้ ขอให้หา root cause ให้ชัดก่อน
```

Expected debugging behavior:

- Treat the report as a lead, not proof
- State a reproduction or simulation path
- Trace to the `failedAttempts` branch in `login`
- Explain why that branch is the fault location rather than the password mismatch branch
- Refuse to call the bug fixed before the failing behavior is proven to disappear

## Case 2: Simulate The Reported Failure

Request:

```text
ช่วยใช้ software-engineering-core ในโหมด analyze หา root cause ใน suites/software-engineering/tests/software-engineering-core/analysis/sample-app/src/orders/status-summary.ts มี report ว่า dashboard นับ active orders เกินจริง อย่าเดา ช่วย simulate เคสเล็กๆ แล้วชี้ให้ได้ว่าปัญหาเริ่มตรงไหน
```

Expected debugging behavior:

- Build or describe a minimal simulation case from the code
- Separate the reported symptom from direct evidence
- Trace to the exact filter condition that misclassifies orders
- Explain why nearby formatting or aggregation logic is not the root cause
- State what would need to be verified after the fix

## Case 3: Rule Out A Misleading Signal

Request:

```text
ช่วยใช้ software-engineering-core ในโหมด analyze หา root cause ใน suites/software-engineering/tests/software-engineering-core/analysis/sample-app/src/billing/invoice-total.ts มี report ว่า invoice บางใบรวมยอดผิด แล้วทีมบอกว่าน่าจะเป็น rounding bug เพราะ log ชอบออกมาเป็นทศนิยมแปลกๆ อย่าเชื่อ log อย่างเดียว ช่วย simulate เคสเล็กๆ แล้วพิสูจน์ให้ได้ว่าปัญหาเริ่มตรงไหน
```

Expected debugging behavior:

- Treat the rounding theory as a hypothesis, not a conclusion
- Build or describe a small invoice input that reproduces the mismatch
- Rule out pure formatting or display logic if the math is already wrong earlier
- Trace to the exact calculation step that introduces the wrong total
- Explain why the competing rounding hypothesis is weaker than the proven fault

## Case 4: Start From Incident Evidence

Request:

```text
ช่วยใช้ software-engineering-core ในโหมด analyze หา root cause ใน suites/software-engineering/tests/software-engineering-core/analysis/sample-app/incidents/payment-status มี incident log กับ payload จากจุดเกิดเหตุอยู่ อย่าข้ามไปเดาจากโค้ดอย่างเดียว ช่วยใช้หลักฐานพวกนี้ก่อนแล้วค่อย simulate เพื่อชี้ให้ได้ว่าปัญหาเริ่มตรงไหน
```

Expected debugging behavior:

- Surface `Incident Evidence` explicitly
- Start from the log and payload before code theories
- Use simulation to confirm or narrow the failing path
- Trace to the exact code branch that misclassifies the payment status
- Explain what in the incident bundle is a symptom and what is direct evidence

## Case 5: Distinguish Application Failure From Runtime / Tooling Failure

Request:

```text
ช่วยหา root cause ให้หน่อย ตอนนี้ระบบที่สั่ง agent ทำงานชอบค้าง เพราะ agent บางครั้ง `npm install` ไม่ผ่าน แล้วเหมือนมี background workers ค้างหลายตัวจน CPU เครื่องพุ่ง อย่าเพิ่ง assume ว่าบั๊กอยู่ในโค้ดแอป ช่วยแยกให้ชัดว่าปัญหาอยู่ใน application logic, dependency/tooling, sandbox/permissions, orchestration/process lifecycle, หรือ system resource pressure กันแน่
```

Expected debugging behavior:

- Classify the likely failure domains before picking a root cause
- Ask for or inspect process, runtime, command, and environment evidence instead of goingตรงไปที่ business code
- Treat sandbox, network, permission, retry, and cleanup behavior as first-class hypotheses
- Distinguish what is proven in the current workspace from what is only reported historically
- Refuse to claim an application-code root cause without evidence that the failure survives past the runtime/tooling boundary
- Use `suites/software-engineering/tests/software-engineering-core/analysis/artifacts/npm-sandbox-repro/package.json` as a minimal repro artifact when testing whether dependency install failures happen before application code ever runs
