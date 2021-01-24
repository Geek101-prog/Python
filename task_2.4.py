user_str = input('Enter any words')
user_str = user_str.split()
for x, i in enumerate(user_str, 1):
    if len(i) > 10:
        i = i[0:10]
    print(x, i)
