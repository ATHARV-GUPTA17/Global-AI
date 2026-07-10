from ollama import chat

MODEL = "qwen2.5-coder:7b"

def determine_workers(goal, tech_stack):

    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": """
You are an AI Project Director.

Available workers:

frontend
backend
database
security
devops

Analyze the user's goal.

Return ONLY comma-separated worker names.

Examples:

Goal: Portfolio Website
Answer: frontend

Goal: Java Calculator
Answer: backend

Goal: AI SaaS Platform
Answer: frontend,backend,database,security,devops
"""
            },
            {
                "role": "user",
                "content": goal
            }
        ]
    )

    return response["message"]["content"].strip()