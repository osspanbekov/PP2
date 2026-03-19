from __future__ import annotations

from functools import reduce


def main() -> None:
    """
    Пример:
    - map(): превращаем строки в int
    - filter(): оставляем только чётные
    - reduce(): суммируем результат
    """

    raw = ["1", "2", "3", "4", "5", "6"]

    ints = list(map(int, raw))
    evens = list(filter(lambda x: x % 2 == 0, ints))

    total = reduce(lambda acc, x: acc + x, evens, 0)

    print(f"raw: {raw}")
    print(f"ints: {ints}")
    print(f"evens: {evens}")
    print(f"reduce(sum) total: {total}")


if __name__ == "__main__":
    main()

