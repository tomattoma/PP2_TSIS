#Write a Python program with builtin function that checks whether a passed string is palindrome or not.
import re

def palindrome(text):
    text = re.sub(r"[^a-zA-Z0-9]", "" , text.lower())
    return text == text[::-1]

text = input()
if palindrome(text):
    print("Yes")
else:
    print("No")
