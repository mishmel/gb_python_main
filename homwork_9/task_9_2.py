class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def required_mass_of_asphalt(self):
        mass = self._length * self._width * 25 * 5 / 1000
        print(mass, 'т')


road = Road(20, 2000)
road.required_mass_of_asphalt()

