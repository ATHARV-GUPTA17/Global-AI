import json
from pathlib import Path

REGISTRY = Path("memory/projects.json")

def register_project(project_name):

    try:
        projects = json.loads(
            REGISTRY.read_text(
                encoding="utf-8"
            )
        )
    except:
        projects = []

    projects.append(project_name)

    REGISTRY.write_text(
        json.dumps(projects, indent=2),
        encoding="utf-8"
    )