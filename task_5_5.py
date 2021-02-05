with open('file_t5.txt', 'w', encoding='utf-8') as x:
    numbers = input('Enter the numbers with space')
    numbers = map(int, numbers.split())
    sum1 = sum(numbers)
    x.write(str(sum1))
    print(sum1)
