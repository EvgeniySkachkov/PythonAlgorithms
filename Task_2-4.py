# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.
class notNumberException(Exception):
    pass


def sumElements(n, number):
    if n == 1:
        return number
    return sumElements(n-1, (-number / 2)) + number

try:
    n = input('Введите количество элементов: ')
    if not n.isdigit():
        raise notNumberException
    n = int(n)
    print(sumElements(n, 1))
except notNumberException:
    print('Вы веели неверные данные. Необходимо ввести число.')
