import math

def deg_rad(degree):
    return math.radians(degree)

mydeg = int(input("Input degree: "))
print(f"Output radian: {deg_rad(mydeg):.6f}")
