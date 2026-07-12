def validate_database_output(text):

    if not text:
        return False

    required = [
        "===FILE:schema.sql===",
        "===FILE:seed.sql===",
        "===FILE:migrations.sql===",
    ]

    return all(
        item in text
        for item in required
    )