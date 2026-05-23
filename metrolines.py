from sys import stdin,stdout
from heapq import heappop,heappush

N,M = map(int,stdin.readline().split())
lines = [[] for _ in range(N + 1)]
for _ in range(M):
    L,R,C = map(int,stdin.readline().split())
    lines[L].append((C,R))
active,D,costs = [],[-1 for _ in range(N + 1)],0
D[0] = 0
# the optimal strategy is: At every adjacent step i → i+1, use the cheapest metro line currently available that covers this segment.
# code runs in O(M log M)
for i in range(N):
    for C,R in lines[i]:
        heappush(active,(C,R))
    while active and active[0][1] <= i:
        heappop(active)
    if not active:
        break
    else:
        D[i + 1] = D[i] + active[0][0]
for i in range(1,N + 1):
    stdout.write(f"{D[i]}\n")
