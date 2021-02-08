class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        mass = self._length * self._width * 25 * 5 / 1000
        return mass


road = Road(20, 5000)
print(road.mass())
