from sys import stdin,stdout
from math import ceil

m,p,n = map(int,stdin.readline().split())
episodes = 0
curr = m
for i in range(n):
    w = int(stdin.readline())
    if w >= curr:
        extra = w - curr
        curr = ceil(m - ((p * extra) / 100))
        episodes += 1
    else:
        curr = ceil(m + ((p * (curr - w)) / 100)) 
stdout.write(f"{episodes}\n")
