class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


x = int(input('Enter a number: '))
y = int(input('Enter another number: '))

try:
    if y == 0:
        raise OwnError('Создатель запретил делить на ноль')
    else:
        print(x / y)
except OwnError:
    print('Создатель запретил делить на ноль')

# class OwnError(Exception):
#
#     def division(self, x, y):
#         try:
#             return print(x / y)
#         except ZeroDivisionError:
#             print('Создатель запретил делить на ноль')
#
#
# z = OwnError()
# z.division(10, 0)


# # Решение № 2
#
# class Division1:
#     def div1(self, x, y):
#         if x == 0 or y == 0:
#             print('ZeroDivisionError')
#         else:
#             return print(x / y)
#
#
# z1 = Division1()
# z1.div1(10, 0)
