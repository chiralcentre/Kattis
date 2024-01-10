from sys import stdin
from random import randint
from math import sqrt

# precompute all squares from 0^2 to 1000000^2
squared = {pow(i,2) for i in range(1000001)}

# return all tuples (a,b) such that a^2 + b^2 = c
def get_pairs(c):
    ans = []
    for i in range(0,int(sqrt(c)) + 1):
        inmd = pow(i,2)
        if c - inmd in squared:
            rem = int(sqrt(c - inmd))
            ans.append((i,rem))
            ans.append((-i,rem))
            ans.append((-i,-rem))
            ans.append((i,-rem))
    return ans

UPPER = pow(10,6)
n = int(stdin.readline())
for i in range(n):
    x,y = randint(0,UPPER),randint(0,UPPER)
    print(f"{x} {y}", flush = True)
    dist = int(stdin.readline())
    for a,b in get_pairs(dist):
        nx,ny = x + a,y + b
        if 0 <= nx <= UPPER and 0 <= ny <= UPPER:
            print(f"{nx} {ny}", flush = True)
            if int(stdin.readline()) == 0:
                break

