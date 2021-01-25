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

print('*' * 33)

my_list_1 = list(input('Enter your numbers without space -'))
for i in range(1, len(my_list_1), 2):
    my_list[i - 1], my_list_1[i] = my_list_1[i], my_list_1[i - 1]
print(my_list_1)
