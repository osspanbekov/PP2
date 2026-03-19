from __future__ import annotations

import os
from pathlib import Path


def main() -> None:
    """
    Пример:
    1) Создаёт вложенные директории.
    2) Выводит список файлов и папок.
    3) Находит файлы по расширению (*.txt).
    """

    base_dir = Path(__file__).resolve().parent
    root = base_dir / "data" / "nested_dirs"

    # Создаём вложенную структуру
    paths_to_create = [
        root / "level1" / "level2a",
        root / "level1" / "level2b",
    ]
    for p in paths_to_create:
        p.mkdir(parents=True, exist_ok=True)

    # Положим по одному файлу в ветки, чтобы было что искать.
    (root / "level1" / "level2a" / "a.txt").write_text("A file with .txt extension\n", encoding="utf-8")
    (root / "level1" / "level2a" / "b.py").write_text("# python file\n", encoding="utf-8")
    (root / "level1" / "level2b" / "c.txt").write_text("C file with .txt extension\n", encoding="utf-8")

    print(f"Created folders under: {root}")

    # Список файлов/папок на первом уровне.
    print("--- listdir (first level) ---")
    for name in os.listdir(root):
        print(name)

    # Поиск файлов по расширению.
    print("--- .txt files found ---")
    txt_files = [p for p in root.rglob("*.txt") if p.is_file()]
    for p in txt_files:
        print(p.relative_to(base_dir))


if __name__ == "__main__":
    main()

