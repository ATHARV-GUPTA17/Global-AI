from ollama import chat

MODEL = "qwen2.5-coder:14b"


def generate_qa(
    goal,
    tech_stack
):

    prompt = f"""
PROJECT:
{goal}

TECH STACK:
{tech_stack}

Generate:

===FILE:test_plan.md===

===FILE:frontend_tests.md===

===FILE:backend_tests.md===

===FILE:security_tests.md===

Only file sections.
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