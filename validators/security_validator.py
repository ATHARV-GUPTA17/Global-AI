def validate_security_output(text):

    if not text:
        return False

    required = [
        "===FILE:security.md===",
        "===FILE:threat_model.md===",
        "===FILE:checklist.md===",
    ]

    return all(
        item in text
        for item in required
    )