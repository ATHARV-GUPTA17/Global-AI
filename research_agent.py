from ollama import chat

MODEL = "qwen2.5-coder:7b"


def research_project(goal):

    prompt = f"""
You are a Senior Software Architect.

PROJECT:
{goal}

Choose EXACTLY ONE technology for each category.

Allowed values:

Frontend:
- React
- Next.js
- Vue

Backend:
- FastAPI
- Django
- Node.js

Database:
- PostgreSQL
- MySQL
- MongoDB

Authentication:
- JWT
- OAuth2

Security:
- OWASP Top 10 + HTTPS

DevOps:
- Docker + Nginx
- Docker + Kubernetes

Cloud:
- AWS
- Azure
- GCP

Return ONLY:

Frontend: value
Backend: value
Database: value
Authentication: value
Security: value
DevOps: value
Cloud: value

No explanations.
No markdown.
No extra text.
"""

    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]