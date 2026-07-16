# Hazard Catalog

Field-tested detail for each verification hazard. Every pattern below cost real rounds before it was understood. Use this when the SKILL.md summary is not enough to recognize the hazard in front of you.

The unifying failure: a result agreed with the setup that produced it instead of with the behavior that ships. Green is a claim; these are the six ways the claim and the shipping behavior come apart.

---

## Hazard 1 — Bypassed-Layer Green

**What it is.** The verification path and the production path diverge before the code under test runs. The test reaches the effect through a shortcut — a direct handler call, a mock transport, an injected state, a client-side shim — that carries none of the constraints the real trigger imposes (deadlines, transitions, backpressure, timing).

**Concrete patterns seen.**

- A test calls the internal effect directly (`flush()`, the RPC handler, a state setter) instead of firing the event that would call it in production. The trigger layer — where the real bug lives — is never exercised. The feature is transition-gated or telemetry-fed, and the test sets the ratio/state directly instead of driving the input that computes it.
- A probe sleeps or grants on the *client* side of a boundary the production code crosses on the *server* side. The probe passes because it never hit the server-side deadline that later caps the real behavior. The fix then moves the wait to the server side — exactly where the cap bites — and the passing probe told you nothing about it.
- A stateful hold/latch/pause is asserted after the state is injected, not after the transition is driven. A one-shot, stateless derivation looks correct for one evaluation, then flips back on the next tick because nothing re-asserts it — and the test, having injected the state once, never took a second tick.

**Why green lied.** The bypass removed the constraint that produces the failure. The test proved the effect works when called directly; production never calls it directly.

**Counter-check.** Exercise the same entry layer production uses.

- Trigger/telemetry/transition/timeout-gated feature → run an end-to-end pass through the real trigger (a live capstone), not a direct call.
- Hold / latch / debounce / anything that must survive re-evaluation → drive the transition, then take a **second evaluation cycle** and confirm it still holds. A manual state edit in a test is a broken production path, not a proof.
- A wait/deadline/timeout → make the check cross the same boundary (same process, same transport, same clock source) the real code crosses.

**Cheapest proof.** One real-trigger run or one extra tick that reaches the code the bypass skipped.

---

## Hazard 2 — Subset Green

**What it is.** The run covered a slice that structurally cannot reach the failing case. Green is honest about the slice and silent about the rest.

**Concrete patterns seen.**

- A packet/module subset passes while the full suite fails — the failing test lives outside the subset (e.g. an integration tier the module tests exclude). A report claims "all tests pass" from a command that never included the tier that broke.
- A compile-only or `-c` build is taken as a test pass. It proves the code builds, not that it behaves.
- Green came from a sandbox that structurally cannot run part of the suite — cannot bind sockets, spawn subprocesses, or touch the filesystem those tests need. The executor's green is a subset-green by construction; the excluded tests only run natively.
- Local passes while CI is red (or stays red unnoticed for many commits). The local environment differs from CI in ways the failing test depends on.
- A run used a fake adapter/mock provider when the real one is required to exercise the behavior; the build tag or flag that selects the real path was missing.

**Why green lied.** The green surface and the shipping surface are not the same set. What broke lives in the difference.

**Counter-check.** Run the full surface in the target environment.

- Full suite, not the packet subset. The real provider/adapter, not the fake. The race detector where concurrency matters.
- Enumerate what your sandbox/local environment *cannot* run, and run exactly those parts where they can run.
- Check CI on every verification, not only local gates. A green local with unknown CI state is a lead, not a pass.

**Cheapest proof.** The full-suite result from the shipping environment, plus an explicit list of anything the narrow run could not cover.

---

## Hazard 3 — Wrong-Theory Green

**What it is.** The fix rests on a root cause that was inferred but never observed failing. The offline test encodes the same assumption as the fix, so they confirm each other while both stay disconnected from the real failure.

**Concrete patterns seen.**

- A root cause was diagnosed twice, wrong both times, from a rendered/summarized view of the failure — until a live probe disproved the theory outright. The real cause was a flag consumed too early, a cursor read from the wrong offset — visible only in the raw stream, not the rendered one.
- A repro and a fix packet were built entirely on an unconfirmed theory (resource contention). Live instrumentation of the *actual* error showed a different cause (a request collision), and the theory-built fix failed live.
- A pattern/fingerprint was matched against a rendered view while production classifies the raw stream; escape sequences split the phrase in the raw bytes, so the pattern that passed on rendered text scored zero on what actually ships. Verifying against the wrong representation cost the same mistake twice.

**Why green lied.** The test and the fix share the wrong model. Two things that agree with each other can both disagree with reality.

**Counter-check.** Make the real failure name the cause before you author the fix.

- Instrument or reproduce the live failure and read the real signal — log the failing value, `grep` the raw stream, `lsof` the live process, inspect the actual error string. Do not theorize from a rendered, summarized, or remembered view.
- Prefer an observation the theory predicts *and a competing theory does not* — that is what discriminates cause from coincidence.
- A prior fix for the same symptom that bounced is a strong signal the theory is wrong, not that the fix was almost right.

**Cheapest proof.** One direct observation of the real failure consistent with the theory and inconsistent with its main rival.

---

## Hazard 4 — Wrong-Tree Green

**What it is.** The artifact you verified is not the one that ships. Green is real, on the wrong bytes.

**Concrete patterns seen.**

- An "amended" or "committed" fix that lives only in the working tree — the sandbox blocked the git write, so `HEAD` still has the old code. Cherry-picking or building from the commit ships the pre-fix version while local green came from the dirty tree.
- An uncommitted change is invisible to the worktree or executor that runs from a branch. The runner silently proceeds on a hollow or stale version and reports against that.
- A build-machine absolute path or a stray generated file leaked into the diff; it passes locally (the path exists on that machine) and fails on a clean checkout / other OS.
- A required companion change was skipped: a hardcoded expected-count not bumped when an entry was added, a registration/manifest/wipe-list not updated. The primary change is green; the companion invariant fails elsewhere — often in a tier the sandbox could not run (see Hazard 2).

**Why green lied.** The observation ran on bytes the commit does not contain, or omits bytes the commit needs.

**Counter-check.** Verify ground truth, not the claim.

- Read the committed content directly: `git show HEAD:<file>`. Do not trust "amended" without it.
- Scan the diff for leaked absolute paths and stray files before merge; prefer environment-neutral temp paths over hardcoded ones.
- Re-run the full suite from a clean checkout of exactly what ships.
- Treat every "done / fixed / amended / tests pass" from a sub-agent, sandbox, or other machine as a lead until the committed artifact reproduces the result.

**Cheapest proof.** The shipping artifact, read from the commit, reproducing the green.

---

## Hazard 5 — Not-Your-Red

**What it is.** A red result you did not cause — a pre-existing flake, environment contention, or timing/throughput sensitivity — misattributed to your change.

**Concrete patterns seen.**

- A test that fails a small fraction of runs on the untouched main branch (a late-activity or ordering race). In-process it can fail several times in a row and perfectly mimic a deterministic regression from your diff.
- Resource contention from the test environment itself: leaked background servers/processes from earlier runs starve the subsystem under test, so a full-suite run flakes under load while the same test passes in isolation.
- CI-only timing/throughput failures — a slow subscriber draining fewer chunks than expected, a cleanup race under constrained parallelism — that are about the CI machine's timing, not the code.
- A red that names a subsystem your change never touched.

**Why green/red lied.** The signal is about the environment or a pre-existing instability, not about the change under test.

**Counter-check.** Reproduce the baseline before blaming the diff.

- Run the **parent commit** under the same stress the failure appeared under: high repeat count, constrained parallelism (e.g. single-threaded), the CI-like environment. If the untouched parent shows the same failure, it is not your diff.
- Isolate contention first: kill leaked servers/processes, re-run the test alone, before trusting a FAIL from a loaded full-suite run.
- Distinguish the three: pre-existing flake (parent fails intermittently too), environment contention (fails only under load, passes isolated), real regression (parent clean, your commit fails deterministically under matched stress).

**Cheapest proof.** The parent commit's behavior under matched stress next to your commit's — the comparison is the evidence.

---

## Hazard 6 — Weak-Oracle Green

**What it is.** The verification reaches the intended layer, surface, and artifact, but the assertion is too permissive to prove the promised outcome.

**Concrete patterns seen.**

- A queue test checks that at least one row exists when the contract promises exactly one, allowing duplicate or over-emitted rows to pass.
- A state-machine test omits a contract-relevant input and passes only because the language's zero value happens to select the expected branch.
- An HTTP or command test checks only success status or exit code while ignoring the returned data, persisted state, ordering, or side effect.
- A snapshot is stable but encodes formatting rather than the semantic contract that users depend on.
- The system remains operational, but its architecture boundary, output shape, required sequence, or other approved plan commitment differs from the intended state and the test checks only functional success.

**Why green lied.** The wrong implementation satisfies the same weak assertion as the correct one.

**Counter-check.** Name a plausible incorrect implementation that would still pass, then add the smallest assertion that makes it fail. Also name one working but plan-divergent implementation and require the oracle to reject it. Compare intended state, observed state, allowed variations, and deviation authority. Set contract-relevant inputs explicitly. Prefer exact cardinality, ordering, state transition, persisted effect, semantic output, and intent-conformance checks over broad truthiness.

An agent cannot declare its own material deviation equivalent, harmless, or better. Only a pre-approved variation or explicit user or governing-document amendment authorizes it.

**Cheapest proof.** One discriminating assertion that fails for the plausible wrong or working-but-nonconforming implementation.

---

## Applying The Catalog

- Most real incidents are a compound: a wrong-theory fix (3) that passed offline because the test bypassed the real trigger (1), reported green from a subset the sandbox could run (2), with an assertion too weak to expose the difference (6). Scan all six even when one is obvious.
- The counter-checks are ordered by cost within each hazard. Run the cheapest one that would actually change your verdict; do not build a harness when a single `git show` or one extra tick settles it.
- When a counter-check moves the verdict from `confirmed` to `still a lead`, that is the skill working. Record it in `Proof Gap` and route per the SKILL's Handoff rather than shipping the green.
