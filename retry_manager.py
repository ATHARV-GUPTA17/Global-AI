import re

MAX_RETRIES = 3


def valid_response(content):

    if not content:
        return False

    if "===FILE:" not in content:
        return False

    if "```" in content:
        return False

    matches = re.findall(
        r"===FILE:(.*?)===",
        content
    )

    if len(matches) == 0:
        return False

    return True


def generate_with_retry(
    generator,
    goal,
    tech_stack,
    validator,
    retries=MAX_RETRIES
):

    for attempt in range(retries):

        result = generator(
            goal,
            tech_stack
        )

        if validator(result):

            print(
                f"Valid output on attempt {attempt + 1}"
            )

            return result

        print(
            f"Retry {attempt + 1}/{retries}"
        )

    return result