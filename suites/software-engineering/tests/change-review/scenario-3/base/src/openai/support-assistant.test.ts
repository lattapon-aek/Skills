import test from "node:test";
import assert from "node:assert/strict";

import { summarizeTicket } from "./support-assistant.ts";

test("summarizeTicket preserves the caller contract while trimming the final text", async () => {
  const calls: Array<{
    model: string;
    messages: Array<{ role: string; content: string }>;
  }> = [];

  const client = {
    chat: {
      completions: {
        create: async (input: {
          model: string;
          messages: Array<{ role: string; content: string }>;
        }) => {
          calls.push(input);
          return {
            content: "- customer could not retry payment\n- provider later captured successfully\n- dashboard still showed failed\n",
          };
        },
      },
    },
  };

  const summary = await summarizeTicket(
    client,
    "Customer reports that the payment eventually captured but the dashboard still showed failed.",
  );

  assert.equal(
    summary,
    "- customer could not retry payment\n- provider later captured successfully\n- dashboard still showed failed",
  );
  assert.equal(calls[0]?.model, "gpt-4o-mini");
  assert.equal(calls[0]?.messages[0]?.role, "system");
  assert.equal(calls[0]?.messages[1]?.role, "user");
});
