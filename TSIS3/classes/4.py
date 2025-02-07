import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return (f"coordinates: x:{self.x} and y:{self.y}")
    def move(self, a, b):
        self.x = a
        self.y = b
    def dist(self, x2, y2):
        self.x2 = x2
        self.y2 = y2
        return math.sqrt((self.x2 - self.x)**2 + (self.y2 - self.y)**2)


sasuke = Point(4,5)
print(sasuke.show())
print(sasuke.move(2,3))
print(sasuke.show())
naruto = Point(8,7)
print(naruto.dist(4,5))