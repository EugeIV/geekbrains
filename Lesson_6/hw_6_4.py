class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} поехала"

    def stop(self):
        return f"{self.name} остановилась"

    def turn(self, direction):
        return f"{self.name} повернула {direction}"

    def show_speed(self):
        return f"Скорость {self.name} = {self.speed}"


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return "Вы превысили скорость"
        else:
            return f"Скорость {self.name} = {self.speed}"


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return "Вы превысили скорость"
        else:
            return f"Скорость {self.name} = {self.speed}"


class PoliceCar(Car):
    pass


mazda = TownCar(speed=90, color="красная", name="Mazda6")
print(mazda.show_speed())
print(mazda.color)
print(mazda.go())
print(mazda.stop())
print(mazda.turn(direction="направо"))


ferrari = SportCar(speed=120, color="желтый", name="Ferrari")
print(ferrari.show_speed())

kamaz = WorkCar(speed=40, color="белый", name="Камаз")
print(kamaz.show_speed())
print(kamaz.is_police)

police = PoliceCar(speed=140, color="цветной", name="ДПС", is_police=True)
print(police.is_police)
print(police.speed)
