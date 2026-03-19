from __future__ import annotations

import time
import shutil
from pathlib import Path


def main() -> None:
    """
    Пример:
    1) Копирует файл в backup (shutil).
    2) Проверяет, что backup появился.
    3) Удаляет исходный файл безопасно.
    """

    base_dir = Path(__file__).resolve().parent
    data_dir = base_dir / "data"
    src = data_dir / "sample.txt"
    backup_dir = data_dir / "backup"
    backup_dir.mkdir(parents=True, exist_ok=True)

    if not src.exists():
        print(f"Source file not found: {src}")
        print("Run write_files.py first.")
        return

    backup_path = backup_dir / f"sample_backup_{int(time.time())}.txt"

    shutil.copy2(src, backup_path)

    if not backup_path.exists():
        print("Backup copy failed (backup file not found).")
        return

    # Delete safely: only delete if backup exists and copy succeeded.
    src.unlink()

    print(f"Copied to backup: {backup_path}")
    print(f"Deleted original: {src}")
    print("Done.")


if __name__ == "__main__":
    main()

