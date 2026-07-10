from ollama import chat
from output_cleaner import clean_output

MODEL = "qwen2.5-coder:14b"


def generate_security(goal, tech_stack):

    prompt = f"""
You are a Senior Application Security Architect.

PROJECT:
{goal}

TECH STACK:
{tech_stack}

Generate production-ready security documentation.

Required files:

===FILE:security.md===

===FILE:threat_model.md===

===FILE:checklist.md===

CRITICAL RULES:

If you output markdown fences (```), the response is invalid.

If you output explanations before the first file,
the response is invalid.

If you output explanations after the last file,
the response is invalid.

Generate realistic security documentation based on the project.

Include:

- Authentication security
- Authorization security
- Data protection
- OWASP Top 10 mitigation
- API security
- Infrastructure security
- Incident response
- Security checklist

Output ONLY file sections.

Do NOT explain anything.

Do NOT include notes.

Do NOT include markdown.

Do NOT include code fences.

Response MUST begin with:

===FILE:security.md===
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