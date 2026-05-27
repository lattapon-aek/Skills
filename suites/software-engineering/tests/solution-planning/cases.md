# Test Cases

## Case 1: Integration Choice

Request:

```text
ช่วยวางแผนว่าจะย้าย OpenAI integration ใน suite นี้ไป Responses API ยังไงดี ตอนนี้ objective ชัดแล้วว่าอยากลดการพึ่ง Chat Completions แต่ยังไม่ควรแก้ code ทันที ช่วยเปรียบเทียบ option ที่สมจริงแล้วแนะนำแนวทางเดียวพร้อมขอบเขตการ implement
```

Expected planning behavior:

- frame the actual decision instead of jumping into edits
- inspect the local wrapper layer first
- consider only realistic options
- recommend one path
- define execution boundaries and proof strategy

## Case 2: Migration Sequencing

Request:

```text
ช่วยวางแผนการแยก payment retry status logic ออกจาก dashboard-specific interpretation หน่อย ตอนนี้ยังไม่แน่ใจว่าควรแยก module ก่อนหรือค่อยทำตอน refactor ใหญ่ ช่วยออกแบบทางเลือกที่สมจริงและแนะนำ path ที่ปลอดภัยกว่า
```

Expected planning behavior:

- keep the focus on the architectural decision
- compare a small number of options
- surface migration and blast-radius tradeoffs
- recommend one path and explain why larger alternatives are ruled out
