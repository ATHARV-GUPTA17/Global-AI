from generators.backend_generator import generate_backend

stack = {
    "Backend": "FastAPI",
    "Database": "PostgreSQL",
    "Authentication": "JWT"
}

result = generate_backend(
    "Build an AI-powered phishing detection SaaS",
    stack
)

print(result[:5000])