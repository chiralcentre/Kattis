from sys import stdin,stdout
from math import ceil

def solve(a,b,c,i,k):
    # maximum of i steps taken, minimum of ceil(i / c) steps taken
    L = ceil(i / c)
    if L * a + 1 > k:
        return "impossible"
    for j in range(L,i + 1): # check every possible number of steps taken
        r = k - a * j - 1 # r represents part of end number that comes from the myRNG() addition
        if r == 0: # set both myRNG() to zero
            return "possible"
        t = 0
        for m in range(b - 1, 0, -1): #try all values of myRNG() for addition part
            t += r // m
            r %= m
            if r == 0:
                if t <= j:
                    return "possible"
                break # not possible for current j
    return "impossible"

for line in stdin:
    a,b,c,i,k = map(int,line.split())
    stdout.write(f"{solve(a,b,c,i,k)}\n")

