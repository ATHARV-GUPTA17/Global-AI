from pathlib import Path
from ceo_agent import run_ceo_agent

from research_agent import research_project
from planner import create_plan
from director import determine_workers
from project_registry import register_project
from stack_parser import parse_stack

from generators.frontend_generator import generate_frontend
from generators.backend_generator import generate_backend
from generators.database_generator import generate_database
from generators.security_generator import generate_security
from generators.devops_generator import generate_devops
from manifest_generator import generate_manifest
from parsers.file_parser import save_generated_files
from validators.output_validator import (
    validate_agent_output
)
from validators.ceo_validator import (
    validate_ceo_output
)

from validators.frontend_validator import (
    validate_frontend_output
)

from validators.backend_validator import (
    validate_backend_output
)

from validators.database_validator import (
    validate_database_output
)

from validators.security_validator import (
    validate_security_output
)

from validators.devops_validator import (
    validate_devops_output
)

from validators.cyber_validator import (
    validate_cyber_output
)
from cyber_agent import run_cyber_review
from memory_agent import (
    remember_project,
    remember_stack,
    remember_history,
    remember_lesson,
    remember_improvement
)

# ==================================
# USER GOAL
# ==================================

goal = input("Project Goal: ")

# ==================================
# RESEARCH AGENT
# ==================================

stack_text = research_project(goal)

tech_stack = parse_stack(
    stack_text
)

remember_project(goal)
remember_stack(stack_text)

remember_history(
    f"Started project: {goal}"
)

print("\n===================")
print("TECH STACK")
print("===================\n")

for key, value in tech_stack.items():
    print(f"{key}: {value}")

# ==================================
# PLANNER
# ==================================

plan = create_plan(goal)

print("\n===================")
print("PROJECT PLAN")
print("===================\n")
print(plan)

# ==================================
# DIRECTOR
# ==================================

selected = determine_workers(
    goal,
    tech_stack
)

print("\n===================")
print("DIRECTOR SELECTED")
print("===================\n")
print(selected)

selected_workers = [
    x.strip().lower()
    for x in selected.split(",")
]

# ==================================
# PROJECT STRUCTURE
# ==================================

project = Path("generated_project")

folders = [
    "executive",
    "planning",
    "frontend",
    "backend",
    "database",
    "security",
    "devops",
    "cyber",
    "testing"
]

for folder in folders:
    (project / folder).mkdir(
        parents=True,
        exist_ok=True
    )
# ==================================
# CEO AGENT
# ==================================

print("\nGenerating CEO Analysis...")

ceo_output = run_ceo_agent(goal)

print("\nCEO RESPONSE")
print("=" * 60)
print(ceo_output[:3000])
print("=" * 60)

if not validate_ceo_output(ceo_output):

    print("Invalid CEO format")

    ceo_output = run_ceo_agent(goal)

success = save_generated_files(
    project / "executive",
    ceo_output
)

if success:
    print("CEO Analysis Saved")
else:
    print("CEO Analysis Save Failed")

# ==================================
# SAVE PLAN
# ==================================

with open(
    project / "planning" / "project_plan.md",
    "w",
    encoding="utf-8"
) as f:
    f.write(plan)

# ==================================
# SAVE TECH STACK
# ==================================

with open(
    project / "planning" / "tech_stack.md",
    "w",
    encoding="utf-8"
) as f:
    f.write(stack_text)

# ==================================
# REGISTER PROJECT
# ==================================

register_project(goal)
import json

manifest = generate_manifest(
    goal,
    tech_stack,
    selected_workers
)

with open(
    project / "project_manifest.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        manifest,
        f,
        indent=4
    )
# ==================================
# FRONTEND
# ==================================

if "frontend" in selected_workers:

    print("\nGenerating Frontend...")

    frontend = generate_frontend(
        goal,
        tech_stack
    )

    print("\nFRONTEND RESPONSE")
    print("=" * 60)
    print(frontend[:3000])
    print("=" * 60)

    if not validate_frontend_output(frontend):

        print("Invalid Frontend format")

        frontend = generate_frontend(
            goal,
            tech_stack
        )

    success = save_generated_files(
        project / "frontend",
        frontend
    )

    if success:
        print("Frontend Saved")
    else:
        print("Frontend Save Failed")

# ==================================
# BACKEND
# ==================================

if "backend" in selected_workers:

    print("\nGenerating Backend...")

    backend = generate_backend(
        goal,
        tech_stack
    )

    print("\nBACKEND RESPONSE")
    print("=" * 60)
    print(backend[:3000])
    print("=" * 60)

    if not validate_backend_output(backend):

        print("Invalid Backend format")

        backend = generate_backend(
            goal,
            tech_stack
        )

    success = save_generated_files(
        project / "backend",
        backend
    )

    if success:
        print("Backend Saved")
    else:
        print("Backend Save Failed")
# ==================================
# DATABASE
# ==================================

if "database" in selected_workers:

    print("\nGenerating Database...")

    database = generate_database(
        goal,
        tech_stack
    )
    if not validate_database_output(database):
        print("Invalid Database format")

        database = generate_database(
            goal,
            tech_stack
        )

    success = save_generated_files(
        project / "database",
        database
    )

    if success:
        print("Database Saved")
    else:
        print("Database Save Failed")

# ==================================
# SECURITY
# ==================================

if "security" in selected_workers:

    print("\nGenerating Security...")

    security = generate_security(
        goal,
        tech_stack
    )

    if not validate_security_output(security):

        print("Invalid Security format")

        security = generate_security(
            goal,
            tech_stack
        )

    success = save_generated_files(
        project / "security",
        security
    )

    if success:
        print("Security Saved")
    else:
        print("Security Save Failed")

# ==================================
# DEVOPS
# ==================================

if "devops" in selected_workers:

    print("\nGenerating DevOps...")

    devops = generate_devops(
        goal,
        tech_stack
    )

    print("\nDEVOPS RESPONSE")
    print("=" * 60)
    print(devops[:3000])
    print("=" * 60)

    if not validate_devops_output(devops):

        print("Invalid DevOps format")

        devops = generate_devops(
            goal,
            tech_stack
        )

    success = save_generated_files(
        project / "devops",
        devops
    )

    if success:
        print("DevOps Saved")
    else:
        print("DevOps Save Failed")

# ==================================
# CYBER AGENT
# ==================================

print("\nGenerating Cyber Review...")

cyber = run_cyber_review(
    goal,
    tech_stack
)

print("\nCYBER RESPONSE")
print("=" * 60)
print(cyber[:3000])
print("=" * 60)

attempts = 0

while not validate_cyber_output(cyber):
    attempts += 1

    print(
        f"Cyber retry {attempts}"
    )

    if attempts >= 3:
        break

    cyber = run_cyber_review(
        goal,
        tech_stack
    )

with open(
    "cyber_debug.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(cyber) 

success = save_generated_files(
    project / "cyber",
    cyber
)

if success:
    print("Cyber Review Saved")
else:
    print("Cyber Review Save Failed")
# ==================================
# SUMMARY
# ==================================
remember_improvement(
    "Need Cyber Agent integration"
)

remember_improvement(
    "Need QA Agent integration"
)
remember_history(
    f"Generated project successfully: {goal}"
)
remember_lesson(
    "Project generation pipeline completed successfully"
)

print("\n===================================")
print("PROJECT GENERATED SUCCESSFULLY")
print("===================================")

print("\nGenerated Workers:")

for worker in selected_workers:
    print(f"✓ {worker}")

print("\nProject Location:")
print(project.resolve())