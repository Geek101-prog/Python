from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, x):
        self.x = x

    @abstractmethod
    def calculation(self):
        pass


class Coat(Clothes):
    @property
    def calculation(self):
        return round(self.x / 6.5 + 0.5)


class Suit(Clothes):
    @property
    def calculation(self):
        return round(2 * self.x + 0.3)


coat = Coat(10)
suit = Suit(12)
print(coat.calculation)
print(suit.calculation)
