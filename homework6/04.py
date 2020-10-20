# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
# свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.


class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля: {self.speed} км/ч')


class SportCar(Car):
    pass


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Превышение скорости!')


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Превышение скорости!')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


sport_car = SportCar(150, 'черный', 'BMW')
sport_car.go()
sport_car.turn('налево')
sport_car.show_speed()
sport_car.stop()
print()

police_car = PoliceCar(80, 'белый', 'Ford')
police_car.go()
police_car.turn('направо')
police_car.show_speed()
police_car.stop()
print()

town_car = TownCar(55, 'красный', 'Honda')
town_car.go()
town_car.turn('налево')
town_car.show_speed()
town_car.stop()
print()

work_car = WorkCar(50, 'синий', 'Renault')
work_car.go()
work_car.turn('направо')
work_car.show_speed()
work_car.stop()
