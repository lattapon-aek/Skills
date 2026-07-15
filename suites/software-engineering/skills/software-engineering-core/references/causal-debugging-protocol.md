# Causal Debugging Protocol

Use this protocol for bugs, regressions, incidents, hangs, performance failures, flaky behavior, and environment/tooling failures. Its purpose is to distinguish a demonstrated cause from a plausible story and to prevent a symptom patch from being accepted as a fix.

## Diagnostic Vocabulary

Do not collapse these terms:

- `Symptom` — the externally visible wrong result or failure.
- `Fault Location` — where incorrect state or behavior first becomes observable.
- `Failure Mechanism` — how the fault propagates into the symptom.
- `Root Cause` — the earliest actionable condition whose correction prevents the demonstrated failure through the observed mechanism.
- `Trigger` — an input or event required to expose the fault; it is not automatically the root cause.
- `Contributing Factor` — changes likelihood or impact but is neither necessary nor sufficient by itself.
- `Mitigation` — reduces impact without proving or removing the cause.

## Investigation Loop

Run the loop until the root-cause gate is met or the remaining proof gap is explicit.

### 1. Freeze The Failure

Record expected behavior, actual behavior, exact input or event sequence, environment, version or artifact, timing, and the outcome oracle. Preserve a minimal reproduction when feasible. If the issue cannot be reproduced, record the historical evidence and do not silently substitute a different failure.

Gather the closest incident evidence first: raw logs, traces, requests, responses, payloads, timestamps, metrics, failing inputs, process state, and environment constraints. Prefer a path you can run or faithfully simulate over a second-hand summary. Use simulation to explain or discriminate incident evidence, not to replace available evidence.

### 2. Trace The Causal Chain

Trace backward from the symptom and forward from the trigger:

`trigger -> state transition -> first divergence -> propagation -> symptom`

Mark each link `observed` or `inferred`. The first suspicious line is not automatically the fault location, and the fault location is not automatically the root cause.

### 3. Maintain A Hypothesis Ledger

For each plausible cause record `Hypothesis | Evidence For | Evidence Against | Distinguishing Prediction | Check | Status`.

When more than one cause fits the evidence, keep at least two live hypotheses. Do not add decorative hypotheses; each candidate needs a check whose outcome would change the diagnosis. Use `live`, `weakened`, `ruled out`, or `supported`, not confidence adjectives without evidence.

### 4. Run Discriminating Checks

Prefer the cheapest check where competing hypotheses predict different outcomes. Useful checks include varying one causal input while holding the rest constant; comparing failing and non-failing cases at the first divergence; inspecting state around the suspected transition; replacing one dependency; testing a negative control; and reproducing across environment, artifact, timing, or concurrency boundaries.

A check that passes under every live hypothesis does not discriminate and cannot establish root cause.

Start at the observed failure and walk outward until the first divergence is located. Compare failing and non-failing cases, reduce the problem when possible, and check configuration, environment, permissions, orchestration, resource pressure, and recent changes before assuming the fault is application logic.

### 5. Apply The Root-Cause Gate

Label a cause `proven` only when all applicable conditions hold:

1. The original symptom is reproduced or anchored to direct incident evidence.
2. The causal chain connects trigger, first divergence, mechanism, and symptom with no material unexplained jump.
3. A discriminating check supports this cause over realistic alternatives.
4. Competing hypotheses are ruled out or bounded by observed evidence.
5. Changing the suspected cause changes the outcome while relevant controls stay stable, when a safe intervention is feasible.
6. The cause explains the observed scope, timing, and affected/non-affected cases.

If any condition is missing, use `supported but incomplete` or `unproven`; state the cheapest next check. Do not rename a correlation, trigger, last error, or successful patch as root cause.

### 6. Choose Corrective Action

Map the proposed change to the demonstrated mechanism. State whether it:

- removes the root cause
- blocks the propagation path
- adds containment or mitigation only
- improves observability only

Do not present mitigation, retry, fallback, timeout increase, error suppression, or output normalization as a corrective fix unless evidence shows it removes the demonstrated cause. Emergency mitigation may proceed only when authority permits it and the unresolved root cause remains explicit.

### 7. Prove Resolution

After the change:

1. Replay the original reproduction or closest faithful incident simulation.
2. Observe the user-visible outcome oracle, not only an internal branch or new unit test.
3. Re-check the causal chain at the former divergence point.
4. Run at least one relevant negative or adjacent control.
5. Challenge whether a symptom-hiding patch or the wrong causal theory would also pass.
6. State the recurrence boundary: which inputs, environments, timing, or paths remain untested.

If the original issue persists, changes form, or disappears for an unexplained reason, return to Analyze. Do not stack another speculative patch on top of the first.

## Required Investigation Record

For non-trivial debugging, preserve:

- `Failure Definition`
- `Reproduction Baseline`
- `Causal Chain`
- `Hypothesis Ledger`
- `Discriminating Checks`
- `Root Cause Status` — `proven`, `supported but incomplete`, or `unproven`
- `Corrective Action Class`
- `Original-Reproduction Replay`
- `Recurrence Boundary`
- `Proof Gap`

Keep the record proportional to the incident. A small local bug may need only a few terse lines; a cross-system or intermittent failure needs a durable work packet and progress log.

## When Reproduction Is Not Possible

Use direct historical evidence such as production logs, traces, metrics, error reports, and user artifacts. State what cannot be reproduced and why. A narrow simulation may bound or explain the mechanism, but it must not silently replace the original incident.

Do not upgrade a non-reproduced incident to a proven root cause. Use `supported but incomplete` or `unproven`, identify the missing causal link, and name the capture or discriminating check that would close it.
