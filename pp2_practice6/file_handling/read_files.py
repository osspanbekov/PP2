from __future__ import annotations

from pathlib import Path


def main() -> None:
    """
    Читает и печатает содержимое текстового файла.
    Рекомендуется сначала выполнить write_files.py.
    """

    base_dir = Path(__file__).resolve().parent
    file_path = base_dir / "data" / "sample.txt"

    try:
        content = file_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Missing file: {file_path}")
        print("Run `python pp2_practice6/file_handling/write_files.py` first.")
        return

    print(f"Reading: {file_path}")
    print("--- File content ---")
    print(content, end="")


if __name__ == "__main__":
    main()

