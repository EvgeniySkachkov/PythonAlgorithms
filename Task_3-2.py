"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш
Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей
ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
Допускаются любые усложения задания - валидация, подключение к БД, передача данных в файл
"""
# sqlite, postgres, db_api, orm

from hashlib import sha256
import sqlite3 as sq3


def create_table(cur):
    try:
        sqlite_query = 'CREATE TABLE users (' \
                           'name TEXT UNIQUE, ' \
                           'password TEXT)'
        cur.execute(sqlite_query)
    except sq3.Error:
        print('Таблица уже существует.')


def show_table(cur):
    sqlite_query = 'SELECT * FROM users'
    print(cur.execute(sqlite_query).fetchall())


def clear_table(cur):
    sqlite_query = 'DROP TABLE IF EXISTS users'
    cur.execute(sqlite_query)
    sqlite_query = 'CREATE TABLE users (' \
                   'name TEXT UNIQUE, ' \
                   'password TEXT)'
    cur.execute(sqlite_query)


def insert_user(cur):
    dict = {}
    login = input('Введите ваш логин: ')
    password = input('Введите ваш пароль: ')
    result = sha256(login.lower().rstrip(' ').encode('utf-8') + password.strip(' ').encode('utf-8')).hexdigest()
    print(result)
    password = input('Введите ваш пароль ещё раз: ')

    if result == sha256(login.lower().rstrip(' ').encode('utf-8') + password.rstrip(' ').encode('utf-8')).hexdigest():
        print('Верный пароль.')
        dict = {login: password}
    else:
        print('Пароль не верен.')

    try:
        cur.executemany('INSERT INTO users VALUES (?, ?)', dict.items())
    except sq3.Error:
        print('Пользователь с таким логином уже существует.')


try:
    db_name = 'db.sql'
    cur = sq3.connect(db_name).cursor()
    print('Подключение к базе данных выполнено успешно.')

    v = -1
    print('1. Создать таблицу.\n2. Вывести содержимое таблицы.\n3. Очистить таблицу.\n4. Добавить пользователя.\n0. Выход.\n')
    while v != 0:
        try:
            v = int(input('Введите номер пункта меню: '))
        except ValueError as err:
            print("Вы ввели неверное значение.")

        if v == 1:
            create_table(cur)
        elif v == 2:
            show_table(cur)
        elif v == 3:
            clear_table(cur)
        elif v == 4:
            insert_user(cur)

    cur.close()
except sq3.Error:
    print('Ошибка подключения к базе данных.')
