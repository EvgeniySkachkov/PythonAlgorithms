"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
Обязательно доработайте алгоритм (сделайте его умнее)!
Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение.
Обязательно сделайте замеры времени обеих реализаций и обосновать дала ли оптимизация эффективность
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере, а по убыванию.
Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

from random import randint
from memory_profiler import memory_usage
from timeit import default_timer


def check_mem_time(func):
    def wrapper(*args, **kwargs):
        start = [default_timer(), memory_usage()]
        result = func(*args)
        end = [default_timer(), memory_usage()]
        return f"{result}Время выполнения = {end[0] - start[0]} | Израсходовано памяти = {end[1][0] - start[1][0]:0.10f} MiB\n\n"
    return wrapper


@check_mem_time
def bubble_sort(lst):
    i = 1
    while i < len(lst):
        j = 0
        while j < (len(lst) - i):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
            j += 1
        i += 1
    return f"Неоптимизированная функция | Результат выполнения {lst}\nДлинна списка {len(lst)} | Шаг окончания {i}\n"


@check_mem_time
def bubble_sort_optimized(lst):
    i = 1
    flag = True
    while i < len(lst) and flag:
        flag = False
        j = 0
        while j < (len(lst) - i):
            if lst[j] < lst[j+1]:
                flag = True
                lst[j], lst[j+1] = lst[j+1], lst[j]
            j += 1
        i += 1
    return f"Оптимизированная функция | Результат выполнения {lst}\nДлинна списка {len(lst)} | Шаг окончания {i}\n"


n = 10
prime_lst = [randint(-100, 99) for _ in range(0, n)]
print(f"Исходный список {prime_lst}")
print(bubble_sort(prime_lst[:]))

n = 10
prime_lst = [randint(-100, 99) for _ in range(0, n)]
print(f"Исходный список {prime_lst}")
print(bubble_sort_optimized(prime_lst[:]))

n = 100
prime_lst = [randint(-100, 99) for _ in range(0, n)]
print(f"Исходный список {prime_lst}")
print(bubble_sort(prime_lst[:]))

n = 100
prime_lst = [randint(-100, 99) for _ in range(0, n)]
print(f"Исходный список {prime_lst}")
print(bubble_sort_optimized(prime_lst[:]))

n = 1000
prime_lst = [randint(-100, 99) for _ in range(0, n)]
print(f"Исходный список {prime_lst}")
print(bubble_sort(prime_lst[:]))

n = 1000
prime_lst = [randint(-100, 99) for _ in range(0, n)]
print(f"Исходный список {prime_lst}")
print(bubble_sort_optimized(prime_lst[:]))

# На основании результатов полученных в процессе тестирования, можно сделать вывод о том,
# что оптимизация действительно сокращает количество иттераций, но возрастает общее время выполненения функции.
# Из этого можно сделать вывод, о том что оптимизация здесь лишняя.
