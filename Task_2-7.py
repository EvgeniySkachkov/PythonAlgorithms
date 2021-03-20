# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

class notNaturalDigitException(Exception):
    pass


def summ(n):
    if n == 1:
        return n
    return summ(n-1) + n


try:
    n = input('Введите любое натуральное число: ')
    if not n.isdigit():
        raise notNaturalDigitException
    n = int(n)
    if summ(n) == int(n * (n + 1) / 2):
        print(f'Равенство подтверждено: {summ(n)} = {int(n * (n + 1) / 2)}')
    else:
        print('Равенство не подтверждено')
except notNaturalDigitException:
    print('Введено неверное значение. Введите науральное число.')
