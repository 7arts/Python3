class Car:

    is_police = False
    def __init__(self, speed, colour, name):
        self.speed = speed
        self.colour = colour
        self.name = name

    def go(self):
        print(f"{self.name} машина поехала")

    def stop(self):
        print(f"{self.name} машина остановилась")

    def turn(self, direction):
        print(f"{self.name} повернула {'налево' if direction == 0 else 'направо'}")

    def show_speed(self):
        return f'{self.name} Её скорость: {self.speed} км/ч'


class TownCar(Car):

    def __init__(self, speed, colour, name):
        super().__init__(speed, colour, name)

    def show_speed(self):
        if self.speed > 60:
            print(f"Превышение скорости на {self.speed - 60} км/ч")
        else:
            print(f'{self.name} Cкорость {self.speed} км/ч')


class SportCar(Car):

    def __init__(self, speed, colour, name):
        super().__init__(speed, colour, name)


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f"Превышение скорости на {self.speed - 40} км/ч")
        else:
            print(f'{self.name} Cкорость {self.speed} км/ч')


class PoliceCar(Car):

    def __init__(self, speed, colour, name):
        super().__init__(speed, colour, name)
        self.is_police = True


town_car = TownCar(70, "Black", "TownCar")
print(town_car.go())
print(town_car.show_speed())
print(town_car.turn(0))
print(town_car.turn(1))
print(town_car.stop())


sport_car = SportCar(40, "Red", "SportCar")
print(sport_car.go())
print(sport_car.show_speed())
print(sport_car.turn(0))
print(sport_car.turn(1))
print(sport_car.stop())
print()

work_car = WorkCar(40, "Green", "WorkCar")
print(work_car.go())
print(work_car.show_speed())
print(work_car.turn(0))
print(work_car.turn(1))
print(work_car.stop())

police_car = PoliceCar(40, "DarkBlue", "PoliceCar")
print(police_car.go())
print(police_car.show_speed())
print(police_car.turn(0))
print(police_car.stop())
