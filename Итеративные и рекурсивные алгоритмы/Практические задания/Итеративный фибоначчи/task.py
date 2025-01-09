from functools import lru_cache

count_it = 0
count_rec = 0

def fib_iterative(n: int) -> int:
    """
    Вычислить n-е число последовательности Фибоначчи, используя итеративный алгоритм.

    :param n: Номер числа последовательности Фибоначии. Нумерация чисел с 0
    :return: n-е число последовательности Фибоначчи
    """
    global count_it

    if n < 0:
        raise ValueError()
    if n == 0:
        count_it += 1
        return 0
    if n == 1:
        count_it += 1
        return 1
    prev, cur = 0, 1
    for idx in range(2, n+1):
        count_it += 1
        prev, cur = cur, cur+prev
    return cur







    ...  # TODO написать итеративный алгоритм чисел Фибоначчи
@lru_cache
def rec_fib(n):
    global count_rec
    if n == 0:
        return 0
    if n == 1:
        return 1
    count_rec += 1
    return rec_fib(n-1) + rec_fib(n-2)


print(fib_iterative(5))
print(count_it)
print(rec_fib(5))
print(count_rec)


