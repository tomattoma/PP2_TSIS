import re


text =input()

pattern =r"a.*b\b" 

result = re.findall(pattern, text)

for res in result:
   print(res)
