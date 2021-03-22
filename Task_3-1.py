"""
Задание 1.
Реализуйте свои пользовательские функции, в которых реализуйте:
a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""

from time import time
from random import randint


def time_count(func):
    def wrapper(n):
        start = time()
        func(n)
        end = time()
        print(f'{end - start}')
        return func(n)
    return wrapper


@time_count
def create_list(lst):
    [lst.append(randint(0, 10)) for _ in range(1000000)]
    return lst


@time_count
def list_operation(lst):
    for i in range(1000000):
       buf = lst[i]


@time_count
def create_dict(dct):
    dct.clear()
    dct = {f'{i}': randint(0,10) for i in range(0, 1000000)}
    return dct


@time_count
def dict_operation(dct):
    for i in range(1000000):
       buf = dct.get(f'{i}')


# Создание списка и словаря из 1000000 элментов.
# Наглядно видно, что список создаётся быстрее, потому что не тратиться время на хэшированние и разрешение коллизий, если таковые случаются.
test_list = []
test_dict = {}

print('Создание списка занимает:')
test_list = create_list(test_list)
print('Создание словаря занимает:')
test_dict = create_dict(test_dict)

# Полный проход по всем элементам списка и словаря
# Судя по показателям видно, что поиск по списку осуществляется быстрее
print('Поиск по списку занимает:')
list_operation(test_list)
print('Поиск по словарю занимает:')
dict_operation(test_dict)
