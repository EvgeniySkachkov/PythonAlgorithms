"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
Без аналитики задание считается не принятым
"""

from random import randint
from timeit import timeit, repeat
from cProfile import run

array = [1, 3, 1, 3, 4, 5, 1, 9, 9, 9, 9, 9]
array = [randint(0,100) for _ in range(10000)]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, оно появилось в массиве {m} раз(а)'



def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, оно появилось в массиве {max_2} раз(а)'


# При небольшом количестве элементов в массиве функция не многим лучше остальных.
# Но чем больше количество элементов в массиве и чем меньше уникальных значений, тем более эффективна функция.
def my_func():
    d = {array.count(el): el for i, el in enumerate(set(array))}
    num = d.get(max(list(d.keys())))
    max_count = max(list(d.keys()))
    return f'Чаще всего встречается число {num}, оно появилось в массиве {max_count} раз(а)'


print(func_1())
print(func_2())
print(my_func())

print(min(repeat("func_1()", setup="from __main__ import func_1", repeat=3, number=10)))
print(min(repeat("func_2()", setup="from __main__ import func_2", repeat=3, number=10)))
print(min(repeat("my_func()", setup="from __main__ import my_func", repeat=3, number=10)))

run("func_1()")
run("func_2()")
run("my_func()")





