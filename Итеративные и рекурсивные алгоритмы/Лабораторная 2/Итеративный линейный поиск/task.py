"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    ...  # TODO реализовать итеративный линейный поиск

    min_ = arr[0]
    for i in range(0, len(arr)):
        # print(i)
        # print(arr[i])
        if arr[i] < min_:
            min_ = i
        if arr[i] > min_:
            min_ = min_
        continue

        return i
    print(i)


print(min_search([11, 30, 7]))
