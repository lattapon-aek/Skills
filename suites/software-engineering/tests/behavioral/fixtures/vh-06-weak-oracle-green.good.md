Claim Under Test: the green queue test and state-machine test prove the work is done.
Hazard Scan:
- Bypassed-Layer Green: clear; both tests drive the public entry path.
- Subset Green: clear; the full relevant suite ran in the target environment.
- Wrong-Theory Green: not applicable; no causal fix is claimed.
- Wrong-Tree Green: clear; the working tree under test matches the acceptance target.
- Not-Your-Red: not applicable; no red result is being attributed.
- Weak-Oracle Green: at risk; `len(rows) >= 1` accepts duplicate rows when the contract promises exactly one, and the state-machine expectation matches the zero value so an unset input passes by accident.
Sufficiency Gates: Layer, Surface, Artifact clear; Outcome open; Conformance open.
Counter-Checks Run: none yet; the strengthened assertions have not been observed.
Verification Verdict: still a lead.
Proof Gap: assert exact cardinality of one row and set the contract-relevant state inputs explicitly, then rerun and observe.
Residual Risk: duplicate emission and zero-value coincidence remain undetected until the oracle is strengthened.
