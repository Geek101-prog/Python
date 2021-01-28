def my_function(x, y, z):
    my_list = [x, y, z]
    my_list.sort(reverse=True)
    result = my_list[0] + my_list[1]
    return result


print(my_function(3, 5, 7))


def my_function1(x, y, z):
    my_list = [x, y, z]
    my_list.remove(min(x, y, z))
    return sum(my_list)


print(my_function1(3, 5, 7))
