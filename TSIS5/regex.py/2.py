import re


text =input()
pattern = r"ab{1,3}"

result = re.findall(pattern, text)
print(result)