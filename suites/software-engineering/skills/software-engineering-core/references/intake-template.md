# Brief Template

## Objective

One sentence describing what must be achieved.

## Desired Outcome

Describe the real result the user wants, not just the artifact.

## Failure or Decision Domain

- Classification: one of — `application logic` | `dependency` | `runtime environment` | `sandbox/permissions` | `orchestration` | `resource pressure` | `external vendor` | `design/migration/integration`
- Rationale for this classification

## Source Material

- Required evidence to proceed
- Files
- Code or repositories
- Docs or tickets
- Logs or command output
- Systems
- Stakeholders
- Deadlines

Helpful context:

- Additional examples
- Background notes
- Nice-to-have references

For incident-driven work, note separately:

- Current workspace state
- Historical incident state
- Whether they agree or conflict

## External Evidence Needed

- Official docs, vendor docs, standards, release notes, or web research required before execution
- What question each external source must answer

## Scoped Work

- The smallest useful deliverable
- Work split into parts if needed

## Out of Scope

- Explicitly excluded work for this phase

## Constraints

- Technical limits
- Policy or approval limits
- Time or budget limits

## Assumptions

- State every assumption explicitly

## Impact and Tradeoffs

- Affected users, systems, and timelines
- Tradeoffs that may change the approach

## Proof of Done

- Observable conditions for success

## Open Questions and Resolution Path

- Only include questions that materially affect execution
- Mark each as `Ask Now`, `Investigate from Source`, `Investigate Externally`, or `Assume Explicitly`

## Clarify Exit Checklist

Complete this before transitioning to the next mode. All items must be checked.

- [ ] Failure or Decision Domain confirmed by at least one user statement, runtime signal, or source scan — not inferred from pattern matching alone
- [ ] Source Material names specific artifacts (files, logs, systems, commands) — no placeholders
- [ ] All `Ask Now` questions answered by the user or re-classified as `Assume Explicitly`
- [ ] Ruled-out Interpretations lists at least one alternative reading that was considered and rejected
- [ ] Objective can be stated in one concrete sentence with a verifiable success condition

If any item is unchecked: present this output and stop. Do not transition in the same response.
