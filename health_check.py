from generators.frontend_generator import generate_frontend
from generators.backend_generator import generate_backend
from generators.database_generator import generate_database
from generators.security_generator import generate_security
from generators.devops_generator import generate_devops

stack = {
    "Frontend": "Next.js",
    "Backend": "FastAPI",
    "Database": "PostgreSQL",
    "Authentication": "JWT",
    "Security": "OWASP Top 10 + HTTPS",
    "DevOps": "Docker + Nginx",
    "Cloud": "AWS"
}

goal = "Build an AI-powered phishing detection SaaS"

tests = [
    ("Frontend", generate_frontend),
    ("Backend", generate_backend),
    ("Database", generate_database),
    ("Security", generate_security),
    ("DevOps", generate_devops),
]

for name, func in tests:

    print(f"\nTesting {name}...")

    try:

        result = func(goal, stack)

        if "===FILE:" in result:
            print(f"[PASS] {name}")
        else:
            print(f"[FAIL] {name}")

    except Exception as e:

        print(f"[ERROR] {name}")
        print(e)