from ollama import chat
from output_cleaner import clean_output

MODEL = "qwen2.5-coder:14b"


def run_ceo_agent(goal):

    prompt = f"""
You are the CEO of an AI Software Company.

PROJECT:
{goal}

Analyze the business opportunity.

Generate ONLY:

===FILE:vision.md===

===FILE:market_analysis.md===

===FILE:success_metrics.md===

Rules:

- No markdown fences
- No explanations
- No notes
- Only file sections
- Response must begin with:

===FILE:vision.md===
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
            "temperature": 0.2,
            "num_ctx": 8192
        }
    )

    return clean_output(
        response["message"]["content"]
    )