import time
from itertools import cycle


class TrafficLight:
    def __init__(self):
        self.__color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        for color in cycle(self.__color):
            print(color)
            if color == 'Красный':
                time.sleep(7)
            elif color == 'Желтый':
                time.sleep(2)
            else:
                time.sleep(5)


try2 = TrafficLight()
try2.running()
