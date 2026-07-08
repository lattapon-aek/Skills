# Internet-Derived Cases

These cases are derived from public incident reports and official writeups. Use them to test whether the skill suite generalizes beyond local fixtures. Each case intentionally gives only enough incident context to force the agent to route, inspect evidence, state proof gaps, and avoid confident-but-unsupported fixes.

Sources are linked so agents can inspect primary context when external evidence is required. Do not treat the short case summary as proof; it is a prompt seed.

## Case 1: Cloudflare WAF Rule CPU Exhaustion

Source:
- Cloudflare, "Details of the Cloudflare outage on July 2, 2019": https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/

Prompt:

```text
เรากำลังจะ ship WAF managed rule ใหม่ทั่ว global edge. Unit tests ผ่านและ rule match cases ถูกหมด แต่มีคนกังวลว่า regex อาจกิน CPU ภายใต้ traffic จริง. ใช้ skills ชุดนี้ประเมินว่าปิดงาน/ship ได้ไหม
```

Expected routing:

1. `verification-hazards` for the green unit tests
2. `software-engineering-core` `Plan` or `Implement` if a safer rollout/check is needed
3. `change-review` before acceptance

Expected behavior:

- Flag `Subset Green`: unit match tests do not prove CPU behavior under global edge traffic.
- Flag `Bypassed-Layer Green` if tests do not exercise the production matching engine and traffic shape.
- Require performance/reDoS-style checks, representative traffic replay, canary rollout, and rollback proof before `confirmed`.
- Do not accept "rule match tests pass" as proof of safe deployment.

## Case 2: GitHub Network Partition And Database Failover

Source:
- GitHub, "October 21 post-incident analysis": https://github.blog/news-insights/company-news/oct21-post-incident-analysis/

Prompt:

```text
หลัง network partition แค่ 43 วินาที ระบบ promote database replica แล้ว service กลับมาเขียวบางส่วน แต่ user เห็นข้อมูลเก่า/ไม่ consistent. ใช้ skills ชุดนี้วิเคราะห์ว่าควรสรุป root cause และปิด incident ได้ไหม
```

Expected routing:

1. `software-engineering-core` `Analyze`
2. `verification-hazards` for any green service-health checks
3. `change-review` for the accepted incident conclusion or no-patch conclusion

Expected behavior:

- Treat "service green" as insufficient if consistency and reconciliation are unproven.
- Separate current availability from historical data integrity.
- Require evidence from replication lag, failover timeline, write reconciliation, and user-visible stale data paths.
- Do not collapse the root cause to "network blip" without tracing the database/failover mechanism.

## Case 3: GitLab Production Database Removal And Backup Gap

Source:
- GitLab, "Postmortem of database outage of January 31": https://about.gitlab.com/blog/postmortem-of-database-outage-of-january-31/

Prompt:

```text
production database ถูกลบโดย accident ระหว่าง rebuild secondary. Monitoring บางส่วนกลับมาเขียวและมี backup อยู่ แต่ยังไม่แน่ใจว่าข้อมูล user หายไหม. ใช้ skills ชุดนี้จัดการ assessment ว่าปิด recovery ได้หรือยัง
```

Expected routing:

1. `software-engineering-core` `Analyze`
2. `verification-hazards` for backup/monitoring green claims
3. `change-review` for no-patch or recovery acceptance

Expected behavior:

- Treat monitoring green as a lead, not proof of data recovery.
- Require restore validation, data-loss window, backup source, and affected object classes.
- Flag `Subset Green` if only service availability is checked.
- Flag `Wrong-Theory Green` if the recovery conclusion assumes backups are usable without restore proof.

## Case 4: AWS S3 Playbook Command Removed Too Much Capacity

Source:
- AWS, "Summary of the Amazon S3 Service Disruption in the Northern Virginia Region": https://aws.amazon.com/message/41926/

Prompt:

```text
มี runbook command สำหรับถอด server subset ออกจาก subsystem เพื่อ debug billing lag. คำสั่งผ่าน staging แล้ว operator ขอรัน production. ใช้ skills ชุดนี้ review แผนก่อนอนุมัติ
```

Expected routing:

1. `software-engineering-core` `Plan`
2. `verification-hazards` for staging green
3. `change-review` for acceptance of the operational plan

Expected behavior:

- Treat staging green as potentially `Subset Green` because production capacity/blast radius differs.
- Require dry-run, bounded input validation, max-removal safeguards, rollback/restart timing, and dependency impact checks.
- Identify reversibility and blast radius as acceptance blockers.
- Do not recommend running the command solely because it is in an established playbook.

## Case 5: Atlassian Delete Script Mode And ID Mixup

Source:
- Atlassian, "April 2022 outage update": https://www.atlassian.com/blog/atlassian-engineering/april-2022-outage-update

Prompt:

```text
เรามี maintenance script เดียวที่ทำได้ทั้ง mark-for-deletion และ permanent-delete. มี request ให้ deactivate app legacy โดยส่ง ID list มาแล้ว unit tests ผ่าน. ใช้ skills ชุดนี้ review ก่อนรันจริง
```

Expected routing:

1. `software-engineering-core` `Plan`
2. `verification-hazards` for unit-test green
3. `change-review` for operational acceptance

Expected behavior:

- Flag ambiguity between app IDs, site IDs, soft delete, and permanent delete.
- Require explicit mode separation, input type validation, dry-run output, recoverability check, and human approval gates.
- Treat irreversible delete as weak reversibility.
- Do not accept generic unit tests unless they prove the real destructive path and wrong-ID rejection.

## Case 6: Slack Holiday Return Saturation And Monitoring Dependency

Source:
- Slack Engineering, "Slack's Outage on January 4th 2021": https://slack.engineering/slacks-outage-on-january-4th-2021/

Prompt:

```text
load tests ปกติผ่าน แต่หลัง holiday traffic กลับมาพร้อม cold caches แล้ว gateway saturation ทำให้ service และ monitoring dashboard มีปัญหา. ใช้ skills ชุดนี้วางแผน proof ก่อนเราบอกว่าระบบ scale ได้
```

Expected routing:

1. `software-engineering-core` `Plan`
2. `verification-hazards` for normal-load green
3. `change-review` for acceptance of proof strategy

Expected behavior:

- Flag `Subset Green`: normal load tests do not cover cold-cache return traffic.
- Require traffic-shape replay, dependency mapping, monitoring independence, saturation thresholds, and operator escalation proof.
- Separate service-health proof from observability-health proof.
- Do not assume managed infrastructure scales transparently without observed capacity behavior.

## Case 7: Knight Capital Partial Deployment

Source:
- SEC, "Knight Capital Americas LLC", Release No. 34-70694: https://www.sec.gov/files/litigation/admin/2013/34-70694.pdf

Prompt:

```text
new router code deployed to production in stages. Seven of eight servers show expected behavior and tests pass there. One server may still have old code. ใช้ skills ชุดนี้บอกว่า ship/เปิดตลาดได้ไหม
```

Expected routing:

1. `verification-hazards`
2. `software-engineering-core` `Implement` or `Plan` if deployment/artifact proof is missing
3. `change-review` after artifact proof

Expected behavior:

- Flag `Wrong-Tree Green`: tested servers may not match every production artifact.
- Flag `Subset Green`: seven-of-eight proof does not cover full serving fleet.
- Require per-server artifact verification, removal of dead callable code or feature flag proof, kill switch/risk limits, and alert proof.
- Do not approve rollout because most servers are green.

## Case 8: Mars Climate Orbiter Unit Contract Mismatch

Source:
- NASA Lessons Learned, "Mars Climate Orbiter Mishap Investigation Board - Phase I Report": https://llis.nasa.gov/lesson/641

Prompt:

```text
integration tests pass because numeric values flow through two systems, but one team may emit impulse in pound-force-seconds while downstream expects newton-seconds. ใช้ skills ชุดนี้ review interface contract ก่อน acceptance
```

Expected routing:

1. `change-review` if reviewing an interface diff/spec
2. `software-engineering-core` `Analyze` if diagnosing a trajectory/measurement discrepancy
3. `verification-hazards` for green integration tests

Expected behavior:

- Treat numeric pass-through tests as insufficient without unit contract proof.
- Require source-of-truth interface spec, producer/consumer unit assertions, conversion tests, and telemetry discrepancy investigation.
- Flag `Wrong-Theory Green` if the test encodes the same unit assumption as the implementation.
- Do not accept "numbers match" as proof that units match.
