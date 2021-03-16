# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.


def ReversFunction(number, new_number):
    if number / 10 == 0:
        print(new_number)
        return number % 10
    return ReversFunction(number // 10, new_number + str(number % 10))


number = 3486
ReversFunction(number, '')
