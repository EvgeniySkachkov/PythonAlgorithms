# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


def digitCounter(number, even, odd):
    if number / 10 == 0:
        print(f'Чётных чисел - {even}. Нечётных - {odd}')
        return number % 10

    if (number % 10) % 2 == 0:
        even += 1
    else:
        odd +=1
    return digitCounter(number // 10, even, odd)


number = 34560
even = 0  # Чётные числа
odd = 0  # Нечётные числа
digitCounter(number, even, odd)
