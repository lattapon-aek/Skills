---
name: task-intake
description: Convert vague, underspecified, or messy requests into a clear execution brief. Use when an agent must clarify the real objective, narrow the scope, gather source material, identify dependencies, surface impact, and define a provable result before implementation or analysis starts.
---

# Task Intake

## Intent

Clarify until the objective, evidence, and proof of done are sufficient for safe execution. Do not rush into implementation on top of an unclear request.
Stay in intake mode: identify what must be known, what evidence must be gathered, and what success must look like. Do not drift into execution, debugging, code inspection, or external research unless the user explicitly asks for that as part of the current phase.
Golden rule: shape the task and name the evidence needed for execution, but do not turn intake into execution, debugging, or proof work.

## When To Use

Use this skill when:

- the request is vague, broad, or underspecified
- the real outcome is not the same as the literal request
- the work could touch multiple systems, teams, or deliverables
- the scope needs to be narrowed before implementation or analysis starts
- success cannot yet be proven with a concrete check

## When Not To Use

- Do not use this skill when the objective, scope, source material, and proof of done are already clear enough to execute safely.
- Do not use this skill as a substitute for debugging, implementation, or review once the task is already in those phases.

## Guiding Principles

Apply the repo's four principles before execution starts:

- `Think Before Coding`: ask until the real objective and tradeoffs are visible
- `Simplicity First`: narrow the request to the smallest useful outcome
- `Surgical Changes`: avoid pulling unrelated work into the scope
- `Goal-Driven Execution`: define proof of done before handoff

## Stop Condition

Stop clarifying and hand off to execution only when all of these are true:

- the `Objective` is specific enough to act on
- the `Desired Outcome` is distinguishable from the user's raw wording
- the minimum `Source Material` needed to proceed is identified
- the `Scoped Work` is narrow enough to execute responsibly
- the initial `Proof of Done` is concrete enough to verify
- remaining unknowns are either low risk, explicitly assumed, or assigned a resolution path
- the intake has not silently drifted into implementation or pre-solving the task

## Clarify Until Clear

- Restate the request in one sentence.
- Extract the real objective, desired outcome, stakeholders, constraints, and success criteria.
- Do not accept the proposed solution as the goal until the underlying problem, decision need, or pain point is clear.
- When the user proposes a solution, ask what failure, bottleneck, decision, or missed outcome that solution is supposed to address.
- Keep asking when the missing detail affects correctness, scope, architecture, budget, or access.
- Stop asking only when the task is scoped tightly enough to execute responsibly.

## Source Of Truth

Use the best available evidence for the intake:

- Start with local material: files, code, docs, data, systems, tickets, examples, screenshots, logs, or current repo context.
- Search external sources when the task depends on third-party behavior, market context, vendor constraints, standards, regulations, or current ecosystem facts.
- When the task depends on legal, regulatory, policy, or vendor-compliance requirements, explicitly identify the authoritative external source that must anchor the work.
- Prefer official docs, vendor docs, standards, release notes, and primary references over secondary commentary.
- Separate `required evidence to proceed` from `helpful context`.
- Distinguish explicit facts from assumptions and unknowns.
- Do not treat guesswork as requirement.
- During intake, name the evidence and authority that must be consulted; do not turn the intake itself into a research or verification pass unless the user explicitly asks for that phase now.

## Question Triage

For each unknown, decide one path:

- `Ask Now`: use when the missing detail affects correctness, architecture, access, budget, or irreversible work.
- `Investigate from Source`: use when the answer should exist in code, files, docs, logs, tickets, or other inspectable artifacts.
- `Investigate Externally`: use when the answer depends on official docs, vendor behavior, standards, release notes, or current external facts not available in the workspace.
- `Assume Explicitly`: use only when the risk is low, the assumption is reversible, and it is clearly labeled in the brief.

## Escalation Rule

- If there are more than two `Ask Now` items that materially affect correctness, scope, or acceptance criteria, do not hand off to execution yet.
- If the task depends on external facts and those facts have not been gathered from authoritative sources yet, do not pretend the intake is complete.
- In that case, ask the user those questions first instead of pretending the task is ready.
- Only continue with assumptions when the unresolved items are low risk and explicitly reversible.

## Intake Boundaries

- Do not inspect repository paths, open files, check links, or browse docs just to prove they exist during intake.
- If the user names artifacts, treat them as claimed source material unless access verification is itself part of the request.
- If access to local or external artifacts is still needed before execution, record that as a resolution path instead of prematurely blocking the intake.
- Do not recommend concrete technical solutions, migrations, or architecture choices during intake unless the user explicitly asks for options at this stage.

## Scope Narrowing

- Narrow the task to the smallest useful deliverable that still solves the real need.
- Break broad goals into parts that can be executed and verified independently.
- Separate must-have outcomes from nice-to-have additions.
- State what is explicitly out of scope for this phase.

## Impact And Tradeoffs

- Call out affected users, systems, timelines, and dependencies.
- Surface tradeoffs early when scope, speed, or quality pull in different directions.
- Recommend the narrower or safer option when it still satisfies the objective.
- Make explicit which interpretations, scopes, or proposed solutions were considered but ruled out, and why.

## Output

Produce a short brief with:

- `Objective`
- `Desired Outcome`
- `Source Material`
- `External Evidence Needed`
- `Scoped Work`
- `Out of Scope`
- `Constraints`
- `Assumptions`
- `Ruled-out Interpretations`
- `Impact and Tradeoffs`
- `Proof of Done`
- `Open Questions and Resolution Path`

## Verification

- Convert subjective requests into observable proof of done.
- Make clear whether proof depends only on local execution or also on external evidence or current vendor/platform behavior.
- If the intake rejected a proposed solution, broad scope, or interpretation, say what evidence or reasoning ruled it out.
- If proof cannot be defined yet, keep clarifying.

## Proof Gap Rule

- State what is already clear enough to proceed.
- State what is not yet proven or not yet gathered.
- State what evidence, answer, or next phase would close that gap.

## Phase Handoff

- Hand off to `root-cause-debugging` when the core problem is still an unexplained failure or regression.
- Hand off to `change-implementation` when the change objective is clear enough to execute safely.
- Hand off to `change-review` only after changes or explicit no-change conclusions are ready to be assessed.

## Reference

Use [references/brief-template.md](references/brief-template.md) when the user wants a structured intake artifact or when another agent will consume the result.
Use [../../references/four-principles.md](../../references/four-principles.md) when you need the shared execution doctrine behind this repo.
