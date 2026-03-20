import os


def main() -> None:
    """
    Демонстрация чтения:
    - `read()` - прочитать всё
    - `readline()` - прочитать первую строку
    - `readlines()` - получить список строк
    """

    base_dir = os.path.dirname(__file__)
    sample_path = os.path.join(base_dir, "sample.txt")

    if not os.path.exists(sample_path):
        print(f"Missing file: {sample_path}")
        print("Run `python pp2_practice6/file_handling/write_files.py` first.")
        return

    print(f"Reading: {sample_path}")

    # read()
    with open(sample_path, "r", encoding="utf-8") as f:
        content = f.read()
    print("--- read() ---")
    print(content, end="")

    # readline()
    with open(sample_path, "r", encoding="utf-8") as f:
        first_line = f.readline()
    print("--- readline() ---")
    print(first_line, end="")

    # readlines()
    with open(sample_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    print("--- readlines() ---")
    print(f"Lines count: {len(lines)}")

    # min/max на длинах строк (встроенные функции из задания)
    stripped_lengths = [len(line.strip()) for line in lines]
    if stripped_lengths:
        print(f"min len(line): {min(stripped_lengths)}")
        print(f"max len(line): {max(stripped_lengths)}")


if __name__ == "__main__":
    main()

