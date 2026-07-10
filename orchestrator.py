from ollama import chat
from pathlib import Path
from datetime import datetime
import json
import re

from tools.tool_manager import ToolManager

tm = ToolManager()

MODEL = "qwen2.5-coder:7b"


def ask(system, prompt):

    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": system
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


goal = input("\nGOAL:\n> ")

# Create project structure automatically
project_path = tm.create_project(goal)

print(f"\nProject Created: {project_path}")

# =====================
# DIRECTOR
# =====================

print("\n[1] DIRECTOR\n")

director = ask(
    """
You are an AI Director.

Break this goal into major tasks.

Return a structured plan.
    """,
    goal
)

print(director)

tm.write(
    f"{project_path}/research/director_plan.md",
    director
)

# =====================
# ANALYZER
# =====================

print("\n[2] ANALYZER\n")

analysis = ask(
    """
You are a senior business and technical analyst.

Analyze:

- Business requirements
- Technical requirements
- Risks
- Recommended technologies
    """,
    goal
)

print(analysis)

tm.write(
    f"{project_path}/architecture/analysis.md",
    analysis
)

# =====================
# WORKER
# =====================

print("\n[3] WORKER\n")

work = ask(
    """
You are a senior execution specialist.

Create detailed deliverables.
    """,
    goal + "\n\n" + analysis
)

print(work)

tm.write(
    f"{project_path}/development/work.md",
    work
)

# =====================
# REVIEWER
# =====================

print("\n[4] REVIEWER\n")

review = ask(
    """
You are a senior reviewer.

Improve:
- Quality
- Security
- Scalability
- Maintainability

Return the final improved version.
    """,
    work
)

print(review)

tm.write(
    f"{project_path}/documentation/final_report.md",
    review
)

# =====================
# MEMORY
# =====================

history_file = Path("memory/history.json")

try:
    history = json.loads(
        history_file.read_text(
            encoding="utf-8"
        )
    )
except:
    history = []

history.append({
    "timestamp": datetime.now().isoformat(),
    "goal": goal,
    "project": project_path
})

history_file.write_text(
    json.dumps(history, indent=2),
    encoding="utf-8"
)

print("\n===================")
print("PROJECT COMPLETED")
print("===================")

print(f"\nSaved to: {project_path}")