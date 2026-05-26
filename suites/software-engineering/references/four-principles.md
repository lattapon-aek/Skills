# Four Principles

These four principles govern execution across this repository's skills.

## Evidence Hierarchy

Use the best available evidence for the question at hand.

Preferred order:

1. Real system behavior: runtime output, logs, traces, metrics, failing commands, observed results
2. Local artifacts: source code, config, tests, docs, tickets, diagrams, data in the current workspace
3. Official external sources: vendor docs, platform docs, standards, API references, release notes, source repositories
4. Supporting external sources: issue trackers, maintainer comments, reputable community writeups

Treat memory, conventions, and generic patterns as hints, not evidence.

## 1. Think Before Coding

- Do not assume silently.
- State assumptions explicitly.
- Present multiple interpretations when ambiguity exists.
- Push back when a simpler or safer approach exists.
- Stop and ask when confusion affects correctness.
- When the answer depends on third-party behavior or current external facts, gather outside evidence before concluding.

This principle addresses wrong assumptions, hidden confusion, and missing tradeoffs.

## 2. Simplicity First

- Write the minimum code that solves the real problem.
- Do not add features, abstractions, configurability, or speculative flexibility that was not requested.
- Do not add error handling for impossible scenarios just to look comprehensive.
- If a smaller implementation is clearly sufficient, prefer it.

This principle addresses overcomplication and bloated abstractions.

## 3. Surgical Changes

- Touch only what the task requires.
- Do not "improve" adjacent code, comments, or formatting unless required for correctness.
- Match the surrounding style.
- Mention unrelated dead code or issues; do not fix them opportunistically.
- Clean up only the imports, variables, and helpers your own change made obsolete.

This principle addresses orthogonal edits and touching code you should not touch.

## 4. Goal-Driven Execution

- Define what success looks like before editing.
- Turn tasks into verifiable checks.
- Prefer tests, reproductions, direct runtime checks, or explicit commands over subjective judgments.
- For multi-step work, pair each step with a verification target.
- Keep iterating until the result is proven, or state exactly what could not be proven.

## Evidence Gathering Rule

- Start with local evidence when the answer should exist in the current workspace or running system.
- Search external sources when local evidence is missing, incomplete, contradictory, or when the question depends on vendor, library, platform, policy, or ecosystem behavior.
- Prefer primary sources first.
- If local and external evidence conflict, state the conflict and resolve it with the most authoritative source available.
- Distinguish local evidence, external evidence, and assumptions in your reasoning and output.

This principle addresses weak success criteria and encourages independent, verification-driven execution.
