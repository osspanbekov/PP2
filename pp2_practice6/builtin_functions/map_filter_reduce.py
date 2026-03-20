from functools import reduce


def main() -> None:
    """
    Демонстрация built-in функций:
    - map() + типовая конверсия `int(...)`
    - filter() для отбора
    - reduce() (functools) для агрегации
    - len()/sum()/min()/max()/sorted()
    """

    raw = ["1", "2", "3", "4", "5", "6"]

    ints = list(map(int, raw))
    evens = list(filter(lambda x: x % 2 == 0, ints))

    total = reduce(lambda acc, x: acc + x, evens, 0)

    print(f"raw: {raw}")
    print(f"ints: {ints}")
    print(f"evens: {evens}")
    print(f"reduce(sum) total: {total}")

    # Остальные built-in из списка задания
    print(f"len(evens): {len(evens)}")
    print(f"sum(evens): {sum(evens)}")
    print(f"min(evens): {min(evens)}")
    print(f"max(evens): {max(evens)}")
    print(f"sorted(evens): {sorted(evens)}")


if __name__ == "__main__":
    main()

