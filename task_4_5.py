from functools import reduce

my_list = [num for num in range(99, 1001) if num % 2 == 0]
multi = reduce(lambda x, y: x * y, my_list)
print(multi)
