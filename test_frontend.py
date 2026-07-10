from generators.frontend_generator import generate_frontend

stack = {
    "Frontend": "Next.js"
}

result = generate_frontend(
    "Build a portfolio website",
    stack
)

print("=" * 80)
print(result)
print("=" * 80)