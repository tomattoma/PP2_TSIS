#Write a Python program with builtin function to multiply all the numbers in a list
import math 
def multiply_all_numbers(somelist):
    return math.prod(somelist)

mylist = (list(map(int, input().split())))
print(multiply_all_numbers(mylist))