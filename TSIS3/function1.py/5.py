from itertools import permutations

def perm(self):
    perms = permutations(self)

    res = [''.join(x) for x in perms]
    print(res)

mystring = input()
perm(mystring)