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

    min_ind = 0
    for i in range(1, len(arr)):
        # print(i)
        # print(arr[i])
        if arr[i] < arr[min_ind]:
            min_ind = i
    return min_ind
    print(min_ind)


print(min_search([1, 30, 55]))
