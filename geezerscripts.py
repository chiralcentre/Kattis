from sys import stdin,stdout
from heapq import heappush,heappop

#code runs in O(m log n) time
INF = pow(10,18)
def modifiedDjikstra(adjList,N,s,e):
    D = [INF for _ in range(N)]; D[s] = 0
    PQ = []; heappush(PQ,(0,s))
    while PQ: #modified Djikstra's is used with O(M log M) time complexity
        d,u = heappop(PQ)
        if u == e:
            return d
        if d == D[u]: # check if this is the superior copy
            for v,w in adjList[u]:
                if D[v] > D[u] + w: # can relax
                    D[v] = D[u] + w
                    heappush(PQ,(D[v],v))
    return -1

A,H = map(int,stdin.readline().split())
n,m = map(int,stdin.readline().split())
adjList = [[] for _ in range(n)]
for i in range(m):
    u,v,a,h = map(int,stdin.readline().split())
    u -= 1; v -= 1
    # weight of edge = health lost by Unnar
    mult = h // A - (h % A == 0)
    w = mult * a
    adjList[u].append((v,w))
d = modifiedDjikstra(adjList,n,0,n - 1)
print("Oh no") if d == -1 or d >= H else print(H - d)
