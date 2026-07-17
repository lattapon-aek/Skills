# AGENTS.md Enforcement Policy

Skill installation makes workflows available; it does not guarantee that an
agent selects them or obeys their earliest gate. Copy the block below into the
root `AGENTS.md` of every repository that requires this suite. Keep it at the
repo level so it is active before a task-specific skill body is selected.

<!-- agents-policy:start -->
## Required Software-Engineering Evidence Gate

Before the first software-engineering tool call or edit, inspect available
skills, select `software-engineering-core`, and state one short reason. Use it
before specialized creation or implementation skills, including for small,
single-file, visual, experimental, and empty-workspace tasks.

When a request has the form `do X because Y`, treat X as dependent on Y unless
the user explicitly requires X even if Y is false. If Y is an unestablished
harness, runtime, framework, platform, vendor, model, tool, protocol, or
infrastructure mechanism, remain in `Clarify` or `Plan`, read the core
mechanism-design protocol, and keep `Implement` unavailable.

User wording, plans, proposed solutions, local file shape, and agent assertions
are mechanism claims, not mechanism evidence. Before any mechanism-dependent
target mutation, record the complete decision-changing claim ledger with
inspected authoritative source or discriminating live-probe evidence and the
exact verdict `Mechanism Verdict: established`. If any material claim is
absent, conditional, unproven, or contradicted, do not mutate the target;
report the proof gap and the cheapest verdict-changing check.

Record the user contract, intended state, plan commitments, allowed variations,
and proof obligations. Functional success does not waive intent conformance:
an unapproved material deviation blocks completion. Use
`verification-hazards` before trusting green/red proof or an agent report, and
use `change-review` before accepting a patch or justified no-patch conclusion.
<!-- agents-policy:end -->

Use the installed skill names shown by the harness. A namespace prefix such as
`agents-skills:` may be added by a plugin or registry; the ownership names in
the policy remain `software-engineering-core`, `verification-hazards`, and
`change-review`.

The mechanism paragraph is intentionally repo-level. The live matched A/B in
[the mechanism evaluation](../tests/mechanism-before-design/evaluation.md)
showed that the core skill body alone could be overridden by explicit solution
wording, while the same fail-closed rule in `AGENTS.md` kept the task in
Clarify/Plan. This is harness-specific evidence, not a universal guarantee;
retain behavioral evaluation for the target agent and version.
