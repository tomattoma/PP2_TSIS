#Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
import math

text = input()
cnt1=cnt2=0
for x in text:
    if x.isupper():
        cnt1+=1
    if x.islower():
        cnt2+=1

print(f"number of upper case letters:{cnt1}")
print(f"number of lower case letters:{cnt2}")