export type ProviderStatus = "AUTHORIZED" | "CAPTURED" | "FAILED";
export type InternalStatus = "PENDING" | "SUCCEEDED" | "FAILED";

export type RetryPaymentPayload = {
  providerStatus: ProviderStatus;
  retryCount: number;
  lastErrorCode?: string;
};

export function mapRetryPaymentStatus(
  payload: RetryPaymentPayload,
): InternalStatus {
  if (payload.providerStatus === "CAPTURED") {
    return "SUCCEEDED";
  }

  if (payload.lastErrorCode) {
    return "FAILED";
  }

  if (payload.providerStatus === "FAILED") {
    return "FAILED";
  }

  return "PENDING";
}
