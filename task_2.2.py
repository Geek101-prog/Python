my_list = []
x = 0
while x <= 5:
    numbers = int(input('Enter six numbers'))
    x += 1
    my_list.append(numbers)
print(my_list)

y = 0
for i in range(int(len(my_list) // 2)):
    my_list[y], my_list[y + 1] = my_list[y + 1], my_list[y]
    y += 2
print(my_list)
