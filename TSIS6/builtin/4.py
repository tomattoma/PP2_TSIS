#Write a Python program that invoke square root function after specific milliseconds.
import math
import time

def root(number):
    return math.sqrt(number)

number = int(input())
milliseconds = int(input())
result = root(number)

time.sleep(milliseconds/1000) #работет только для минут поэтому конвертируем в секунду

print(f"Square root of {number} after {milliseconds} miliseconds is {result}")