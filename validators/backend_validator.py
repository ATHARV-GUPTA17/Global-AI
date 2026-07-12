def validate_backend_output(text):

    if not text:
        return False

    required = [
        "===FILE:.env.example===",
        "===FILE:requirements.txt===",
        "===FILE:main.py===",
        "===FILE:database.py===",
        "===FILE:models.py===",
        "===FILE:routes.py===",
        "===FILE:jwt_auth.py===",
    ]

    for file_marker in required:

        if file_marker not in text:
            print(
                f"Missing backend file: {file_marker}"
            )
            return False

    return True