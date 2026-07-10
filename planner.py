from ollama import chat

MODEL = "qwen2.5-coder:7b"

def create_plan(goal):

    response = chat(
        model=MODEL,
        messages=[
            {
                "role":"system",
                "content":"""
You are a Project Planner.

Break the project into tasks.

Return only a numbered task list.
"""
            },
            {
                "role":"user",
                "content":goal
            }
        ]
    )

    return response["message"]["content"]