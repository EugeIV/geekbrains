from time import sleep


class TrafficLight:

    def __init__(self):
        self.color = ["красный", "желтый", "зеленый"]

    def running(self):
        print(self.color[0])
        sleep(7)
        print(self.color[1])
        sleep(3)
        print(self.color[2])
        sleep(5)


sfetofor = TrafficLight()
sfetofor.running()
