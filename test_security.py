from generators.security_generator import generate_security

result = generate_security(
    "AI Phishing SaaS",
    "React + FastAPI + PostgreSQL"
)

print(result[:2000])