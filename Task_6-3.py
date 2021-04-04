"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""

from memory_profiler import profile, memory_usage


def check_mem(func):
    def wrapper(*args, **kwargs):
        start = memory_usage()
        result = func(*args)
        end = memory_usage()
        diff = end[0] - start[0]
        return result, diff
    return wrapper


@profile
def wrapper(num):
    def recursive_reverse(num):
        print(num)
        if num == 0:
            return ''
        return f'{str(num % 10)}{recursive_reverse(num // 10)}'
    return recursive_reverse


@check_mem
def recursive_reverse(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


# При профилировки функций с рекурсией возникает проблема с множественным вызовом профилировщика.
# Решается эта проблема либо созданием собственного декоратора, либо оборачиванием функции в еще одну функцию.
num_10000 = 16250615961502295651225
wrapper(num_10000)
res, d = recursive_reverse(num_10000)
print(f"{d} MiB")

