import json
from pathlib import Path

MEMORY_DIR = Path("memory")


def load_memory(filename):
    file = MEMORY_DIR / filename

    if not file.exists():
        return []

    try:
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


def save_memory(filename, data):
    file = MEMORY_DIR / filename

    with open(file, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            indent=4
        )


# ==================================
# PROJECTS
# ==================================

def remember_project(goal):

    projects = load_memory(
        "projects.json"
    )

    projects.append(
        {
            "project": goal
        }
    )

    save_memory(
        "projects.json",
        projects
    )


# ==================================
# STACKS
# ==================================

def remember_stack(stack):

    stacks = load_memory(
        "stacks.json"
    )

    stacks.append(
        {
            "stack": stack
        }
    )

    save_memory(
        "stacks.json",
        stacks
    )


# ==================================
# LESSONS
# ==================================

def remember_lesson(text):

    lessons = load_memory(
        "lessons.json"
    )

    lessons.append(
        {
            "lesson": text
        }
    )

    save_memory(
        "lessons.json",
        lessons
    )


# ==================================
# IMPROVEMENTS
# ==================================

def remember_improvement(text):

    improvements = load_memory(
        "improvements.json"
    )

    improvements.append(
        {
            "improvement": text
        }
    )

    save_memory(
        "improvements.json",
        improvements
    )


# ==================================
# HISTORY
# ==================================

def remember_history(text):

    history = load_memory(
        "history.json"
    )

    history.append(
        {
            "event": text
        }
    )

    save_memory(
        "history.json",
        history
    )


# ==================================
# KNOWLEDGE
# ==================================

def remember_knowledge(text):

    knowledge = load_memory(
        "knowledge.json"
    )

    knowledge.append(
        {
            "knowledge": text
        }
    )

    save_memory(
        "knowledge.json",
        knowledge
    )


# ==================================
# READ HELPERS
# ==================================

def get_projects():
    return load_memory("projects.json")


def get_stacks():
    return load_memory("stacks.json")


def get_lessons():
    return load_memory("lessons.json")


def get_improvements():
    return load_memory("improvements.json")


def get_history():
    return load_memory("history.json")


def get_knowledge():
    return load_memory("knowledge.json")