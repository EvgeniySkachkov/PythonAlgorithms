"""
Задание 5.**
Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).
Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (https://younglinux.info/algorithm/sieve)
Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма
Укажите формулу сложности О-нотация каждого алгоритма
и сделайте обоснвование рез-ам
"""

from timeit import timeit


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


def eratosfen(num):
    lst = [el for el in range(1, num * 10)]
    new_lst = [1, 2, 3]
    i = 3
    while len(new_lst) <= num:
        j = 1
        flag = False
        while (j < len(new_lst)) and not flag:
            if lst[i] % new_lst[j] == 0:
                flag = True
            j += 1
        if not flag:
            new_lst.append(lst[i])
        i += 1
    return new_lst[-1]

def eratos(i):
    n = 2
    l = i * 10
    sieve = [el for el in range(l)]
    sieve[1] = 0
    while n < l:
        if sieve[n] != 0:
            m = n * 2
            while m < l:
                sieve[m] = 0
                m += n
        n += 1
    return [p for p in sieve if p != 0][i - 1]


i = int(input('Введите порядковый номер искомого простого числа: '))

print('Simple')
print(simple(i))
print(timeit('simple(i)', setup='from __main__ import simple, i', number=100))

print('Eratosfen')
print(eratosfen(i))
print(timeit('eratosfen(i)', setup='from __main__ import eratosfen, i', number=100))

print('Eratosfen')
print(eratos(i))
print(timeit('eratos(i)', setup='from __main__ import eratos, i', number=100))



