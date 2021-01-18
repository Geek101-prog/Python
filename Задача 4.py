# Задача 4
number = int(input('Введите целое положительное число'))
a = number % 10

while number >= 1:
    number = number // 10
    if number % 10 > a:
        a = number % 10
    if number > 9:
        continue
    else:
        print("Максимальное цифра в числе ", a)
        break
