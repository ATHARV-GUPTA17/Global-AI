from pathlib import Path


def validate_saved_file(path):

    file_path = Path(path)

    if not file_path.exists():
        return False

    if file_path.stat().st_size == 0:
        return False

    return True