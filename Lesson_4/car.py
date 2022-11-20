class CarNotEnoughFuel(Exception):
    def __init__(self, message):
        super().__init__(message)


class Car:
    fuel = 20
    rate = 0.1
    traveled = 0

    # Конструктор __init__ (передать можно только fuel и rate)
    # Метод __str__

    def drive(self, distance):
        can_travel = self.fuel / self.rate

        if distance > can_travel:
            raise CarNotEnoughFuel(f'Машина сможет проехать только {can_travel} км.')
        else:
            self.traveled += distance
            self.fuel -= distance * self.rate


