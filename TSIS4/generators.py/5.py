def down(n):
    for x in range (n,-1,-1):
        yield str(x)
    

N = int(input())
rev = ', '.join(down(N))
print(rev)