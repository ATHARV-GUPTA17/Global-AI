from pathlib import Path
import re

def create_project(project_name):

    safe = re.sub(
        r"[^a-zA-Z0-9_-]",
        "-",
        project_name.lower()
    )

    base = Path("projects") / safe

    folders = [
        "research",
        "architecture",
        "development",
        "security",
        "deployment",
        "documentation"
    ]

    for folder in folders:
        (base / folder).mkdir(
            parents=True,
            exist_ok=True
        )

    return str(base)