"""
Задание 2.
Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.
Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!
Если у вас есть идеи, предложите вариант оптимизации, если мемоизация не имеет смысла.
Без аналитики задание считается не принятым
"""

from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)


print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=10000))


def memoize(f):
    cache = {}
    def decorate(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))


# В данном примере мемоизация позволяет ускорить время работы, так как все замеры производятся с использованием одних и тех же данных.
# А результат выполнения сохраняется в памяти, что и позволяет сэкономить время на повторных замерах с теми же данными.
# Но при работе с различными исходными данными мемоизация либо не сработает и лишь замедлит выполнения алгоритма,
# либо повлияет недостаточно эффективно, чтобы воспринимать это как улучшение, с учётом увеличения кода. Что повлияет на его читаемость и поддерживаемость.

def my_func(num):
    return str(num)[::-1]

print('Моя функция my_func')
print(
    timeit(
        'my_func(num_100)',
        setup='from __main__ import my_func, num_100',
        number=10000))
print(
    timeit(
        'my_func(num_1000)',
        setup='from __main__ import my_func, num_1000',
        number=10000))
print(
    timeit(
        'my_func(num_10000)',
        setup='from __main__ import my_func, num_10000',
        number=10000))
