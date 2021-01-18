# Задача 2
time = int(input('Enter the time in seconds'))
hour = time // 3600
minute = (time - hour * 3600) // 60
second = time % 60
print('{:02}:{:02}:{:02}'.format(hour, minute, second))
print(f'{hour:02}:{minute:02}:{second:02}')
