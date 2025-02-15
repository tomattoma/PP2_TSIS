def func(n):
    for i in range (0,n+1):
        if i%3 == 0 and i%4 == 0:
            yield str(i) 
    
N = int(input())
rev = ', '.join(func(N))
print(rev)