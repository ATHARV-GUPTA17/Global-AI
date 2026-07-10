from ollama import chat

MODEL = "qwen2.5-coder:14b"


def review_project(
    goal,
    generated_content
):

    prompt = f"""
You are a Senior Software Reviewer.

PROJECT:
{goal}

CONTENT:
{generated_content}

Review for:

- Syntax errors
- Missing imports
- Missing files
- Broken references
- Placeholder credentials
- Security issues

Return:

===FILE:review.md===

Review report only.
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