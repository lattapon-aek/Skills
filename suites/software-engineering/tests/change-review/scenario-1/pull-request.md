# PR Summary

Surface retry failures more aggressively in payment status mapping so support can see retry-related problems earlier.

## Claimed intent

- If a payment payload still carries a `lastErrorCode`, mark it as `FAILED`
- Keep the current provider `FAILED` handling
- Keep tests aligned with the new behavior
