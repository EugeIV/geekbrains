from abc import ABC, abstractmethod


class Clothes(ABC):
    total_cloth = 0

    @abstractmethod
    def amount_of_cloth(self):
        pass


class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    @property
    def amount_of_cloth(self):
        cloth = self.size / 6.5 + 0.5
        Clothes.total_cloth += round(cloth, 2)
        return round(cloth, 2)


class Suit(Clothes):

    def __init__(self, height):
        self.height = height

    @property
    def amount_of_cloth(self):
        cloth = 2 * self.height + 0.3
        Clothes.total_cloth += round(cloth, 2)
        return round(cloth, 2)


a = Coat(175)
print(a.amount_of_cloth)
b = Suit(56)
print(b.amount_of_cloth)
print(Clothes.total_cloth)
