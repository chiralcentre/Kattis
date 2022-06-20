from sys import stdin,stdout
from heapq import heappush,heappop,heapify

# the game is winnable if and only if
# 1. The total number of coins is even
# 2. The largest stack of coins <= all the other stacks combined together

# one possible strategy is to always pick from the two largest stacks
# It is easy to prove that if the first two conditions hold before such a move, they also hold after.

n = int(stdin.readline())
stacks = list(map(int,stdin.readline().split()))
largest,total = 0,0
for i in range(n):
    total += stacks[i]
    if stacks[i] > largest:
        largest = stacks[i]
        
if total%2 or total < 2*largest:
    stdout.write("no\n")
else:
    #negate to turn into max heap; do not put empty stacks into PQ
    PQ = [(-stacks[i],i+1) for i in range(n) if stacks[i] > 0]
    heapify(PQ)
    sol = []
    while len(PQ) > 1: #need to have at least two elements in PQ
        a,i = heappop(PQ); b,j = heappop(PQ)
        sol.append(f'{i} {j}')
        a += 1; b += 1
        if a != 0:
            heappush(PQ,(a,i))
        if b != 0:
            heappush(PQ,(b,j))
    stdout.write("yes\n"+"\n".join(row for row in sol)) if not PQ else stdout.write("no\n")
        
