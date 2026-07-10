from ollama import chat
from pathlib import Path
from datetime import datetime

MODEL = "qwen2.5-coder:7b"

def ask(system, prompt):
    response = chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ]
    )
    return response["message"]["content"]

goal = input("\nGOAL:\n> ")

print("\n[1/4] Director Thinking...\n")

director = ask(
    "You are an AI Director. Break goals into executable tasks.",
    goal
)

print(director)

print("\n[2/4] Analyzer Thinking...\n")

analysis = ask(
    "You are an AI Business and Technical Analyst. Analyze the project deeply.",
    director
)

print(analysis)

print("\n[3/4] Worker Executing...\n")

work = ask(
    "You are a world-class execution agent. Produce the deliverables.",
    analysis
)

print(work)

print("\n[4/4] Reviewer Reviewing...\n")

review = ask(
    "You are a strict reviewer. Improve and finalize the result.",
    work
)

print(review)

Path("outputs").mkdir(exist_ok=True)

filename = f"outputs/{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"

with open(filename, "w", encoding="utf-8") as f:
    f.write("# GOAL\n\n")
    f.write(goal)
    f.write("\n\n# DIRECTOR\n\n")
    f.write(director)
    f.write("\n\n# ANALYSIS\n\n")
    f.write(analysis)
    f.write("\n\n# WORK\n\n")
    f.write(work)
    f.write("\n\n# REVIEW\n\n")
    f.write(review)

print(f"\nSaved: {filename}")