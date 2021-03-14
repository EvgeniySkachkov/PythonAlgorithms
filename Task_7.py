"""
Задание 7.
Задание на закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов, например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
и в таких строках (включающих пробелы)
"""



def is_palindrome(prime_str):
    str = prime_str.replace(' ', '')
    flag = True
    for i in range(0, round(len(str) / 2)):
        if str[i] != str[-(i+1)]:
            flag = False
    if flag:
        print(f'{prime_str} - is palindrome')
    else:
        print(f"{prime_str} - isn't palindrome")

test_str = 'молоко делили ледоколом'
test_str_1 = 'топот'
test_str_2 = 'ропот'

is_palindrome(test_str)
is_palindrome(test_str_1)
is_palindrome(test_str_2)