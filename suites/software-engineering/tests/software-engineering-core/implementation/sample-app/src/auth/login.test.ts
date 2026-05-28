import test from "node:test";
import assert from "node:assert/strict";

import { login } from "./login.ts";

test("login locks users with five or more failed attempts before credential matching", () => {
  const lockedByAttempts = login(
    {
      id: "u-1",
      password: "correct-horse-battery-staple",
      failedAttempts: 5,
      locked: false,
    },
    "wrong-password",
  );

  assert.deepEqual(lockedByAttempts, { ok: false, reason: "LOCKED" });
});

test("login still rejects bad credentials below the lock threshold", () => {
  const invalidCredentials = login(
    {
      id: "u-2",
      password: "correct-horse-battery-staple",
      failedAttempts: 4,
      locked: false,
    },
    "wrong-password",
  );

  assert.deepEqual(invalidCredentials, {
    ok: false,
    reason: "INVALID_CREDENTIALS",
  });
});

