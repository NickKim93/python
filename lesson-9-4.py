class Car:

    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print(f'Машина поехала {self.name} со скоростью {self.speed}')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print('Машина остановилась')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость превышена, текущая скорость: {self.speed}')
        else:
            print(f'Tекущая скорость: {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость превышена, текущая скорость: {self.speed}')
        else:
            print(f'Tекущая скорость: {self.speed}')


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, name, speed, color, is_police=True ):
        super().__init__(name, speed, color, is_police)


police_car = PoliceCar('Ford', 70, 'White')
police_car.go()
car_2 = TownCar('Toyota', 70, 'Yellow', is_police=False)
car_2.show_speed()
