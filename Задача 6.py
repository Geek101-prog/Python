a = int(input('Дистанция в первый день пробжки'))
b = int(input('Дистанция на крайний день тренировок'))
i = 1
while b > a:
    a = a + 0.1 * a
    i += 1
print(f'Вы достигли результата через {i}')
