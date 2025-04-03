from sys import stdin
from itertools import combinations

# total time complexity = O(2^N * N*2)
def possible(comb,adjList):
    for i in range(len(comb)):
        for j in range(i + 1, len(comb)):
            if comb[j] in adjList[comb[i]]:
                return False
    return True
            
N,M = map(int,stdin.readline().split())
adjList = [set() for i in range(N)]
items = [i for i in range(N)]
for i in range(M):
    u,v = map(lambda x: int(x) - 1, stdin.readline().split())
    adjList[u].add(v)
    adjList[v].add(u)

ans = 1 # empty pizza
for i in range(1,N + 1):
    for comb in combinations(items, i):
        if possible(comb,adjList):
            ans += 1
print(ans)
