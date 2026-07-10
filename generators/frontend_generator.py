from ollama import chat
from output_cleaner import clean_output

MODEL = "qwen2.5-coder:14b"


def generate_frontend(goal, tech_stack):

    frontend = tech_stack.get(
        "Frontend",
        "React"
    )

    if frontend == "Next.js":

        prompt = f"""
You are a Senior Next.js Developer.

PROJECT:
{goal}

Generate a COMPLETE production-ready Next.js application.

Build the actual application described in PROJECT.

Do not generate create-next-app examples.

Do not generate starter templates.

Do not generate placeholder pages.

Do not generate "Welcome to Next.js".

Do not generate "Deploy", "Docs", "Learn", or example content.

Every page must be specific to the project goal.

The application must look like a real SaaS product.

Generate business-specific UI and functionality.

RETURN FILES EXACTLY IN THIS FORMAT:

===FILE:package.json===

===FILE:next.config.js===

===FILE:app/layout.tsx===

===FILE:app/page.tsx===

===FILE:app/globals.css===

CRITICAL RULES:

1. Every file must start with:
===FILE:filename===

2. No markdown

3. No code fences

4. No explanations

5. Output only file sections

6. Response must start with:
===FILE:package.json===
"""

    else:

        prompt = f"""
You are a Senior React Developer.

PROJECT:
{goal}

Generate a COMPLETE production-ready React application.

Build the actual application described in PROJECT.

Generate business-specific UI and functionality.

RETURN FILES EXACTLY IN THIS FORMAT:

===FILE:package.json===

===FILE:src/App.jsx===

===FILE:src/main.jsx===

===FILE:src/index.css===

CRITICAL RULES:

1. Every file must start with:
===FILE:filename===

2. No markdown

3. No code fences

4. No explanations

5. Output only file sections

6. Response must start with:
===FILE:package.json===
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