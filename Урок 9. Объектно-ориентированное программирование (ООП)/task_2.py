class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self, density, thickness):
        return (self._length * self._width * density * thickness) // 1000


road = Road(20, 5000)
print(road.calc(25, 5))
