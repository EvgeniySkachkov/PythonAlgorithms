"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.
Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Пример:
рара - 6 уникальных подстрок
рар
ра
ар
ара
р
а
"""

# hash?

from hashlib import sha256

cash = []
string = input('Введите строку: ').lower()
for i in range(0, len(string)):
    for j in range(i, len(string)):
        if string[i:j+1] != string:
            cash.append(hash(string[i:j+1]))

cash = set(cash)
print(cash)
print(f'Количество уникальных подстрок {len(cash)}')
