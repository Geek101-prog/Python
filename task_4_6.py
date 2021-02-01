# Задача 6.1
from itertools import count
from itertools import cycle

for i in count(int(input('Enter number: '))):
    if i < 15:
        print(i)

# Задача 6.2
my_list = [1, 2]
x = 0
for i in cycle(my_list):
    if x < 10:
        print(i)
        x += 1
