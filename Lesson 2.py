# x = - 1
# while x <= 10:
#     x += 1
#     if x % 2 == 0:
#         print(x)
#
# a = 1
# while a <= 10:
#     if a % 2 == 0:
#         print(a)
#     a += 1
#
# n = int(input('Numbers'))
# i = 0
# while n > 0:
#     y = n % 10
#     i = i + y
#     n = n // 10
#
# print(i)
#
# v = 643 % 10
# w = 643 // 10
# print(v)
# print(w)
# h = 8000 // 3600
# s = 8000 % 60
# print(h, s)
# print(int(17.5))
# print(int('10001', 2))
# print(bin(17))
# print(oct(17))
# print(hex(17))
# import sys
# sys. float_info ограничение системы для флоат
n = complex(2, 13)
print(n)
# Конкетинация
print('Hi' + 'People')
print('Hi' ' ' 'People!')
print('Hi' + ' ' + 'People!')
# Умножение строк
print('I love Lil' * 5)
print('3' * 3)
print('*' * 33)
# Индексы строки
my_str = 'Python the best of the world'
print(my_str)
# Вызов индекса строки по индексу
print(my_str[12])
print(my_str[-1])
print('*' * 33)
# Срез строки отрезается до крайнего индекса в slice
print(my_str[0:6])
print(my_str[0:5])
print(my_str[:-6])
# Полная копия строки
print(my_str[:])
print('*' * 33)
# Разворот строки
print(my_str[::-1])
print('*' * 33)
# slice это копия не влияющая на состояние строки. Это не метод.
# Подсчет элементов/объектов с любых типов данных len
print(len(my_str))
# Метод split
# Убираем пробелы из списка '1 2  34'.split()
# Объединение строковых элементов списка.Необходимо, чтобы список состоял из
# cтроковых элементов
print(' '.join(['Name',    'Surname']))
# Изменение регистра
print('сЕрГей'.title())
# Верхний и нижний регистр
print('СсСр'.upper())
print('ПРИВЕТ'.lower())
print('*' * 33)
# Подстчет под строк
print('gipopotampo'.count('po'))
print('*' * 33)
# Изменение строки
print('gipopotampo'.replace('po', 'pa'))
print('gipopotampo'.replace('po', ' '))
print('*' * 33)
# Как узнать индекс. Отображает только первый индекс
print('gipopotampo'.index('po'))
print('*' * 33)
# Начать поиск с определенного индекса
print('gipopotampo'.index('po', 3))
print('*' * 33)
# Поиск индекса через find. При отсуствии нужного элемента выдаст -1
print('gipopotampo'.find('po'))
print('gipopotampo'.find('w'))
print('*' * 33)
# Списки. Внутренние элементы можно изменить
print(list('gipopotampo'))
my_list = [23, 3.4, 'str', False, [1, 2]]
# Сложение и умножение списков
print([1, 2] + [3, 4])
print([1, 2] * 4)
print('*' * 33)
# Измерение длинны списка len (счет пойдет с 1, а не с 0)
print(len(my_list))
print('*' * 33)
# Вызов элемента спика по индексу, реверс списка, срез списка
print(my_list[0])
print(my_list[::-1])
print(my_list[0:2])
print('*' * 33)
# Замена элемента списка
my_list[0] = 333
print(my_list)
print('*' * 33)
# Добавление элемента списка
my_list.append(333)
print(my_list)
print('*' * 33)
# Добавление элемента в конкретное место.
my_list.insert(2, 333)
print(my_list)
print('*' * 33)
# Подсчет количества определенно элемента. Если элемент не существует,
# вывод 0
print(my_list.count(333))
print('*' * 33)
# Индекс
my_list.index(333)
# Reverse. Изменяет сам список
my_list.reverse()
print(my_list)
print('*' * 33)
# Вызвать элемент под списка
print(my_list[1][0])
print('*' * 33)
# Удаление последнего элемента списка или определенного элемента по индексу
print(my_list.pop())
print('*' * 33)
# Удаление по значению. Удалит первый элемент, если он повторный.
my_list.remove(333)
print(my_list)
print('*' * 33)
# Множетсво является контейнером с неповторяющимися элементами и распологаются
# в случайном порядке. индекс не подойдет.
my_set= {23, 3.4, 'str', False, (1, 2)}
print(my_set)
# Добавить в множество .add
my_set.add(True)
my_set.add(77)
my_set.add('fdf')
print(my_set)
# Методы удаления
# pop удаляет случайный первый элемент
my_set.pop()
# remove удаление конкретного значения
my_set.remove(77)
# discard удаление конкретного элемента
my_set.discard(23)
print(my_set)
# Подсчет элементов в множестве len
print(len(my_set))
# Математические операции. Вычетание и объединение (одинаковые элементы исчезнут)
print({1, 2, 3} - {1, 2, 8, 9})
print({1, 2, 3} | {1, 2, 8, 9})
print('*' * 33)
# Словарь. индексация не рабоает, значения могу повторятся j и o ключи.
# Список, множество, словарь не могут быть ключом, но могут быть значением.
print(dict(j=67, o=8))
my_dic = {1: 11, 2.3: 22, False: 33, '4': 44, (1, 2): 55}
# К словарю можно обратиться по ключу (false это ноль, try это 1)
# При обращении через get при несуществующем ключе ошибки не будет
print(my_dic[0])
print(my_dic.get(False))
# Замена значения. словарь[ключ] = новое значение. Ключ это доступ к значению
my_dic[1] = 555
# Добавить элементы в словарь. ключ + значение
my_dic[99] = 1111111
# Вызов списка содержающий ключи
print(my_dic.keys())
# Вызов значений
print(my_dic.values())
# Вызов пары
print(my_dic.items())
# Подсчет элементов len
print(len(my_dic))
print('*' * 33)
# Тип данных bool
# Тип данных bytes and bytearray
# bytes для хранения текстокой,графической и звуковой информации
# bytearray массив байт
# Тип данных None пустое состояние (невидимое)
# Тип данных исключение try and except
# Цикл for in для обхода последовательностей
# Список
my_own = [1, 2, 3]
for i in my_own:
    print(i)
print('*' * 33)
# Множество
my_own1 = {1, 2, 3}
for i in my_own1:
    print(i)
print('*' * 33)
# Словарь. В степень будет возведены ключи.
my_own2 = {1: 'a', 2: 'h', 3: 'h'}
for i in my_own2:
    print(i ** 2)
print('*' * 33)
# Если нужны значения указать
# # my_own2.values(). Строки нельзя возвезти в квадрад, только умножить.
my_own3 = {1: 'a', 2: 'h', 3: 'h'}
for i in my_own3.values():
    print(i * 2)
print('*' * 33)
# Кортежи словаря
my_own4 = {1: 'a', 2: 'h', 3: 'h'}
for i in my_own4.items():
    print(i)
print('*' * 33)

my_own4 = {1: 'a', 2: 'h', 3: 'h'}
for k, v in my_own4.items():
    print(k, v)
print('*' * 33)

my_own4 = {1: 'a', 2: 'h', 3: 'h'}
for i in range(len(my_own4)):
    print(i)
print('*' * 33)
# Тернарный оператор (a - b) if a > b else 1 / 0
# Метод содержит ли строка символы похожие на цифры
# .isdigit() не работает с отрицательными числами и дробными числами
# num = input('Enter your number: ')
# print(True if num.isdigit() else False)
# print(True if num.isdecimal() else False)
# print(True if num.isnumeric() else False)
print('*' * 33)
# Оператор is проверяет индентичность двух объектов в памяти
# Возвращает true, если обе переменные ссылаются на один и тот же объект
n = 10
m = 10
print(n is m)
print('*' * 33)
# при сравнении двух списков n = [1, 2] m [1, 2] результат is будет отрицательный
# Оператор in проверяет вхождение элемента в какую структуру
print(7 in [1, 2, 7])
# Если проверять структуру словаря, то проверка будет по ключам.
print(7 in {1: 55, 2: 66, 3: 7})
# Возможна проверка буквы в слове