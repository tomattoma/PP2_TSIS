def squares(y, z):
    for x in range (y,z+1):
        yield str(x**2)
    

a, b = map(int, input().split())
rev = ', '.join(squares(a, b))
print(rev)