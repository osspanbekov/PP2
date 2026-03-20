import os
import time
import shutil


def main() -> None:
    """
    Демонстрация:
    - копирование и back-up через `shutil.copy2` (backup НЕ в папке, а отдельным именем файла)
    - безопасное удаление исходника после успешного копирования
    """

    base_dir = os.path.dirname(__file__)
    src_path = os.path.join(base_dir, "sample.txt")
    keep_backup = False  # чтобы не оставлять мусор в репозитории после демонстрации

    if not os.path.exists(src_path):
        print(f"Source file not found: {src_path}")
        print("Run `python pp2_practice6/file_handling/write_files.py` first.")
        return

    backup_name = f"sample_backup_{int(time.time())}.txt"
    backup_path = os.path.join(base_dir, backup_name)

    shutil.copy2(src_path, backup_path)

    if not os.path.exists(backup_path):
        print("Backup copy failed (backup file not found).")
        return

    # Delete safely: только после того, как backup точно появился.
    os.remove(src_path)

    print(f"Backup created: {backup_path}")
    print(f"Deleted original: {src_path}")

    if not keep_backup:
        os.remove(backup_path)
        print(f"Removed backup (cleanup): {backup_path}")


if __name__ == "__main__":
    main()

