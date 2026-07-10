import re

def validate_agent_output(text):

    if not text:
        return False

    patterns = [
        r"===FILE:",
        r"# FILE:",
        r"==FILE:"
    ]

    for pattern in patterns:

        matches = re.findall(
            pattern,
            text
        )

        if len(matches) >= 1:
            return True

    return False