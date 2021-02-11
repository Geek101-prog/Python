class Cell:
    def __init__(self, amount):
        self.amount = amount

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.amount // rows)]) + '\n' + '*' * (self.amount % rows)

    def __str__(self):
        return str(self.amount)

    def __add__(self, other):
        return str(self.amount + other.amount)

    def __sub__(self, other):
        return self.amount - other.amount if (self.amount - other.amount) > 0 else 'Результат отрицательный'

    def __mul__(self, other):
        return str(self.amount * other.amount)

    def __truediv__(self, other):
        return self.amount / other.amount


cell1 = Cell(10)
cell2 = Cell(20)
print(cell1 + cell2)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell1.make_order(5))
print(cell1 - cell2)
print(cell1.amount - 11)
