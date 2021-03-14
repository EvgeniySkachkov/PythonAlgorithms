"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""




# companies = [
#     ['Company_1', 10000],
#     ['Company_2', 2500],
#     ['Company_3', 7580],
#     ['Company_4', 15230], #1
#     ['Company_5', 9600],
#     ['Company_6', 11570], #3
#     ['Company_7', 6800],
#     ['Company_8', 12100], #2
#     ['Company_9', 7400],
#     ['Company_10', 9800],
# ]

companies_dict = {
    'Company_1': 10000,
    'Company_2': 2500,
    'Company_3': 7580,
    'Company_4': 15230, #1
    'Company_5': 9600,
    'Company_6': 11570, #3
    'Company_7': 6800,
    'Company_8': 12100, #2
    'Company_9': 7400,
    'Company_10': 9800,
}
companies_profit = list(companies_dict.values())
companies_name = list(companies_dict.keys())

# Метод №1
# Сложность = O(n)

def method_1(companies_profit, companies_name):
    result_list = [] # O(1)
    max = 0 # O(1)
    max_position = 0 # O(1)
    for j in range(3): # 3*O(1)
        for i, elem in enumerate(companies_profit): # O(n)
            if companies_profit[i] > max: # O(1)
                max = companies_profit[i] # O(1)
                max_position = i # O(1)
        result_list.append([companies_name[max_position], companies_profit[max_position]]) # O(1)
        companies_profit.pop(max_position) # O(1)
        companies_name.pop(max_position) # O(1)
        max = 0 # O(1)
        max_position = 0 # O(1)
    print(f'Первый метод - {result_list}')


# Метод №2
# Сложность - O(n^2)

def method_2(companies_profit):
    i = 0 # O(1)
    print('Второй метод: ')
    while i < len(companies_profit) - 1: # O(n^2)
        max = i # O(1)
        j = i + 1 # O(1)
        while j < len(companies_profit): # O(n)
            if companies_profit[j] > companies_profit[max]: # O(1)
                max = j # O(1)
            j += 1 # O(1)
        companies_profit[i], companies_profit[max] = companies_profit[max], companies_profit[i] # O(1)
        i += 1 # O(1)
    for i in range(0,3): # 3*O(1)
        for key, value in companies_dict.items(): # O(n)
            if companies_profit[i] == value: # O(1)
                print(f'{key} - {companies_profit[i]}')

# Метод №3
# Сложность O(n)


def method_3(companies_profit):
    result_lst = [] # O(1)
    # Ищет максимальное значение из списка прибылей, получает ег индекс, удаляет из исходного списка и добавлает его в новый
    for i in range(0, 3): # O(1)
        result_lst.append(companies_profit.pop(companies_profit.index(max(companies_profit)))) # O(n)
    print(f'Третий метод - {result_lst}')


# Считаю третий метод самым эффективным, так как его сложность не велика, а количество строк в разы меньше остальных.
# Что делает его более лёгким для чтения и простым для понимания и редактирования, в случае необходимости.

method_1(companies_profit, companies_name)
method_2(companies_profit)
method_3(companies_profit)