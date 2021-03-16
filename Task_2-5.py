# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.


def tableASCII(position):
    if position == 127:
        print(f'{position} - {chr(position)}', end=' ')
        return ''

    if position % 10 != 1:
        print(f'{position} - {chr(position)}', end=' | ')
        return tableASCII(position + 1)
    elif position % 10 == 1:
        print(f'{position} - {chr(position)}', end='\n')
        return tableASCII(position + 1)

tableASCII(32)
