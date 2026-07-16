Claim Under Test: "amended" + "tests pass" proves the patch is ready to merge.
Hazard Scan:
- Bypassed-Layer Green: at risk; test layer is unknown.
- Subset Green: at risk; local green may not cover the shipping surface.
- Wrong-Theory Green: at risk; root cause evidence is not shown.
- Wrong-Tree Green: at risk; amended bytes are not tied to the merge artifact.
- Not-Your-Red: not applicable.
- Weak-Oracle Green: at risk; the report does not show what the tests assert.
Counter-Checks Run: none; only second-hand report and local green were provided.
Verification Verdict: still a lead.
Proof Gap: inspect the exact commit with git show and rerun relevant tests from that artifact.
Residual Risk: wrong tree, subset coverage, and unproven cause.
