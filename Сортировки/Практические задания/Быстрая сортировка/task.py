from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Алгоритм быстрой сортировки.

    1. Выбираем опорный элемент. Например, первый элемент.
    2. В левую часть отправляем всё что меньше опорного элемента, в правую всё что больше.
    3. К левой и правой части рекурсивно применяет алгоритм быстрой сортировки.

    :param container: последовательность, которую надо отсортировать
    :return: Отсортированная в порядке возрастания последовательность
    """
    ...  # TODO реализовать алгоритм быстрой сортировки

# pivot - опорный элемент

    if not container:
        return container

    pivot = container[0]
    return (
            sort([item for item in container if item < pivot]) +
            [item for item in container if item == pivot] +
            sort([item for item in container if item > pivot])
    )



print(sort([2,4,7,1,2,3,4,5]))