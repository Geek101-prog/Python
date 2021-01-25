my_set = [1, 1.2, 'How i met your mother', (5 + 6j), True, None]
for x, i in enumerate(my_set, 1):
    print(x, type(i))
print('*' * 33)
for i, item in enumerate(my_set, 1):
    print(f'{i} {item} - {type(item)}')
