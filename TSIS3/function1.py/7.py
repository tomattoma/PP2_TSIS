def has_33(thislist):
    for i in range(len(thislist)-1):
        if thislist[i] == 3 and thislist[i+1]==3:
            return True
    return False

mylist = list(map(int, input().split()))
print(has_33(mylist))
