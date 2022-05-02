import time


class TrafficLight:

    color = ('green', 'yellow', 'red')

    def running(self):
        print(f'Trafficlight is now {self.color[2]}')
        time.sleep(7)
        print(f'Trafficlight is now {self.color[1]}')
        time.sleep(2)
        print(f'Trafficlight is now {self.color[0]}')
        time.sleep(7)


first_try = TrafficLight()
first_try.running()
