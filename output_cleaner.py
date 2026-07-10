import re


def clean_output(text):

    text = re.sub(
        r"```[a-zA-Z]*",
        "",
        text
    )

    text = text.replace(
        "```",
        ""
    )

    return text.strip()