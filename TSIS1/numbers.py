import random

x = 1    # int
y = 2.8  # float
p = 1j   # complex 
z = 12

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(z) 

#You cannot convert complex numbers into another number type.

print(a) 
print(type(a))

print(b)
print(type(b))

print(c)
print(type(c))

#random
print(random.randrange(1,99), "- random number")






