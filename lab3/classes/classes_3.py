class Rectangle(Shape):
    def __init__(self,width,length):
        self.width = width
        self.length = length
    def ar(self):
        print(self.length*self.width)