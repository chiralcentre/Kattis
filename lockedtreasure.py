from sys import stdin,stdout
from math import comb

#there is a minimum of n choose m - 1 locks
#for each subset of m - 1 bandits, there must be at least one lock they cannot open
#for each subset of m - 1 bandits, there is one lock such that the keys are distributed to all others who are not in subset
#any group of m bandits must have a key to every lock

for _ in range(int(stdin.readline())):
    n,m = map(int,stdin.readline().split())
    stdout.write(f"{comb(n,m-1)}\n")
