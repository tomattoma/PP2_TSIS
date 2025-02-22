#Write a Python program to convert a given camel case string to snake case.
import re

def snake_case(text):
    text = re.sub(r"([a-z])([A-Z])", r"\1_\2", text)
    cvt = "".join(word.lower() for word in text)
    return cvt
    
    

text = "helloWorld"

result = snake_case(text)
print(result)