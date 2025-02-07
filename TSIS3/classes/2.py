class Shape:
    def _init_(self):
        pass
    
    def area(self):
        return 0
    
class Square(Shape):

    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

S = Square(6)
print(S.area())



        

        