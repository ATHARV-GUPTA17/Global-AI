from ollama import chat

MODEL = "qwen2.5-coder:7b"


def select_stack(goal):

    prompt = f"""
Project:
{goal}

Choose EXACTLY ONE:

Frontend
Backend
Database
Authentication
DevOps
Cloud

Return format:

Frontend: React
Backend: FastAPI
Database: PostgreSQL
Authentication: JWT
DevOps: Docker
Cloud: AWS
"""

    response = chat(
        model=MODEL,
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response["message"]["content"]