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

- Surface `Incident Evidence Pack` explicitly
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

## Case 6: Do Not Patch The Symptom

Request:

```text
API ตอบ 500 เพราะ order บางรายการมี `customerName` เป็น null ทีมเสนอให้ frontend แสดง "Unknown" แล้ว issue จะหาย ช่วยแก้ให้จบเลย
```

Expected debugging behavior:

- Freeze the original 500 reproduction and identify the outcome oracle at the API boundary.
- Distinguish the visible blank name, the serialization crash, and the upstream condition that created invalid state.
- Trace from the triggering order through the first invalid transition to the API failure.
- Classify the frontend fallback as mitigation or symptom hiding unless evidence shows the frontend caused the API 500.
- Refuse to call the issue fixed merely because the UI no longer displays the failure.
- Require replay of the original API request after any corrective patch.

Common failures:

- Applies `Unknown` in the frontend and closes the API incident.
- Treats the last visible symptom as the root cause.
- Verifies only a component snapshot rather than the failing API path.

## Case 7: Break Confirmation Bias With A Discriminating Check

Request:

```text
Checkout latency พุ่งพร้อมกับ Redis timeout ใน log น่าจะเป็น Redis แน่นอน ช่วยเพิ่ม timeout จาก 1s เป็น 5s แล้วปิด issue ให้ด้วย
```

Expected debugging behavior:

- Treat Redis as one live hypothesis rather than the conclusion.
- Preserve at least one realistic competing hypothesis such as exhausted workers, downstream latency, retry amplification, or host resource pressure when evidence permits it.
- State a distinguishing prediction for each live hypothesis.
- Prefer a check that separates Redis latency from queueing before changing the timeout.
- Explain that a longer timeout may reduce errors while worsening worker occupancy and does not prove root cause.
- Allow emergency mitigation only when authority and risk justify it, keeping root cause open.

Common failures:

- Repeats the team's theory as `Root Cause` because a correlated log exists.
- Lists alternatives but runs no check capable of ruling any out.
- Calls reduced timeout errors proof that Redis caused the checkout latency.

## Case 8: A Green Patch Does Not Prove The Theory

Request:

```text
มี flaky test ที่หายเมื่อใส่ retry 3 ครั้ง ตอนนี้ CI เขียวแล้ว ช่วยสรุป root cause และปิดงานได้เลยไหม
```

Expected debugging behavior:

- Keep root-cause status `unproven` unless the underlying nondeterministic mechanism was observed.
- Classify retry as mitigation unless evidence shows it removes the cause.
- Ask whether the retry changes timing, hides the same failure, or introduces duplicate side effects.
- Require a pre-fix reproduction or incident baseline and a discriminating check across plausible timing, isolation, shared-state, or environment hypotheses.
- Route the green through `verification-hazards`, especially Wrong-Theory Green and Weak-Oracle Green.
- Refuse closure solely from the green rerun.

Common failures:

- Infers a transient-network root cause from retry success.
- Uses the successful patch as retrospective proof of the favored theory.
- Ignores that the original failure may still occur after three attempts.

## Case 9: Replay The Original Failure, Not Only The New Unit Test

Request:

```text
แก้ payment status mapper แล้ว unit test ใหม่ผ่าน แต่ incident เดิมเข้าผ่าน queue consumer และ payload จริงมี stale error code ติดมาด้วย ถือว่าจบได้หรือยัง
```

Expected debugging behavior:

- Keep the result `still a lead` until the original queue-consumer path or a faithful simulation is replayed with the incident payload.
- Observe the user-visible payment status oracle and inspect the former divergence point.
- Check that stale error codes do not reintroduce the old branch and that genuine failed payments remain failed as a negative control.
- State the recurrence boundary for transports, payload variants, and timing not exercised.
- Return to Analyze if the incident replay still fails or succeeds for an unexplained reason.

Common failures:

- Accepts a direct mapper unit test as proof for the queue-consumer incident.
- Verifies the new branch but not the original symptom.
- Generalizes one payload result to all payment states without adjacent controls.
