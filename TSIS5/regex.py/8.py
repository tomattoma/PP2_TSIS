import re

text = "HelloWorld"

result = re.split(r"[A-Z]", text)
print(result)