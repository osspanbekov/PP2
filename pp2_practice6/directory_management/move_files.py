import os
import shutil


def main() -> None:
    """
    Демонстрация:
    - создание директорий через os.makedirs()
    - копирование и перемещение через shutil.copy2 / shutil.move
    - cleanup, чтобы не оставлять мусор
    """

    base_dir = os.path.dirname(__file__)
    src_dir = os.path.join(base_dir, "move_src")
    dst_dir = os.path.join(base_dir, "move_dst")

    # Пересоздадим директории аккуратно.
    for d in (src_dir, dst_dir):
        if os.path.exists(d):
            for root, _, files in os.walk(d, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
            for root, dirs, _ in os.walk(d, topdown=False):
                for dd in dirs:
                    try:
                        os.rmdir(os.path.join(root, dd))
                    except OSError:
                        pass
            try:
                os.rmdir(d)
            except OSError:
                pass

    os.makedirs(src_dir, exist_ok=True)
    os.makedirs(dst_dir, exist_ok=True)

    src_copy = os.path.join(src_dir, "to_copy.txt")
    src_move = os.path.join(src_dir, "to_move.txt")
    with open(src_copy, "w", encoding="utf-8") as f:
        f.write("This file will be copied.\n")
    with open(src_move, "w", encoding="utf-8") as f:
        f.write("This file will be moved.\n")

    copied_path = os.path.join(dst_dir, os.path.basename(src_copy))
    moved_path = os.path.join(dst_dir, os.path.basename(src_move))

    shutil.copy2(src_copy, copied_path)
    shutil.move(src_move, moved_path)

    print(f"Copied: {src_copy} -> {copied_path}")
    print(f"Moved: {src_move} -> {moved_path}")

    # cleanup
    for root, _, files in os.walk(src_dir, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
    for root, _, files in os.walk(dst_dir, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))

    try:
        os.rmdir(src_dir)
    except OSError:
        pass
    try:
        os.rmdir(dst_dir)
    except OSError:
        pass


if __name__ == "__main__":
    main()

