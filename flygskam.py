from sys import stdin,stdout
from math import cos,sin,acos,radians
from heapq import heappush,heappop

INF = 1000000000 #use 1 billion to represent infinity
def modifiedDjikstra(adjList,s,e):
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
                    
def greatCircleDistance(a,b,x,y):
    return 6381 * acos(cos(a) * cos(b) * cos(x - y) + sin(a) * sin(b))

N,M = map(int,stdin.readline().split())
adjList,mappings,coordinates = [[] for _ in range(N)],{},[]
S,T = stdin.readline().split()
for i in range(N):
    s,la,lo = stdin.readline().split()
    la,lo = float(la),float(lo)
    coordinates.append((la,lo))
    mappings[s] = i
for i in range(M):
    c,d = stdin.readline().split()
    u,v = mappings[c],mappings[d]
    a,x = coordinates[u]; b,y = coordinates[v]
    w = greatCircleDistance(radians(a),radians(b),radians(x),radians(y)) + 100 
    adjList[u].append((v,w))
    adjList[v].append((u,w))

stdout.write(f"{modifiedDjikstra(adjList,mappings[S],mappings[T])}\n")
    
    

