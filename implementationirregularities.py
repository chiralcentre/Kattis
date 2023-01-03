from sys import stdin,stdout
from math import ceil

#sort problems by solve time, discarding any unsolved problems
#note that if there are C computers, and the team solves the ith problem after m minutes,
#the total computer time available for first i problems is C * m.
n = int(stdin.readline())
c = list(map(int,stdin.readline().split()))
solved = list(map(int,stdin.readline().split()))
pairs = sorted([(solved[i],i) for i in range(n) if solved[i] > - 1], key = lambda x: x[0])
ans,total = -1,0
for s,j in pairs:
    total += c[j]
    ans = max(ans,ceil(total/s))
stdout.write(f"{ans}\n")
