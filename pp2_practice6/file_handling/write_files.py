from __future__ import annotations

from pathlib import Path


def main() -> None:
    """
    1) Создаёт текстовый файл.
    2) Записывает sample data.
    3) Добавляет новые строки (append).
    4) Проверяет содержимое повторным чтением.
    """

    base_dir = Path(__file__).resolve().parent
    file_path = base_dir / "data" / "sample.txt"

    # Создаём папку, если её ещё нет.
    file_path.parent.mkdir(parents=True, exist_ok=True)

    initial_lines = [
        "Hello from PP2 practice 6!",
        "This file is created by write_files.py",
        "Line 3: sample data",
    ]
    file_path.write_text("\n".join(initial_lines) + "\n", encoding="utf-8")

    append_lines = [
        "Appended line 1",
        "Appended line 2",
    ]
    with file_path.open("a", encoding="utf-8") as f:
        for line in append_lines:
            f.write(line + "\n")

    # Verify: перечитываем и убеждаемся, что append сработал.
    content = file_path.read_text(encoding="utf-8")
    ok = all(x in content for x in append_lines)

    print(f"File written: {file_path}")
    print(f"Append verification: {'OK' if ok else 'FAILED'}")
    print("--- File content preview ---")
    print(content, end="")


if __name__ == "__main__":
    main()

