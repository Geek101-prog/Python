from sys import argv


def salary():
    try:
        name, hours, rate, bonus = argv
        result = int(hours) * int(rate) + int(bonus)
        print(f'Salary {result}')
    except ValueError:
        print('Plz no')


salary()
