thislist = ["apple", "banana", "cherry"]
print(len(thislist)) 
print(type(thislist))

i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

listik = ["one", "two", "three", "four"]
del listik[1] # the del keyword can also delete the list completely.
print(listik)

