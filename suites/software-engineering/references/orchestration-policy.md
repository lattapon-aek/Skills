# Orchestration Policy

Use this policy when a software-engineering task spans ownership phases.

## Preflight

Before the first engineering tool call or edit:

1. Inspect available skills.
2. Name the selected primary skill and one short reason.
3. Identify the working document and authority mode.
4. Only then inspect, plan, verify, or edit.

Do not skip preflight because a task is small, single-file, visual, experimental, or in an empty workspace.

## Suite Contract

Use exactly one primary owner at a time:

- `software-engineering-core` owns clarification, planning, causal analysis, implementation, and justified no patch.
- `verification-hazards` challenges whether a concrete result or report proves functional behavior and intent conformance.
- `change-review` accepts or rejects a concrete result.

Default flow:

1. `software-engineering-core`
2. `verification-hazards` whenever a result or report is about to be trusted
3. `change-review` for every concrete patch, implemented result, or justified no-patch conclusion

Every applicable gate remains mandatory regardless of task size. Continuity artifact choice does not alter execution rigor.

## Routing

- Use core `Clarify` when objective, domain, source material, intended state, or proof of done is unclear.
- Use core `Plan` when the objective is clear but approach, boundary, commitments, or conformance criteria are unsettled.
- Use core `Analyze` when a failure mechanism or root cause is not proven.
- Use core `Implement` when approach, assumptions, boundary, intended state, and authority are confirmed.
- Use hazards before trusting green/red output, CI, benchmark, staging, rollout, monitoring, or an agent report.
- Use hazards first for approve, merge, ship, accept, close, go/no-go, or production-run questions based mainly on such proof.
- Use review only when a concrete acceptance target or justified no-patch artifact exists.

Start with the earliest unmet gate. Do not jump to review while objective, diagnosis, plan, implementation, conformance, or proof remains open.

## Intent-Conformance Routing

When observed state differs materially from intended state:

1. Do not accept functional green as closure.
2. Check whether the delta is inside an explicit allowed variation.
3. If not, mark `unresolved deviation`.
4. Return to core `Implement` when restoring the approved state stays inside the proven boundary.
5. Return to core `Plan` when the approach, boundary, contract, or intended state must change.
6. Amend the working document before implementing the alternative and obtain required authority.

An agent cannot authorize its own material deviation or retrospectively redefine the intended state.

## Handoff Packets

- Core to hazards: working document, claim, intended state, exact result, acceptance artifact, conformance check, and known gaps.
- Hazards to core: failed hazard or gate, observed tell, cheapest next check, and mode to resume.
- Hazards to review: verdict, sufficiency gates, open hazards, conformance status, and residual risk.
- Core to review: contract, objective, intended and observed state, diff or no patch, acceptance coverage, deviations, verification, hazard verdict, and proof gaps.
- Review to core: blocking finding, exact open gate, required evidence or change, and owner/mode to resume.

Carry inspectable evidence, not only prose conclusions. After compaction or handoff, rebuild state from the working document and current workspace.

## Backward Routing

- Unclear objective or intended state -> `Clarify`
- Invalidated approach or material plan deviation -> `Plan`
- Unproven failure mechanism -> `Analyze`
- Concrete patch, artifact, or oracle gap -> `Implement`
- Untrusted green/red result -> `verification-hazards`

Treat a phase gate as an evidence boundary, not an automatic user round trip. Continue when authority permits and the gate is proven; stop only for missing evidence, user decision, new authority, or external state.

## No-Patch Rule

`No patch` is valid when current source and runtime evidence do not justify a change. It must state what was inspected, what candidate fixes were ruled out, how current state compares with intended state, remaining historical or external gaps, and the final review verdict.
