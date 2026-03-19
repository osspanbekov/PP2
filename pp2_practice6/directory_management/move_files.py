from __future__ import annotations

import shutil
from pathlib import Path


def main() -> None:
    """
    Пример:
    1) Копирует файл между директориями (shutil.copy2).
    2) Перемещает другой файл между директориями (shutil.move).
    """

    base_dir = Path(__file__).resolve().parent
    data_dir = base_dir / "data"

    src_dir = data_dir / "move_src"
    dst_dir = data_dir / "move_dst"
    src_dir.mkdir(parents=True, exist_ok=True)
    dst_dir.mkdir(parents=True, exist_ok=True)

    src_copy = src_dir / "to_copy.txt"
    src_move = src_dir / "to_move.txt"
    src_copy.write_text("This file will be copied.\n", encoding="utf-8")
    src_move.write_text("This file will be moved.\n", encoding="utf-8")

    # Copy
    copied_path = dst_dir / src_copy.name
    shutil.copy2(src_copy, copied_path)

    # Move
    moved_path = dst_dir / src_move.name
    shutil.move(src_move, moved_path)

    print(f"Copied: {src_copy} -> {copied_path}")
    print(f"Moved: {src_move} -> {moved_path}")
    print("Done.")


if __name__ == "__main__":
    main()

