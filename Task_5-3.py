"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.
Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям
И добавить аналитику, так ли это или нет.!
"""

from timeit import timeit, repeat
from collections import deque


def lst_add_to_end(n):
    lst = []
    for i in range(0, n):
        lst.append(i)
    return lst


def deque_add_to_end(n):
    deq = deque()
    for i in range(0, n):
        deq.append(i)
    return deq


def lst_add_to_start(n):
    lst = []
    for i in range(0, n):
        lst.insert(0, i)
    return lst


def deque_add_to_start(n):
    deq = deque()
    for i in range(0, n):
        deq.appendleft(i)
    return deq


def lst_get_elems_from_start(lst):
    for i in range(0, len(lst)):
        lst.pop()


def deque_get_elems_from_start(deq):
    for i in range(0, len(deq)):
        deq.pop()



def lst_get_elems_from_end(lst):
    for i in range(0, len(lst)):
        lst.pop(0)


def deque_get_elems_from_end(deq):
    for i in range(0, len(deq)):
        deq.popleft()


print(f"Добавление элементов в начало списка {min(repeat('lst_add_to_start(1000)', setup='from __main__ import lst_add_to_start', repeat=3, number=10000))}")
print(f"Добавление элементов в начало дека {min(repeat('deque_add_to_start(1000)', setup='from __main__ import deque_add_to_start', repeat=3, number=10000))}")
print(f"Добавление элементов в конец списка {min(repeat('lst_add_to_end(1000)', setup='from __main__ import lst_add_to_end', repeat=3, number=10000))}")
print(f"Добавление элементов в конец дека {min(repeat('deque_add_to_end(1000)', setup='from __main__ import deque_add_to_end', repeat=3, number=10000))}")

lst = lst_add_to_start(1000)
deq = deque_add_to_start(1000)
print(f"Извлечение элементов из начала списка {min(repeat('lst_get_elems_from_start(lst)', setup='from __main__ import lst_get_elems_from_start, lst', repeat=3, number=1000000))}")
print(f"Извлечение элементов из начала дека {min(repeat('deque_get_elems_from_start(deq)', setup='from __main__ import deque_get_elems_from_start, deq', repeat=3, number=1000000))}")
lst = lst_add_to_start(1000)
deq = deque_add_to_start(1000)
print(f"Извлечение элементов из конца списка {min(repeat('lst_get_elems_from_end(lst)', setup='from __main__ import lst_get_elems_from_end, lst', repeat=3, number=1000000))}")
print(f"Извлечение элементов из конца дека {min(repeat('deque_get_elems_from_end(deq)', setup='from __main__ import deque_get_elems_from_end, deq', repeat=3, number=1000000))}")

# При добавлении элементов в начало дек заметно выигрывает по времени.
# Но в случае с добавлением в конец время примерно одинаковое.
#
# При извлечении элементов из начала/конца время и у дека, и у очереди одинаковое
