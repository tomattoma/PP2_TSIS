import re


text =input()
pattern = r"ab*"

result = re.findall(pattern, text)
print(result)