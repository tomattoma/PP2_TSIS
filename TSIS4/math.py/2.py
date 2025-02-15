import math 

def Area(h, a, b):
    return (a+b)/2*h

height = int(input("Height: ")) 
first_value = int(input("Base, first value: "))
second_value = int(input("Base, second value: "))
print(f"Expected Output: {Area(height, first_value, second_value):.1f}")