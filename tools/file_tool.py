from pathlib import Path

def read_file(path):
    try:
        return Path(path).read_text(encoding="utf-8")
    except Exception as e:
        return str(e)

def write_file(path, content):
    Path(path).parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    return f"Saved: {path}"

def append_file(path, content):
    with open(path, "a", encoding="utf-8") as f:
        f.write(content)

    return f"Updated: {path}"