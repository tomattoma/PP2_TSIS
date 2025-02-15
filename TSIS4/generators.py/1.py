def generator(start, stop):
    while start <= stop:
        a = start
        start+=1
        print(a**2)

n = int(input())
generator(1,n)

