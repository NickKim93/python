class Road:

    weight = 25
    thickness = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.road_calc()

    def road_calc(self):
        road_volume = (self._length * self._width * self.weight * self.thickness) / 100
        print(f'Required volume of asphalt is: {road_volume} kg')


road_1 = Road(20, 50)
