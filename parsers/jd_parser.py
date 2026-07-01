from pathlib import Path


def read_jd_text(file_path):

    path = Path(file_path)

    return path.read_text(
        encoding="utf-8",
        errors="ignore"
    )