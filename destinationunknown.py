from sys import stdin,stdout
from heapq import heappush,heappop

INF = 1000000000 #use 1 billion to represent infinity
def modifiedDjikstra(s,n,g,h): 
    #D[a][b] represents smallest distance to point a,
    #b = 0 if special edge is not encountered, b = 1 otherwise
    D = [[INF for j in range(2)] for i in range(n)]
    D[s][0] = 0; PQ = [(0,s,0)]
    while PQ:
        d,u,c = heappop(PQ)
        if d == D[u][c]:
            for v,w in adjList[u]:
                if (u == g and v == h) or (u == h and v == g):
                    if D[v][1] > d + w:
                        D[v][1] = d + w
                        heappush(PQ,(D[v][1],v,1))
                else:
                    if D[v][c] > d + w:
                        D[v][c] = d + w
                        heappush(PQ,(D[v][c],v,c))
    return D

for _ in range(int(stdin.readline())):
    #number of vertices = n, number of edges = m
    n,m,t = map(int,stdin.readline().split())
    s,g,h = map(int,stdin.readline().split())
    s -= 1; g -= 1; h -= 1 #offset by 1
    adjList = [[] for _ in range(n)]
    for i in range(m):
        u,v,w = map(int,stdin.readline().split())
        u -= 1; v -= 1 #offset by 1
        adjList[u].append((v,w))
        adjList[v].append((u,w))
    destinations = sorted([int(stdin.readline()) - 1 for i in range(t)])
    D = modifiedDjikstra(s,n,g,h)
    ans = [d for d in destinations if D[d][1] < INF and D[d][1] == min(D[d])]
    stdout.write(' '.join(str(d + 1) for d in ans) + "\n") #add back the 1
    
