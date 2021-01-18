revenue = int(input('Выручка'))
costs = int(input('Издержки'))
if revenue > costs:
    print('Profit')
    profit = revenue - costs
    profitability = profit / revenue
    print(f'Рентабельность комании равна:{profitability}')
    employees = int(input('Введите количество сотрудников'))
    profit_employ = profit // employees
    print(f'Прибыль на 1 сотрудника равна:{profit_employ}')
else:
    print('Loss')
