from ollama import chat

MODEL = "qwen2.5-coder:14b"


def review_content(content):

    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": """
Review this output.

Check:
- bugs
- security
- scalability
- missing components

Return improved version.
"""
            },
            {
                "role": "user",
                "content": content
            }
        ]
    )

    return response["message"]["content"]