from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param stairway: список целых чисел, где каждое целое число является стоимостью конкретной ступени
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    ...  # TODO реализовать прямой метод расчета

    """for i in range(2, count_stairs + 1):  # начиная с 2 до n включительно
        count_paths[i] = count_paths[i-1] + count_paths[i-2]

    return count_paths"""

    count_stairs = len(stairway)
    if count_stairs == 1:
        return stairway[0]
    if count_stairs == 2:
        return stairway[1]

    coast = [0] * count_stairs
    coast[0] = stairway[0]
    coast[1] = stairway[1]

    for current_step in range(2, len(stairway)):
        coast[current_step] = stairway[current_step] + min(coast[current_step - 1], coast[current_step - 2])

    return coast[-1]

if __name__ == '__main__':
    print(stairway_path([1, 3, 1, 5]))  # 7
