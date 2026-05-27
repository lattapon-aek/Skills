# PR: Migrate the OpenAI wrapper to Responses API

## Intent

Move the local OpenAI wrapper off Chat Completions and onto Responses API while preserving the `summarizeTicket` caller contract.

## Claimed Safety

- The caller contract should stay the same.
- The patch should stay inside the wrapper seam unless field-shape differences force a caller change.
- Validation should prove the summary text is still returned and trimmed correctly.
