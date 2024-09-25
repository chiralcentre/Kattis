from collections import deque
from sys import stdin

INF = 1000000000 #use 1 billion to represent infinity
def modifiedDjikstra(adjList,N,s,e):
    D = [INF for _ in range(N)]; D[s] = 0
    PQ = deque([(0,s)])
    while PQ:
        d,u = PQ.popleft()
        if u == e:
            return d
        if d == D[u]: # check if this is the superior copy
            for v,w in adjList[u]:
                if D[v] > D[u] + w: # can relax
                    D[v] = D[u] + w
                    if w == 1:
                        PQ.append((D[v],v))
                    else:
                        PQ.appendleft((D[v],v))
    return -1

# 0-1 Djikstra runs in O(E) time
N,M = map(int,stdin.readline().split())
adjList = [[] for _ in range(N)]
for i in range(M):
    a,b,c = map(int,stdin.readline().split())
    adjList[a - 1].append((b - 1, c))
    adjList[b - 1].append((a - 1, c))
print(modifiedDjikstra(adjList,N,0,N - 1))
