"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from timeit import repeat
from collections import OrderedDict


def dict_add_item(n):
    dct = {}
    for i in range(0, n):
        dct[f'{i}'] = i
    return dct


def odict_add_item(n):
    ordered_dct = OrderedDict({f'{i}': i for i in range(0, n)})
    return ordered_dct


def dct_pop_last_item(dct):
    for i in range(0, len(dct)):
        dct.pop(f'{i}')


def odct_pop_last_item(odct):
    for i in range(0, len(odct)):
        odct.popitem(False)


n = 1000
dct = dict_add_item(n)
odct = odict_add_item(n)
print(f"Словарь - {min(repeat('dict_add_item(n)', setup='from __main__ import dict_add_item, n', repeat=3, number=1000))}")
print(f"Сортированный словарь - {min(repeat('odict_add_item(n)', setup='from __main__ import odict_add_item, n', repeat=3, number=1000))}")

print(f"Словарь - {min(repeat('dct_pop_last_item(dct)', setup='from __main__ import dct_pop_last_item, dct', repeat=3, number=1000000))}")
print(f"Сортированный словарь - {min(repeat('odct_pop_last_item(odct)', setup='from __main__ import odct_pop_last_item, odct', repeat=3, number=1000000))}")

# При создании обычный словарь немного выигрывает по времени.
# Но при извлечении элементов разница по времени не заметна.
# Даже сейчас упорядоченные словари актуальны, когда необходимо задать определённый порядок пар ключ/значение











