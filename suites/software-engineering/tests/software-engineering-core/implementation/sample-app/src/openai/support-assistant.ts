import { createSummary, type OpenAIClient } from "./client.ts";

export async function summarizeTicket(
  client: OpenAIClient,
  transcript: string,
): Promise<string> {
  return createSummary(client, "gpt-4o-mini", [
    {
      role: "system",
      content: "Summarize the support ticket in exactly three bullet points.",
    },
    {
      role: "user",
      content: transcript,
    },
  ]);
}
