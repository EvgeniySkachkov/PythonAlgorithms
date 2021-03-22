"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""
from hashlib import sha256


def insert_hash_into_cash(url, file_name):
    f = open(file_name, 'r')
    cash = set(el.rstrip('\n') for i, el in enumerate(f.readlines()))
    f.close()

    f = open(file_name, 'a')
    result = f'{url} ' + sha256(url.lower().encode("utf-8") + url.lower().split(".")[0].encode("utf-8")).hexdigest() + '\n'
    if result.rstrip('\n') not in cash:
        f.write(result)
        print('URL успешно добавлен в кэш.')
    else:
        print('Данный URL уже находится в кэше.')
    f.close()


def print_cash(file_name):
    f = open(cash_file_name, 'r')
    c = set(el.rstrip('\n') for i, el in enumerate(f.readlines()))
    if len(c) != 0:
        print(c)
    else:
        print('Кэш пустой.')
    f.close()


def clear_cash(file_name):
    f = open(file_name, 'w')
    f.close()


cash_file_name = 'url_cash.txt'
v = -1
print('1. Добавить URL сайта в кэш.\n2. Вывести содержимое кэша.\n3. Очистить кэш.\n0. Выход.\n')
while v != 0:
    try:
        v = int(input('Введите номер пункта меню: '))
    except ValueError as err:
        print("Вы ввели неверное значение.")

    if v == 1:
        url = input('Введите URL сайта: ')
        insert_hash_into_cash(url, cash_file_name)
    elif v == 2:
        print_cash(cash_file_name)
    elif v == 3:
        clear_cash(cash_file_name)
