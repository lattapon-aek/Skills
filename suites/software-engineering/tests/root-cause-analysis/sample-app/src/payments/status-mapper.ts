export type ProviderStatus = "AUTHORIZED" | "CAPTURED" | "FAILED";
export type InternalStatus = "PENDING" | "SUCCEEDED" | "FAILED";

export type PaymentPayload = {
  providerStatus: ProviderStatus;
  captureCount: number;
  lastErrorCode?: string;
};

export function mapPaymentStatus(payload: PaymentPayload): InternalStatus {
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
