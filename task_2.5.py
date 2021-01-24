number = int(input("Enter number: "))
my_list = [7, 5, 3, 3, 2]
x = my_list.count(number)
for i in my_list:
    if x > 0:
        y = my_list.index(number)
        my_list.insert(y + x, str(number))
        break
    else:
        if number > i:
            z = my_list.index(i)
            my_list.insert(z, str(number))
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)
