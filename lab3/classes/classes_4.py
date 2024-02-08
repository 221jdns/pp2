import math
class Point:
    def __init__(self,x,y):
        x.self = x
        y.self = y
    def show(self):
        print(x.self,y.self)
    def move(self,mx,my):
        self.x +=mx
        self.y +=my
    def dist(self, somepoint):
        distance = math.sqrt((self.x - somepoint.x)**2 +(self.y - somepoint.y)**2)
        return distance