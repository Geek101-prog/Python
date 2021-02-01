# Взаимодействие с модулями
# The fist method. Использование через точку
# import math
#
# print(math.pi)
# print(math.sin(5))
# print(math.sqrt(4))
# print('*' * 33)
# The second method. Подключение определенный элементов. Вызов без точки
# from math import pi, sin, sqrt
#
# print(pi)
# print(sin(56))
# print(sqrt(10))
# print('*' * 33)
# The third method. from math import * Подключение всей бибилиотеки
# Не переопределять математические переменные. Например pi = 3.2
# При подключении бибилиотеки, работа происходит с её дубликатом
# Лучше всего для каждой библиотеки использовать своё подключение.

# Создание собственного модуля.
# import My_first_lib as  My
#
# print(My.sh_m())
# print(My.simple())

# Создание скрипта с параметрами argv список с первым элементом пути
# Получение данных не через input, а через командную строку Run-Edit-Parametrs
# from sys import argv
# name, s_1, s_2, s_3 = argv
# print(argv)
# print(s_1)
# print(s_2)
# print(s_3)
# Второй способ через терминал

# Генераторы списков, словарей и множеств
# Создание на основе базы и добавление фильтров. Тип генератора определяется скобками
my_list = [1, 2, 3, 4, 5, 6, 7]
# Увелечение каждого четного элемента на + 10, иначе возводим в степень
new_ = [num + 10 if num % 2 == 0 else num ** 3 for num in my_list]
print(new_)
print('*' * 33)
#  Тернарные операторы поддерживают вложенность
# new_1 = [num + 10 if num % 2 == 0 else num ** 3 for num in my_list for t in]
# Без базы
new_1 = {num ** 3 for num in range(1, 11)}
print(new_1)
new_2 = {num: num ** 3 for num in range(1, 11)}
print(new_2)
print('*' * 33)
# Модуль random для генерации псевдослучайных чисел
from random import randint, randrange, random

print(randint(1, 10))
print(randrange(3))
print(randrange(3, 21, 3))
print(random())
print(random() * 10)
print(random() * 100)
print('*' * 33)


# yield слово как return только возвращает генератор
def my_gen():
    for i in [1, 2, 3, 4]:
        yield i


print(my_gen())
for k in my_gen():
    print(k)

print('*' * 33)
# Модули functools, itertools
# reduce как map. работает с функциями принимающие не более двух аргументов
from functools import reduce


def my_func(prev_el, el):
    # prev_el предыдущий элемент
    # el текущий элемент
    return prev_el + el


print(reduce(my_func, [1, 2, 3, 4, 5]))
# ответ 15 - результат суммирования

# intertools содержит бесконечные циклы
from itertools import count

# for el in count(7.1, 2.08) работает с дробями + можно добавить шаг, но только с числами
for el in count(7):
    if el > 15:
        break
    else:
        print(el)

print('*' * 33)
#  cycle работает также с значениями
from itertools import cycle
c = 0
for el in cycle(["ABC", False, 1]):
    if c > 10:
        break
    print(el)
    c += 1

# Модуль math