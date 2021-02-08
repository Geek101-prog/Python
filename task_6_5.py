class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationary):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pencil(Stationary):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Handle(Stationary):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')


stat = Stationary('WEW')
stat.draw()
pen = Pen('Parker')
pen.draw()
pencil = Pencil('Lulu')
pencil.draw()
handle = Handle('Iron')
handle.draw()
