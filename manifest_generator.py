from datetime import datetime


def generate_manifest(
    goal,
    tech_stack,
    selected_workers
):

    return {
        "project_name": goal,

        "created_at": str(
            datetime.now()
        ),

        "tech_stack": tech_stack,

        "workers": selected_workers,

        "features": [],

        "frontend": tech_stack.get(
            "Frontend"
        ),

        "backend": tech_stack.get(
            "Backend"
        ),

        "database": tech_stack.get(
            "Database"
        ),

        "authentication": tech_stack.get(
            "Authentication"
        ),

        "security": tech_stack.get(
            "Security"
        ),

        "cloud": tech_stack.get(
            "Cloud"
        )
    }