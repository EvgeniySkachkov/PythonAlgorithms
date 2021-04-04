"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235
Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34
Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1
Предприятия, с прибылью ниже среднего значения: Фирма_2
"""

from collections import namedtuple


count_companies = int(input('Введите количество предприятий для расчета прибыли: '))
layout = namedtuple('Companies', 'name company_profit profit_average')
companies_lst = []  # Список для хранения всех компаний
average_companies_profit = 0  # Среднее значение годовых прибылей

for i in range(0, count_companies):
    company_name = input('Введите название предприятия: ')
    profit = input('Через пробел введите прибыль данного предприятия за каждый квартал (Всего 4 квартала): ')
    companies_lst.append(
        layout(
            name=company_name,
            company_profit=list(profit.split()),
            profit_average=sum(map(lambda x: int(x), list(profit.split())))/4
        )
    )
    average_companies_profit += companies_lst[i].profit_average
average_companies_profit /= count_companies

print(f'Средняя годовая прибыль всех предприятий: {average_companies_profit:.3f}')

print('Предприятия, с прибылью выше среднего значения: ', end='')
for i in range(0, count_companies):
    if companies_lst[i].profit_average >= average_companies_profit:
        print(f'{companies_lst[i].name} = {companies_lst[i].profit_average} | ')
print()
print('Предприятия, с прибылью ниже среднего значения: ', end='')
for i in range(0, count_companies):
    if companies_lst[i].profit_average < average_companies_profit:
        print(f'{companies_lst[i].name} = {companies_lst[i].profit_average} | ')
