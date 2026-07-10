from ollama import chat
from pathlib import Path

MODEL = "qwen2.5-coder:7b"

workers = {
    "research_worker": "Research technologies, competitors and best practices",
    "frontend_worker": "Create frontend architecture and UI plan",
    "backend_worker": "Create backend architecture and API plan",
    "database_worker": "Create database schema and storage plan",
    "security_worker": "Create security assessment and recommendations",
    "devops_worker": "Create deployment and DevOps strategy"
}

goal = input("\nPROJECT GOAL:\n> ")

Path("outputs").mkdir(exist_ok=True)

for worker, system_prompt in workers.items():

    print(f"\nRunning {worker}")

    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": goal
            }
        ]
    )

    result = response["message"]["content"]

    file_path = f"outputs/{worker}.md"

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as f:
        f.write(result)

    print(f"Saved: {file_path}")

print("\nALL WORKERS COMPLETED")