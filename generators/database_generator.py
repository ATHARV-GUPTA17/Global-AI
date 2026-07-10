from ollama import chat
from output_cleaner import clean_output

MODEL = "qwen2.5-coder:14b"


def generate_database(goal, tech_stack):

    database = tech_stack.get(
        "Database",
        "PostgreSQL"
    )

    prompt = f"""
You are a Senior Database Architect.

PROJECT:
{goal}

Database:
{database}

Generate a production-ready database design.

Required files:

===FILE:schema.sql===

===FILE:seed.sql===

===FILE:migrations.sql===

CRITICAL RULES:

If you output markdown fences (```), the response is invalid.

If you output placeholder table names such as:

table1
users_table
example_table

the response is invalid.

Generate realistic schema based on the project.

Include:
- Primary keys
- Foreign keys
- Indexes
- Constraints
- Timestamps

Output ONLY file sections.

Do NOT explain anything.

Do NOT include notes.

Do NOT include markdown.

Response MUST begin with:

===FILE:schema.sql===

Response MUST contain ALL files:

===FILE:schema.sql===

===FILE:seed.sql===

===FILE:migrations.sql===

If any file is missing, the response is invalid.
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