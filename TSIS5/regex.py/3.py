import re


text =input()

pattern =r"\b\w+-\w+\b" 

result = re.findall(pattern, text)

for res in result:
   print(res)
