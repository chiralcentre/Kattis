from sys import stdin
from math import ceil

sizes = {"S": 6, "M": 8, "L": 12}

n = int(stdin.readline())
pieces = {}
for _ in range(n):
    s,f = stdin.readline().split()
    pieces[s] = pieces.get(s,0) + int(f)
print(sum(ceil(v / sizes[k]) for k,v in pieces.items()))
