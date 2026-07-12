def validate_devops_output(text):

    if not text:
        return False

    required = [
        "===FILE:Dockerfile===",
        "===FILE:docker-compose.yml===",
        "===FILE:nginx.conf===",
        "===FILE:deployment.md===",
    ]

    return all(
        item in text
        for item in required
    )