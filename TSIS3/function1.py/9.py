import math

def volume(radius):
    if radius < 0:
        print("Incorrect value")
    else:
        result = (4 * math.pi * radius**3)/3
        print(f"{result:.2f}")
    

radius = float(input())
volume(radius)