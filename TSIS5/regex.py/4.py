import re 

text =input()

pattern =r"[A-Z][a-z]+" 

result = re.findall(pattern, text)

for res in result:
   print(res)