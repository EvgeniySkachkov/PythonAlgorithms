# В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, то вывести загаданное число.
from random import randint


def guessNumber(num, try_count):
    user_num = input(f'Угадайте число от 0 до 100. У вас осталось {try_count} попыток: ')
    while not user_num.isdigit():
        user_num = input('Вы ввели неверное значение. Введите число: ')
    user_num = int(user_num)

    if try_count == 1:
        print(f'Ваши попытки закончились. Вы проиграли. Загаданное число - {num}')
        return
    if try_count > 1 and user_num == num:
        print(f'Вы угадали, это число {num}')
        return
    elif try_count > 1 and user_num > num:
        print('Ваше число больше загаданного. Попробуйте ещё раз.')
        return guessNumber(num, try_count - 1)
    elif try_count > 1 and user_num < num:
        print('Ваше число меньше загаданного. Попробуйте ещё раз.')
        return guessNumber(num, try_count - 1)


number = randint(0, 100)
guessNumber(number, 10)
