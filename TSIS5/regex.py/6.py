import re


text = "we say its over,but i keep fucking with you, and every time i do it i wake up with love hangover " 

result = re.sub(r"[., ]", ":", text)

print(result)

