from ollama import chat

MODEL = "qwen2.5-coder:7b"

goal = input("Goal: ")

response = chat(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": """
You are a Director.

Determine which specialists are needed.

Return only a list.
"""
        },
        {
            "role": "user",
            "content": goal
        }
    ]
)

print(response["message"]["content"])