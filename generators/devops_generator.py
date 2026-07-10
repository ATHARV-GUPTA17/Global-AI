from ollama import chat
from output_cleaner import clean_output

MODEL = "qwen2.5-coder:14b"


def generate_devops(goal, tech_stack):

    devops = tech_stack.get(
        "DevOps",
        "Docker + Nginx"
    )

    cloud = tech_stack.get(
        "Cloud",
        "AWS"
    )

    prompt = f"""
You are a Senior DevOps Engineer.

PROJECT:
{goal}

DEVOPS:
{devops}

CLOUD:
{cloud}

Generate production-ready deployment infrastructure.

Required files:

===FILE:Dockerfile===

===FILE:docker-compose.yml===

===FILE:nginx.conf===

===FILE:deployment.md===

CRITICAL RULES:

If you output markdown fences (```), the response is invalid.

If you output explanations before the first file,
the response is invalid.

If you output explanations after the last file,
the response is invalid.

Generate realistic deployment infrastructure.

Include:

- Docker containerization
- Reverse proxy configuration
- Environment variables
- Production deployment steps
- Security best practices

Output ONLY file sections.

Do NOT explain anything.

Do NOT include notes.

Do NOT include markdown.

Do NOT include code fences.

Response MUST begin with:

===FILE:Dockerfile===
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