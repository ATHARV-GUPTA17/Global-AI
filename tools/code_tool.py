from ollama import chat

MODEL = "qwen2.5-coder:7b"

def generate_code(prompt):

    response = chat(
        model=MODEL,
        messages=[
            {
                "role":"system",
                "content":"You are a senior software engineer."
            },
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response["message"]["content"]