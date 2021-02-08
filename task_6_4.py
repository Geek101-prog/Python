import random


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} go')

    def stop(self):
        print(f'{self.name} stop')

    def turn(self):
        turns_dic = {1: 'right', 2: 'left'}
        x = random.choice(list(turns_dic))
        if x == 1:
            print(turns_dic[1])
        elif x == 2:
            print(turns_dic[2])

    def show_speed(self):
        print(f'Current speed : {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Your speed is too high')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Your speed is too high')


class PoliceCar(Car):
    is_police = True


town_car = TownCar(70, 'grey', 'Mersedes')
town_car.go()
town_car.turn()
town_car.show_speed()

print('*' * 33)

sport_car = SportCar(50, 'yellow', 'BMW')
sport_car.go()
sport_car.turn()
sport_car.show_speed()

print('*' * 33)

work_car = WorkCar(80, 'black', 'Audi')
work_car.go()
work_car.turn()
work_car.show_speed()

print('*' * 33)

police_car = PoliceCar(120, 'white', 'Mazda')
police_car.go()
police_car.turn()
police_car.show_speed()
