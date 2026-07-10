import re
from pathlib import Path


def save_generated_files(base_folder, content):

    patterns = [
        r"===FILE:\s*(.*?)===\s*(.*?)(?=(===FILE:|$))",
        r"# FILE:\s*(.*?)\n(.*?)(?=(# FILE:|$))",
    ]

    matches = []

    for pattern in patterns:
        matches.extend(
            re.findall(
                pattern,
                content,
                re.DOTALL
            )
        )

    if not matches:
        print("No files found in response")
        return False

    for match in matches:

        filename = match[0].strip()
        file_content = match[1].strip()

        file_content = re.sub(
            r"^```[a-zA-Z]*",
            "",
            file_content
        )

        file_content = file_content.replace(
            "```",
            ""
        )

        file_path = Path(base_folder) / filename

        file_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        file_path.write_text(
            file_content,
            encoding="utf-8"
        )

        print(f"Saved: {filename}")

    return True