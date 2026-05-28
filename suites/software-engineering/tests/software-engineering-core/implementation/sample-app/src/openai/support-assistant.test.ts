import test from "node:test";
import assert from "node:assert/strict";

import { summarizeTicket } from "./support-assistant.ts";

test("summarizeTicket preserves the caller contract while trimming the final text", async () => {
  const calls: Array<{
    model: string;
    instructions?: string;
    input: Array<{ role: string; content: string }>;
    store: false;
  }> = [];

  const client = {
    responses: {
      create: async (input: {
        model: string;
        instructions?: string;
        input: Array<{ role: string; content: string }>;
        store: false;
      }) => {
        calls.push(input);
        return {
          output_text:
            "- customer could not retry payment\n- provider later captured successfully\n- dashboard still showed failed\n",
        };
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
  assert.equal(
    calls[0]?.instructions,
    "Summarize the support ticket in exactly three bullet points.",
  );
  assert.equal(calls[0]?.store, false);
  assert.equal(calls[0]?.input[0]?.role, "user");
  assert.equal(
    calls[0]?.input[0]?.content,
    "Customer reports that the payment eventually captured but the dashboard still showed failed.",
  );
});
