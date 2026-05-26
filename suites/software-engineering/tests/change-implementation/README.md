# Change Implementation Tests

Focused fixtures for forward-testing the `change-implementation` skill on real files in this repository.

## Goals

- Verify that the agent traces to a concrete patch point before proposing edits.
- Verify that the agent prefers the smallest safe patch.
- Verify that the agent explains `Why This Patch Point` and the likely blast radius.
- Verify that the agent separates local evidence from external evidence when third-party API behavior matters.

## Fixtures

- `sample-app/README.md`: doc-only small patch target
- `sample-app/src/auth/login.ts`: local code path with a narrow bug-fix surface
- `sample-app/src/openai/client.ts`: OpenAI wrapper layer
- `sample-app/src/openai/support-assistant.ts`: feature logic that depends on the wrapper

## Suggested Cases

1. Reorder or update a small doc block in `sample-app/README.md`
2. Fix a login bug by tracing from the exported function to the exact branch that needs to change
3. Migrate the OpenAI wrapper toward the Responses API while preserving surrounding behavior
