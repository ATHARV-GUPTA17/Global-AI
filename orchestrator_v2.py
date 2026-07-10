from ollama import chat
from pathlib import Path
import re

MODEL = "qwen2.5-coder:7b"

goal = input("\nPROJECT GOAL:\n> ")

safe_name = re.sub(
    r"[^a-zA-Z0-9_-]",
    "-",
    goal.lower()
)

project_path = Path("projects") / safe_name

folders = [
    "research",
    "frontend",
    "backend",
    "database",
    "security",
    "devops",
    "documentation"
]

for folder in folders:
    (project_path / folder).mkdir(
        parents=True,
        exist_ok=True
    )

workers = {

    "research": """
Research technologies, competitors,
best practices and recommendations.
""",

    "frontend": """
Create frontend architecture.

Generate:
- UI Structure
- Pages
- Components
- HTML Example
""",

    "backend": """
Create backend architecture.

Generate:
- FastAPI structure
- Endpoints
- Authentication
- Database integration
""",

    "database": """
Create PostgreSQL schema.

Generate:
- Tables
- Relationships
- SQL
""",

    "security": """
Perform security review.

Generate:
- Threat model
- OWASP checklist
- Security controls
""",

    "devops": """
Generate deployment strategy.

Generate:
- Docker
- CI/CD
- Hosting
- Monitoring
"""
}

for worker, system_prompt in workers.items():

    print(f"\nRunning {worker} worker...")

    response = chat(
        model=MODEL,
        messages=[
            {
                "role":"system",
                "content":system_prompt
            },
            {
                "role":"user",
                "content":goal
            }
        ]
    )

    result = response["message"]["content"]

    file_path = project_path / worker / f"{worker}.md"

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as f:
        f.write(result)

    print(f"Saved: {file_path}")

print("\nProject Generation Complete")