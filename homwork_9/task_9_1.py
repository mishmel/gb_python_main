from time import sleep
from itertools import cycle

class TrafficLight:

    def __init__(self):
        self._color = (('red', 7), ('yellow', 2), ('green', 7))

    def running(self):
        for color, sec in cycle(self._color):
            print(color) #'will burn {} sec'.format(sec))
            sleep(sec)

traffic_Light = TrafficLight()
traffic_Light.running()
