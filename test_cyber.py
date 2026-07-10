from cyber_agent import run_cyber_review

stack = {
    "Frontend": "React",
    "Backend": "FastAPI",
    "Database": "PostgreSQL",
    "Authentication": "JWT",
    "Security": "OWASP Top 10 + HTTPS",
    "DevOps": "Docker + Nginx",
    "Cloud": "AWS"
}

result = run_cyber_review(
    "Build an AI-powered phishing detection SaaS",
    stack
)

print(result)