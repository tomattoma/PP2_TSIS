def solve(numheads, numlegs):
    
    rabbits = (numlegs/2) - numheads
    chickens = 2 * numheads - (numlegs/2)

    print(rabbits, chickens)

numheads = int(input())
numlegs = int(input())

solve(numheads, numlegs)
