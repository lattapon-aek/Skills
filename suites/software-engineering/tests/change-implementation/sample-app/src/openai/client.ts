export type ChatMessage = {
  role: "system" | "user" | "assistant";
  content: string;
};

export type ResponsesCreateInput = {
  model: string;
  input: ChatMessage[];
  store: false;
};

export type OpenAIClient = {
  responses: {
    create(input: ResponsesCreateInput): Promise<{
      output_text: string;
    }>;
  };
};

export async function createSummary(
  client: OpenAIClient,
  model: string,
  messages: ChatMessage[],
): Promise<string> {
  const response = await client.responses.create({
    model,
    input: messages,
    store: false,
  });

  return response.output_text.trim();
}
