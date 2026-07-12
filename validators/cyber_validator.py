def validate_cyber_output(text):

    if not text:
        return False

    required = [
        "===FILE:threat_model.md===",
        "===FILE:attack_surface.md===",
        "===FILE:owasp_review.md===",
        "===FILE:auth_review.md===",
        "===FILE:security_controls.md===",
        "===FILE:incident_response.md===",
    ]

    return all(
        item in text
        for item in required
    )