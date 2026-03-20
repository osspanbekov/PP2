import os


def main() -> None:
    """
    Демонстрация:
    - file modes: `x`, `w`, `a`
    - context manager: `with open(...) as f`
    - запись sample data + append
    - верификация через `read()`
    """

    base_dir = os.path.dirname(__file__)
    sample_path = os.path.join(base_dir, "sample.txt")

    # Чтобы режим `x` сработал при повторном запуске.
    if os.path.exists(sample_path):
        os.remove(sample_path)

    initial_lines = [
        "Hello from PP2 practice 6!",
        "This file is created by write_files.py",
        "Line 3: sample data",
    ]

    # `x` -> создать новый файл, если его ещё нет.
    with open(sample_path, "x", encoding="utf-8") as f:
        for line in initial_lines:
            f.write(line + "\n")

    # `w` тоже покажем (перезапишем заголовок).
    # В учебных целях: режим `w` отрабатывает как "перезаписать файл".
    with open(sample_path, "w", encoding="utf-8") as f:
        f.write(initial_lines[0] + "\n")
        f.write(initial_lines[1] + "\n")

    # Вернём остальные линии через `append`.
    with open(sample_path, "a", encoding="utf-8") as f:
        f.write(initial_lines[2] + "\n")
        f.write("Appended line 1\n")
        f.write("Appended line 2\n")

    with open(sample_path, "r", encoding="utf-8") as f:
        content = f.read()

    ok = ("Appended line 1" in content) and ("Appended line 2" in content)
    print(f"File written: {sample_path}")
    print(f"Append verification: {'OK' if ok else 'FAILED'}")
    print("--- File content preview ---")
    print(content, end="")


if __name__ == "__main__":
    main()

