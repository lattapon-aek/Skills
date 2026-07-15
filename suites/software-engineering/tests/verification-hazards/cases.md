# Test Cases — verification-hazards

Stress cases for the six hazards. Each presents a plausibly-green (or plausibly-your-fault-red) situation; the expected behavior is the counter-check that exposes the lie, not a rush to accept or blame. These are assessment scenarios (like the software-engineering-core cases), not `node --test` fixtures — the skill is verification doctrine, not a code transform.

## Case 1: Bypassed-Layer Green

Request:

```text
ใช้ verification-hazards ประเมินอันนี้ให้หน่อย: ผมมี feature ที่จะ pause session เมื่อ budget เกิน threshold. unit test เขียว — มันเรียก derivePause() ตรง ๆ แล้วเช็คว่า return PAUSED. พร้อม merge เลยไหม?
```

Expected behavior:

- Flag hazard 1 `at risk`: the test calls the derivation directly, not through the trigger that feeds it in production.
- Note the transition/re-evaluation risk: a one-shot derivation can flip back on the next tick if nothing re-asserts the state.
- Require a real-trigger pass and a second evaluation cycle before `confirmed`.
- Do not accept the direct-call green as proof the feature holds in production.

## Case 2: Subset Green

Request:

```text
ใช้ verification-hazards ดูให้หน่อย: executor รายงานว่า `go test ./internal/...` ผ่านหมด 32 ok. executor รันใน sandbox ที่ bind unix socket ไม่ได้. ปิดงานได้ไหม?
```

Expected behavior:

- Flag hazard 2 `at risk`: the sandbox structurally cannot run socket/daemon-tier tests, so green is a subset.
- Flag hazard 4 as adjacent: the report is a lead from another environment, not proof.
- Require the daemon/socket tier run natively, the full suite (not the `internal/...` slice), and a CI check before acceptance.

## Case 3: Wrong-Theory Green

Request:

```text
ใช้ verification-hazards: เจอ write ล้มเป็นระยะ ผมตั้งสมมติฐานว่าเป็น SQLite contention เลยเขียน fix + test จำลอง contention แล้วเขียว. ควร ship ไหม?
```

Expected behavior:

- Flag hazard 3 `at risk`: the root cause was theorized, never observed; the test encodes the same contention assumption as the fix.
- Require instrumenting the actual live failure (read the real error, not a constructed repro) before trusting the fix.
- Ask for an observation the contention theory predicts and a competing theory (e.g. a request collision) does not.

## Case 4: Wrong-Tree Green

Request:

```text
ใช้ verification-hazards: sub-agent บอกว่า "amended the fix, tests pass". local เขียว. merge ได้เลยไหม?
```

Expected behavior:

- Flag hazard 4 `at risk`: "amended" is asserted without inspecting the commit; the sandbox may have blocked the git write, leaving the fix only in the working tree.
- Require `git show HEAD:<file>` to confirm the committed bytes, a diff scan for leaked paths/stray files, and a full-suite run from a clean checkout.
- Treat the sub-agent report as a lead until the committed artifact reproduces the green.

## Case 5: Not-Your-Red

Request:

```text
ใช้ verification-hazards: push แล้ว CI แดงที่ TestSteadyIdle ซึ่ง flaky อยู่บ้าง. commit ผมไม่ได้แตะ subsystem นั้นเลย. ต้อง revert ไหม?
```

Expected behavior:

- Flag hazard 5 `at risk`: intermittent, timing-shaped failure in a subsystem the change did not touch.
- Require reproducing the parent commit under matched stress (high `-count`, CI-like constraints) before attributing red to the diff.
- Distinguish pre-existing flake vs environment contention vs real regression; do not revert on a single loaded FAIL without the baseline comparison.

## Case 6: Weak-Oracle Green

Request:

```text
ใช้ verification-hazards: queue test ผ่านเพราะเช็ค `len(rows) >= 1` และ state-machine test ไม่ได้กำหนด liveness แต่ expected result ตรงกับ zero value. ปิดงานได้ไหม?
```

Expected behavior:

- Flag hazard 6 `at risk`: both assertions allow plausible incorrect implementations to pass.
- Use all six exact hazard labels; do not replace `Not-Your-Red` with the `Baseline` gate name.
- Require exact queue cardinality when the contract promises one row.
- Require explicit contract-relevant state inputs instead of relying on zero values.
- Return `still a lead` until the strengthened assertions are observed green.

## Case 7: Compound (all six)

Request:

```text
ใช้ verification-hazards ทำ full hazard scan: fix สำหรับ bug ที่ผมยังไม่เคยเห็นเกิดจริง, unit test เขียวโดยเรียก handler ตรงและเช็คแค่ status, รันใน sandbox subset, sub-agent commit ให้, และ CI มี test อื่นแดงที่ผมไม่ได้แตะ.
```

Expected behavior:

- Produce a `Hazard Scan` marking 1–6 all `at risk` with the tell for each.
- Order counter-checks by cost; run the cheapest that changes the verdict first.
- Return verdict `still a lead` with a `Proof Gap` naming the next check per open hazard, and route per Phase Handoff (Analyze for the unproven cause, Implement for the unverified committed artifact).

## Case 8: Working But Nonconforming Green

Request:

```text
ใช้ verification-hazards: approved plan กำหนด durable queue แต่ implementation ใช้ in-memory callback แทน ตอนนี้ happy-path test เขียวและ demo ใช้งานได้ ปิดงานได้ไหม?
```

Expected behavior:

- Flag `Weak-Oracle Green` as `at risk` because the happy-path oracle accepts a working implementation that violates the durability and failure-boundary commitments.
- Mark `Outcome` only partially established and `Conformance` open.
- Treat `Allowed Variations` as `none` unless the working document states otherwise.
- Return `still a lead` despite functional green.
- Route to Implement to restore the approved boundary, or Plan for a prospective amendment with explicit authority.
- Do not let the agent authorize the deviation or rewrite the plan retrospectively.
