from ollama import chat
from output_cleaner import clean_output

MODEL = "qwen2.5-coder:14b"


def generate_backend(goal, tech_stack):

    backend = tech_stack.get(
        "Backend",
        "FastAPI"
    )

    database = tech_stack.get(
        "Database",
        "PostgreSQL"
    )

    auth = tech_stack.get(
        "Authentication",
        "JWT"
    )

    prompt = f"""
You are a Senior Backend Engineer.

PROJECT:
{goal}

Backend Technology:
{backend}

Database:
{database}

Authentication:
{auth}

Generate a production-ready backend.

Required files:

===FILE:.env.example===

===FILE:requirements.txt===

===FILE:main.py===

===FILE:database.py===

===FILE:models.py===

===FILE:routes.py===

===FILE:jwt_auth.py===

CRITICAL RULES:

If you output markdown fences (```), the response is invalid.

If you output placeholder values such as:

your_secret_key
password
localhost
example.com

the response is invalid.

Use environment variable placeholders only.

Example:

DATABASE_URL=${{DATABASE_URL}}
SECRET_KEY=${{SECRET_KEY}}

Output ONLY file sections.

Do NOT explain anything.

Do NOT include notes.

Do NOT include markdown.

Response MUST begin with:

===FILE:.env.example===
"""

    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": 0.1,
            "num_ctx": 16384,
            "stop": [
                "Explanation:",
                "Notes:",
                "Summary:"
            ]
        }
    )

    return clean_output(
        response["message"]["content"]
    )