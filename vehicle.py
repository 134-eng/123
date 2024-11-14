class vehicle:
    def __init__(self, speed):
        self.speed = speed

    def moving(self):
        print(f"транспорт переміщається зі швидкістю {self.speed} км/год.")


class car(vehicle):
    def __init__(self, speed, brand):
        super().__init__(speed)
        self.brand = brand

    def moving(self):

        print(f"{self.brand} автомобіль переміщається зі швидкістю {self.speed} км/год.")

class bicycle(vehicle):
    def __init__(self, speed, type):
        super().__init__(speed)
        self.type = type

    def moving(self):
        print(f"{self.type} велосипед переміщається зі швидкістю {self.speed} км/год.")

class plane(vehicle):
    def __init__(self, speed, brand):
        super().__init__(speed)
        self.brand = brand

    def moving(self):
        print(f"{self.brand} літак переміщається зі швидкістю {self.speed} км/год.")

car = car(90, "audi")
bicycle = bicycle(15, "горний")
plane = plane(850, "boeing 747")

car.moving()
bicycle.moving()
plane.moving()
