export type ChatMessage = {
  role: "system" | "user" | "assistant";
  content: string;
};

export type ChatCompletionResponse = {
  content: string;
};

export type OpenAIClient = {
  chat: {
    completions: {
      create(input: {
        model: string;
        messages: ChatMessage[];
      }): Promise<ChatCompletionResponse>;
    };
  };
};

export async function createSummary(
  client: OpenAIClient,
  model: string,
  messages: ChatMessage[],
): Promise<string> {
  const response = await client.chat.completions.create({
    model,
    messages,
  });

  return response.content.trim();
}
