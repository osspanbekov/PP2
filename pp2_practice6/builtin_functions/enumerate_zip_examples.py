def to_int(value):
    """
    type checking and conversions:
    - если значение уже int -> возвращаем
    - если str -> пытаемся преобразовать в int
    - иначе -> None
    """

    if isinstance(value, int):
        return value

    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            return None

    return None


def main() -> None:
    """
    - enumerate(): парная итерация с индексом
    - zip(): идём по двум спискам параллельно
    - type checking & conversion: to_int(...)
    """

    names = ["alice", "bob", "carol"]
    scores = [100, 95, 88]

    print("--- enumerate(names) ---")
    for idx, name in enumerate(names, start=1):
        print(f"{idx}. {name}")

    print("--- zip(names, scores) ---")
    for name, score in zip(names, scores):
        print(f"{name}: {score}")

    values = ["10", "20", "oops", 30]
    converted = [to_int(v) for v in values]

    print("--- type checking & conversions ---")
    print(f"values: {values}")
    print(f"converted (None means can't convert): {converted}")


if __name__ == "__main__":
    main()

