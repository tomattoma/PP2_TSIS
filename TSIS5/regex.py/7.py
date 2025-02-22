import re

def camelCase(text):
    def lower_to_upper(match):
        return match.group(1).upper()
    
    text = re.sub(r"_(\w)", lower_to_upper, text.lower())
    
    
    return text


text = "Hello_woRld"
result = camelCase(text)
print(result)