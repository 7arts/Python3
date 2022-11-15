from abc import ABC, abstractmethod


class Cloth(ABC):

    @abstractmethod
    def calc_cloth(self):
        pass


class Coat(Cloth):

    def __init__(self, size):
        self.__size = size

    def calc_cloth(self):
        return float(self.__size / 6.5 + 0.5)


class Costume(Cloth):

    def __init__(self, height):
        self.__height = height

    def calc_cloth(self):
        return float(2 * self.__height + 0.3)


cloth_1 = Coat(55)
cloth_2 = Costume(120)
print(cloth_1.calc_cloth())
print(cloth_2.calc_cloth())
