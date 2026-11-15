from sys import stdin
from math import ceil
from heapq import heappush,heappop

INF = 1000000000 #use 1 billion to represent infinity
def modifiedDjikstra(adjList,N,s):
    D = [INF for _ in range(N)]; D[s] = 0
    PQ = []; heappush(PQ,(0,s))
    while PQ:
        d,u = heappop(PQ)
        if d == D[u]: # check if this is the superior copy
            for v,w in adjList[u]:
                if D[v] > D[u] + w: # can relax
                    D[v] = D[u] + w
                    heappush(PQ,(D[v],v))
    return D

# overall approach runs in O(M log N) time
B,N = map(int,stdin.readline().split())
sizes = []
for _ in range(B):
    U,F = map(int,stdin.readline().split())
    sizes.append((U,F))
adjList = [[] for _ in range(N + 1)]
for _ in range(int(stdin.readline())):
    u,v,w = map(int,stdin.readline().split())
    adjList[u].append((v,1/w))
    adjList[v].append((u,1/w))
D = modifiedDjikstra(adjList,N + 1,0)
print(ceil(sum(f * D[u] for u,f in sizes)))
