x = ["kbtu", "narxoz"]
y = ["kbtu", "narxoz"]
z = x

print(x is z) # returns True because z is the same object as x

print(x is y) # returns False because x is not the same object as y, even if they have the same content

print(x == y) # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y


a = ["mandarin", "banan", "alma"]
print("mandarin" not in a)