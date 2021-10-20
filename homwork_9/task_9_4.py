class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('car rides')

    def stop(self):
        print('the car stopped')

    def turn(self, direction):
        self.direction = direction
        print(f'the car went {direction}')

    def show_speed(self):
        print(f'your speed {self.speed}')

class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'your speed {self.speed} you are breaking!')
        else:
            print(f'your speed {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'your speed {self.speed} you are breaking!')
        else:
            print(f'your speed {self.speed}')


class PoliceCar(Car):
    pass


sport_car = SportCar(222, 'жёлтая', 'спортивная машина', False)
town_car = TownCar(80, 'синяя', 'городская машина', False)
work_car = WorkCar(60, 'жёлтая', 'рабочая машина', False)
police_car = PoliceCar(200, 'белая', 'милицейская) машина', True)

sport_car.turn('rights')
town_car.show_speed()
police_car.stop()