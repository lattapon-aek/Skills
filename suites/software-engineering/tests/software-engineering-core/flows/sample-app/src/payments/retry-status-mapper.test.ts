import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";

import { mapRetryPaymentStatus } from "./retry-status-mapper.ts";

const incidentDir = path.resolve(import.meta.dirname, "../../incidents/payment-retry");

test("does not reproduce the incident's FAILED dashboard status for the captured retry payload", () => {
  const incidentLogPath = path.join(incidentDir, "incident.log");
  const incidentLog = fs.readFileSync(incidentLogPath, "utf8");
  const incidentStatusMatch = incidentLog.match(/internal_status=(\w+)/);

  assert.equal(incidentStatusMatch?.[1], "FAILED");

  const payloadPath = path.join(incidentDir, "payload.json");
  const payload = JSON.parse(fs.readFileSync(payloadPath, "utf8"));

  assert.notEqual(mapRetryPaymentStatus(payload), incidentStatusMatch?.[1]);
  assert.equal(mapRetryPaymentStatus(payload), "SUCCEEDED");
});

test("returns SUCCEEDED for a captured retry even when a stale retry error code is still present", () => {
  const payloadPath = path.resolve(
    incidentDir,
    "payload.json",
  );
  const payload = JSON.parse(fs.readFileSync(payloadPath, "utf8"));

  assert.equal(mapRetryPaymentStatus(payload), "SUCCEEDED");
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
