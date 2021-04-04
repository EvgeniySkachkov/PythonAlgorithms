"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.
Можно взять задачи с курса Основ
или с текущего курса Алгоритмов
Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)
ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""


from memory_profiler import profile, memory_usage
from timeit import default_timer
from random import randint
import json


def check_mem_time(func):
    def wrapper(*args, **kwargs):
        start = [default_timer(), memory_usage()]
        res = func(*args)
        end = [default_timer(), memory_usage()]
        return f"Затраченное время = {end[0] - start[0]}\n" \
               f"Затраченная память = {end[1][0] - start[1][0]} MiB"
    return wrapper


# Функция сохраняет в массиве индексы четных элементов другого массива
@check_mem_time
@profile
def func_1(nums):  # Функция с выводом итога через список
    return [i for i, el in enumerate(nums) if el % 2 == 0]


@check_mem_time
@profile
def func_2(nums):  # Функция с выводом итога через кортеж
    return (i for i, el in enumerate(nums) if el % 2 == 0)


# Замена списка на кортеж позволила сократить использование памяти в 100 раз и уменьшить время выполнения алгоритма
lst = [randint(0, 10) for _ in range(1000000)]
print(func_1(lst))
print(func_2(lst))


# Функции заполняют словарь и возвращают его
@check_mem_time
def dct(n):
    return {i: i * 2 for i in range(n)}  # Возврат обычного словаря


@check_mem_time
def j_dct(n):
    return json.dumps({i: i * 2 for i in range(n)})  # Возврат словаря с использованием json-формата


# Использование json-формата позволило сохранить большой объём памяти, но страдает время выполнения
n = 1000000
print(dct(n))
print(j_dct(n))


# Функиция получает на вход список и формирует из него новый, возводя каждый элемент в квадрат
@check_mem_time
def f_1(lst):
    new_lst = []
    for i, el in enumerate(lst):
        new_lst.append(el*el)
    return new_lst


@check_mem_time
def f_2(lst):
    new_lst = []
    new_lst = map(lambda x: x*x, lst)
    return new_lst


# Использование встроенной функции map позволило сократить время выполнения и количество затраченной памяти
lst = [randint(1, 9) for i in range(10000000)]
print(f_1(lst))
print(f_2(lst))

