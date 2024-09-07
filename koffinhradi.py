from sys import stdin
from heapq import heappush,heappop

# overall algorithm runs in O(n log n)
n = int(stdin.readline())
tasks = [tuple(map(int,stdin.readline().split())) for _ in range(n)]
# sort in ascending order of deadline
tasks.sort(key = lambda x: x[1])
PQ,time,drinks = [],0,0
# convert to max heap by taking negation
for t,s in tasks:
    heappush(PQ,-t)
    time += t
    while time > s:
        # take most time consuming task, and halve the time taken
        longest = -heappop(PQ)
        half = longest >> 1
        heappush(PQ,-half)
        time -= longest - half
        drinks += 1
print(drinks)
