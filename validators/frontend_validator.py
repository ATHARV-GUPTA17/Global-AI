def validate_frontend_output(text):

    if not text:
        return False

    required = [
        "===FILE:package.json===",
    ]

    found = any(
        marker in text
        for marker in [
            "===FILE:src/App.jsx===",
            "===FILE:src/main.jsx===",
            "===FILE:src/index.css===",
            "===FILE:app/layout.tsx===",
            "===FILE:app/page.tsx===",
            "===FILE:app/globals.css===",
        ]
    )

    if not found:
        return False

    for file_marker in required:

        if file_marker not in text:
            return False

    return True