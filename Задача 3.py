# Задача 3
number = int(input('Enter the number'))
number_sum1 = str(number) + str(number)
number_sum2 = str(number) + str(number) + str(number)
number_sum3 = number + int(number_sum1) + int(number_sum2)
print(number_sum3)
