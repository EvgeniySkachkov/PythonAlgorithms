"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через cProfile и через timeit
Сделайте вывод, какая из трех реализаций эффективнее и почему!!!
И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""
from timeit import timeit
from cProfile import run
from random import randint


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

num = randint(0,10000000)

print(f"Первая функция - {timeit('revers_1(num)', setup='from __main__ import revers_1, num', number=100000)}")
print(f"Вторая функция - {timeit('revers_2(num)', setup='from __main__ import revers_2, num', number=100000)}")
print(f"Третья функция - {timeit('revers_3(num)', setup='from __main__ import revers_3, num', number=100000)}")


print(f"Первая функция {revers_1(num)}")
run('revers_1(num)')
print(f"Вторая функция {revers_2(num)}")
run('revers_2(num)')
print(f"Третья функция {revers_3(num)}")
run('revers_3(num)')

# Третья функция является наилучшей, так как имеет наименьшее время выполнения и наименьшую сложность O(n).
# Также читаемость алгоритма выше, чем у остальных.