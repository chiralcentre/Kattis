from sys import stdin,stdout
from heapq import heappush,heappop

def modifiedDjikstra(n,items,adjList):
    INF = 1000000000 #use 1 billion to represent infinity
    D = [INF for i in range(n)]; D[0] = 0
    bestItems = [0 for i in range(n)]; bestItems[0] = items[0]
    PQ = [(0,0,items[0])] #start at source 0
    while PQ:
        d,u,t = heappop(PQ)
        if d == D[u]:
            for v,w in adjList[u]:
                if D[v] > D[u] + w:
                    D[v] = D[u] + w
                    bestItems[v] = bestItems[u] + items[v]
                    heappush(PQ,(D[v],v,bestItems[v]))
                elif D[v] == D[u] + w and bestItems[v] < bestItems[u] + items[v]:
                    bestItems[v] = bestItems[u] + items[v]
                    heappush(PQ,(D[v],v,bestItems[v]))
    return "impossible" if D[n-1] == INF else f'{D[n-1]} {bestItems[n-1]}'        
    
n = int(stdin.readline()); adjList = [[] for _ in range(n)]
items = list(map(int,stdin.readline().split()))
for i in range(int(stdin.readline())):
    a,b,d = map(int,stdin.readline().split())
    a -= 1; b -= 1; #offset by 1 due to zero indexing
    adjList[a].append((b,d))
    adjList[b].append((a,d))
stdout.write(modifiedDjikstra(n,items,adjList))
