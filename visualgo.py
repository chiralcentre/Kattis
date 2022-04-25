from sys import stdin,stdout
from heapq import heappush,heappop

V,E = map(int,stdin.readline().split())
adjList = [[] for _ in range(V)]
for i in range(E):
    u,v,w = map(int,stdin.readline().split())
    adjList[u].append((v,w))
s,t = map(int,stdin.readline().split())
# perform Djikstra's in O(E log V) time
INF = 1000000000000 #use 1 billion to represent infinity
D,spcount = [INF for _ in range(V)],[0 for _ in range(V)]
PQ = [(0,s)]; D[s] = 0; spcount[s] = 1; # there is one way to go from s to itself
while PQ:
    d,u = heappop(PQ)
    if d == D[u]:
        for v,w in adjList[u]:
            if D[v] > D[u] + w:
                D[v] = D[u] + w
                heappush(PQ,(D[v],v))
                spcount[v] = spcount[u]
            elif D[v] == D[u] + w:
                spcount[v] += spcount[u]
stdout.write(f'{spcount[t]}')
