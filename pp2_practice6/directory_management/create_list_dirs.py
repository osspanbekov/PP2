import os


def main() -> None:
    """
    Демонстрация директории:
    - os.mkdir() / os.makedirs()
    - os.getcwd() / os.chdir()
    - os.listdir()
    - найти файлы по расширению через os.walk
    - os.rmdir() (cleanup пустых папок)
    """

    base_dir = os.path.dirname(__file__)
    nested_root = os.path.join(base_dir, "nested_dirs")

    # Чтобы повторы не ломались.
    # Удалять всё на старте будем осторожно: только если папка существует.
    if os.path.exists(nested_root):
        # Удаляем файлы, затем пробуем удалить папки снизу вверх.
        for root, _, files in os.walk(nested_root, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for d in os.listdir(root):
                full = os.path.join(root, d)
                if os.path.isdir(full):
                    try:
                        os.rmdir(full)
                    except OSError:
                        pass
        try:
            os.rmdir(nested_root)
        except OSError:
            pass

    # Папки: сначала через os.mkdir, потом через os.makedirs (оба варианта показаны).
    if not os.path.exists(nested_root):
        os.mkdir(nested_root)
    level1 = os.path.join(nested_root, "level1")
    os.mkdir(level1)
    os.makedirs(os.path.join(level1, "level2a"), exist_ok=True)
    os.makedirs(os.path.join(level1, "level2b"), exist_ok=True)

    # Файлы для поиска.
    a_txt = os.path.join(level1, "level2a", "a.txt")
    b_py = os.path.join(level1, "level2a", "b.py")
    c_txt = os.path.join(level1, "level2b", "c.txt")
    with open(a_txt, "w", encoding="utf-8") as f:
        f.write("A file with .txt extension\n")
    with open(b_py, "w", encoding="utf-8") as f:
        f.write("# python file\n")
    with open(c_txt, "w", encoding="utf-8") as f:
        f.write("C file with .txt extension\n")

    print(f"Created folders under: {nested_root}")
    print("--- os.getcwd()/os.chdir() ---")
    print(f"Before chdir: {os.getcwd()}")
    os.chdir(nested_root)
    print(f"After chdir: {os.getcwd()}")

    print("--- os.listdir() (first level) ---")
    for name in os.listdir("."):
        print(name)

    # Ищем файлы по расширению.
    print("--- .txt files found (os.walk) ---")
    found = []
    for root, _, files in os.walk("."):
        for name in files:
            if name.endswith(".txt"):
                found.append(os.path.join(root, name))

    for p in sorted(found):
        print(p)

    # Cleanup: удалим созданные файлы и папки, чтобы не мусорить в репозитории.
    for root, _, files in os.walk(nested_root, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for d in os.listdir(root):
            full = os.path.join(root, d)
            if os.path.isdir(full):
                try:
                    os.rmdir(full)
                except OSError:
                    pass
    try:
        os.chdir(base_dir)
    except OSError:
        pass
    try:
        os.rmdir(nested_root)
    except OSError:
        pass


if __name__ == "__main__":
    main()

