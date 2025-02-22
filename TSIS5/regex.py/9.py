import re 

def FreeSpace(text):

    return re.sub(r"([a-z])([A-Z])", r"\1 \2", text)
    

text = "MadinaLikesHandsomeBoys"
result = FreeSpace(text)
print(result)

