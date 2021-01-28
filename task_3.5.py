def my_sum():
    i = 0
    while True:
        my_list = input('Enter your number. "q" to exit: ').split()
        for number in my_list:
            if number == "q":
                return i
            else:
                try:
                    i += int(number)
                except ValueError:
                    print('"q" for exit')
        print(f'{i}')


print(my_sum())
