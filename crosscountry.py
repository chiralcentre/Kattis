from sys import stdin,stdout
from heapq import heappush,heappop

def modifiedDjikstra(N,S,T,adjList):
    INF = 1000000000 # use 1 billion to represent infinity
    D = [INF for _ in range(N)]; D[S] = 0
    PQ = [(0,S)] #start from source
    while PQ:
        d,u = heappop(PQ)
        if u == T:
            return str(d)
        if d == D[u]:
            for v,w in adjList[u]:
                if D[v] > D[u] + w:
                    D[v] = D[u] + w
                    heappush(PQ,(D[v],v))
    
N,S,T = map(int,stdin.readline().split())
adjList = [[] for i in range(N)]
for i in range(N): #O(N^2)
    line = list(map(int,stdin.readline().split()))
    for j in range(N):
        if i != j:
            adjList[i].append((j,line[j]))
stdout.write(modifiedDjikstra(N,S,T,adjList))
