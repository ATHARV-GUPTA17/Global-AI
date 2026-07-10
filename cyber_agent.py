from ollama import chat

MODEL = "qwen2.5-coder:14b"


def run_cyber_review(goal, tech_stack):

    prompt = f"""
You are a Senior Cybersecurity Architect.

PROJECT:
{goal}

TECH STACK:
{tech_stack}

Generate a professional security review.

RETURN EXACTLY:

===FILE:threat_model.md===
Threat model

===FILE:attack_surface.md===
Attack surface analysis

===FILE:owasp_review.md===
OWASP review

===FILE:auth_review.md===
Authentication review

===FILE:security_controls.md===
Security controls

===FILE:incident_response.md===
Incident response plan

RULES:

- ONLY file sections
- NO markdown code fences
- NO explanations
- NO headings outside files
- DO NOT write:
  ### Threat Model
  ### Attack Surface
- ALWAYS use:
  ===FILE:filename===
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