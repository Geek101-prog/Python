def my_function(num_1=(int(input('num_1'))), num_2=(int(input('num_2')))):
    try:
        result = num_1 / num_2
        return result
    except ZeroDivisionError:
        return 'Создатель запретил делить на 0'


print(my_function())


def my_function1(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return 'Создатель запретил делить на 0'


print(my_function1(3, 0))
