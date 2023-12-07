from sys import stdin,stdout
from heapq import heappush,heappop

INF = 1e12 #use 1 trillion to represent infinity
def modifiedDjikstra(adjList,N,s):
    D = [INF for _ in range(N)]; D[s] = 0
    PQ = []; heappush(PQ,(0,s))
    while PQ: #modified Djikstra's is used with O(M log M) time complexity
        d,u = heappop(PQ)
        if d == D[u]: # check if this is the superior copy
            for v,w in adjList[u]:
                if D[v] > D[u] + w: # can relax
                    D[v] = D[u] + w
                    heappush(PQ,(D[v],v))
    return D

n,m = map(int,stdin.readline().split())
lodging = list(map(int,stdin.readline().split()))
alfurAdjList = [[] for _ in range(n)]
benediktAdjList = [[] for _ in range(n)]
for _ in range(m):
    u,v,a,b = map(int,stdin.readline().split())
    u -= 1; v -= 1
    alfurAdjList[u].append((v,a))
    alfurAdjList[v].append((u,a))
    benediktAdjList[u].append((v,b))
    benediktAdjList[v].append((u,b))
    
d1,d2 = modifiedDjikstra(alfurAdjList,n,0),modifiedDjikstra(benediktAdjList,n,n - 1)
ans = INF
for i in range(n):
    ans = min(ans,d1[i] + d2[i] + lodging[i])
stdout.write(f"{ans}\n")
