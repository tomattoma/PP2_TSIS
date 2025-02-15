def func(n):
    for i in range (0,n+1):
        if i%2 == 0:
            yield str(i) 
    
N = int(input())
rev = ', '.join(func(N))
print(rev)