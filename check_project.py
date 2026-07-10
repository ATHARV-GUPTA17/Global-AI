import py_compile

files = [
    "project_builder.py",

    "research_agent.py",
    "planner.py",
    "director.py",
    "cyber_agent.py",

    "stack_parser.py",
    "output_cleaner.py",

    "generators/frontend_generator.py",
    "generators/backend_generator.py",
    "generators/database_generator.py",
    "generators/security_generator.py",
    "generators/devops_generator.py",

    "validators/output_validator.py",

    "memory_agent.py",
    "project_registry.py",
    "manifest_generator.py"
]

print("\nChecking files...\n")

failed = []

for file in files:
    try:
        py_compile.compile(
            file,
            doraise=True
        )

        print(f"[OK] {file}")

    except Exception as e:

        print(f"[FAILED] {file}")
        print(e)

        failed.append(file)

print("\n====================")

if failed:

    print("FAILED FILES:\n")

    for f in failed:
        print(f)

else:

    print("ALL FILES PASSED")

print("====================")