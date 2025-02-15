import math 

def Area(sides, length):
    apothem = ((length)/(2*math.tan(math.pi/sides)))
    return (sides*length*apothem)/2

Sides_number = int(input("Input number of sides: "))
Length_of_a_side = int(input("Input the length of a side: "))
print(f"The area of the polygon is: {Area(Sides_number, Length_of_a_side):.2f}")