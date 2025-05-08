from sys import stdin,stdout
from heapq import heappush,heappop

INF = pow(10,15)
def modifiedDjikstra(n,s,e): 
    #D[a][b] represents smallest distance to point a,
    #b = 0 if special edge with A380 is not encountered, b = 1 otherwise
    D = [[INF for j in range(2)] for i in range(n)]
    D[s][0] = 0; PQ = [(0,s,0)]
    while PQ:
        d,a,b = heappop(PQ)
        if d == D[a][b]:
            for v,w,c in adjList[a]:
                t = max(c,b)
                if D[v][t] > d + w:
                    D[v][t] = d + w
                    heappush(PQ,(D[v][t],v,t))
    return -1 if D[e][1] == INF else D[e][1]

# code runs in O(F log A) time
A,F = map(int,stdin.readline().split())
adjList = [[] for _ in range(A)]
for _ in range(F):
    O,D,C,M = stdin.readline().split()
    u,v,w = map(int,[O,D,C])
    has_A380 = (M == "A380")
    adjList[u].append((v,w,has_A380))
stdout.write(f"{modifiedDjikstra(A,0,A - 1)}\n")
