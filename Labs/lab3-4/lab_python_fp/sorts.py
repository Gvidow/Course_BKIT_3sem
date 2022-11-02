from platform import java_ver
import re


def sort_with_lambda(lst):
    return sorted(lst, key=lambda x: abs(x), reverse=True)


def sort_not_use_lambda(lst):
    return sorted(lst, key=abs, reverse=True)


if __name__ == "__main__":
    data = [1, -4, 7, -3, 61]
    print(f"Пример результата вызова функции sort_with_lambda{data}")
    print(sort_with_lambda(data))
    print(f"\nПример результата вызова функции sort_not_use_lambda{data}")
    print(sort_not_use_lambda(data))
    print(f"\nИсходный массив {data}")
    print(data)
