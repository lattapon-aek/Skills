# Core Planning Mode Tests

Fixtures for forward-testing the `software-engineering-core` skill in `Plan` mode against realistic design-decision prompts before implementation starts.

## Goals

- Verify that the agent frames the actual decision clearly
- Verify that the agent compares a small realistic option set instead of brainstorming endlessly
- Verify that the agent recommends one approach explicitly
- Verify that the agent defines execution boundaries and proof strategy for the next phase

## Scenario 1

- integration choice with local code context and external API constraints
- local seam to inspect:
  - `../implementation/sample-app/src/openai/client.ts`
  - `../implementation/sample-app/src/openai/support-assistant.ts`

## Scenario 2

- migration sequencing decision with rollout and blast-radius tradeoffs
