import ollama


response = ollama.chat(
    model="qwen2.5:3b",
    messages=[
        {
            "role": "user",
            "content": "Spiegami in una frase cos'è Python."
        }
    ]
)

print(response["message"]["content"])