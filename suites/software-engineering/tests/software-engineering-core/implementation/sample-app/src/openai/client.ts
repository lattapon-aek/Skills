export type ChatMessage = {
  role: "system" | "user" | "assistant";
  content: string;
};

export type ResponsesCreateInput = {
  model: string;
  instructions?: string;
  input: Array<{
    role: "user" | "assistant";
    content: string;
  }>;
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
  const [firstMessage, ...remainingMessages] = messages;
  const instructions =
    firstMessage?.role === "system" ? firstMessage.content : undefined;
  const inputMessages =
    firstMessage?.role === "system" ? remainingMessages : messages;

  const response = await client.responses.create({
    model,
    instructions,
    input: inputMessages.map((message) => ({
      role: message.role === "assistant" ? "assistant" : "user",
      content: message.content,
    })),
    store: false,
  });

  return response.output_text.trim();
}
