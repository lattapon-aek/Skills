import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";

import { mapPaymentStatus } from "./status-mapper.ts";

test("returns SUCCEEDED for the captured payment from the incident payload", () => {
  const payloadPath = path.resolve(
    import.meta.dirname,
    "../../incidents/payment-status/payload.json",
  );
  const payload = JSON.parse(fs.readFileSync(payloadPath, "utf8"));

  assert.equal(mapPaymentStatus(payload), "SUCCEEDED");
});

test("still returns FAILED when the provider reports FAILED", () => {
  assert.equal(
    mapPaymentStatus({
      providerStatus: "FAILED",
      captureCount: 0,
      lastErrorCode: "DECLINED",
    }),
    "FAILED",
  );
});
