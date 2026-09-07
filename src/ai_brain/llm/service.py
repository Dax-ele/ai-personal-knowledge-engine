import ollama


class LLMService:
    def __init__(self, model="qwen2.5:3b"):
        self.model = model

    def generate(self, prompt):
        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]


if __name__ == "__main__":
    service = LLMService()

    response = service.generate(
        "Spiegami in una frase cos'è Python."
    )

    print(response)