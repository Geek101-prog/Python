month = int(input('What moth you want? Enter number 1-12: '))
month_set = ['winter', 'spring', 'summer', 'autumn']
if month == 1 or month == 2 or month == 12:
    print(month_set[0])
elif month == 3 or month == 4 or month == 5:
    print(month_set[1])
elif month == 6 or month == 7 or month == 8:
    print(month_set[2])
elif month == 9 or month == 10 or month == 11:
    print(month_set[3])
else:
    print('Господи, Боже мой. В году 12 месяцев')

dict_month = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
if month == 1 or month == 2 or month == 12:
    print(dict_month.get(1))
elif month == 3 or month == 4 or month == 5:
    print(dict_month.get(2))
elif month == 6 or month == 7 or month == 8:
    print(dict_month.get(3))
elif month == 9 or month == 10 or month == 11:
    print(dict_month.get(4))
else:
    print('У вас что клингонский календарь?')
