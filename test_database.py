from generators.database_generator import generate_database

stack = {
    "Database": "PostgreSQL"
}

result = generate_database(
    "Build an AI-powered phishing detection SaaS",
    stack
)

print(result)