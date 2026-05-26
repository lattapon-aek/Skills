import test from "node:test";
import assert from "node:assert/strict";

import { mapRetryPaymentStatus } from "./retry-status-mapper.ts";

test("returns SUCCEEDED for a captured retry even when a stale retry error code is still present", () => {
  assert.equal(
    mapRetryPaymentStatus({
      providerStatus: "CAPTURED",
      retryCount: 2,
      lastErrorCode: "RETRY_TIMEOUT",
    }),
    "SUCCEEDED",
  );
});

test("still returns FAILED when the provider reports FAILED", () => {
  assert.equal(
    mapRetryPaymentStatus({
      providerStatus: "FAILED",
      retryCount: 2,
      lastErrorCode: "DECLINED",
    }),
    "FAILED",
  );
});
