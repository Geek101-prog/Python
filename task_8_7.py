class MyComplex:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%s+%sj)' % (self.x, self.y)

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return MyComplex(new_x, new_y)

    def __mul__(self, other):
        new_x = self.x * other.x - self.y * other.y
        new_y = self.y * other.x + self.x * other.y
        return MyComplex(new_x, new_y)


z1 = MyComplex(1, -2)
z2 = MyComplex(3, 4)

print(f"{z1} + {z2} = ", z1 + z2)
print(f"{z1} * {z2} = ", z1 * z2)


class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.a * other.a - (self.b * other.b)} + {(self.a * other.b) + (self.b * other.a)} * i'


z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
x = z_1 + z_2
print(x)
print(z_1 * z_2)
