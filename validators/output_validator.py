import re


def validate_agent_output(text):

    if not text:
        return False

    files = re.findall(
        r"===FILE:(.*?)===",
        text,
        re.DOTALL
    )

    if not files:
        return False

    sections = text.count("===FILE:")

    if sections != len(files):
        return False

    return True