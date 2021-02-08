class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        return full_name

    def get_total_income(self):
        total_income = sum(self._income.values())
        return total_income


person = Position('Вася', 'Пупкин', 'Сын', 250000, 30000)
print(person.get_full_name())
print(person.get_total_income())
