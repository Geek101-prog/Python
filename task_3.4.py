def my_function1(x, y):
    z = x ** y
    return print(z.__round__(4))


my_function1(2, -5)


def my_func(x, y):
    if y < 0:
        return 1 / my_func(x, -y)
    elif y == 1:
        return x
    elif y == 0:
        return 1
    return x * my_func(x, y - 1)


print(my_func(2, -5))
