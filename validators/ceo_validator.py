def validate_ceo_output(text):

    if not text:
        return False

    required = [
        "===FILE:vision.md===",
        "===FILE:market_analysis.md===",
        "===FILE:success_metrics.md===",
    ]

    return all(
        item in text
        for item in required
    )