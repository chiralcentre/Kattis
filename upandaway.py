from sys import stdin,stdout
from heapq import heappush,heappop

INF = 1000000000 #use 1 billion to represent infinity
def modifiedDjikstra(adjMat,h,n,k,s,e):
    # D[a][b] represents the shortest time to get to location a with b uses of fireworks
    D = [[INF for _ in range(k + 1)] for i in range(n)]
    D[s][0] = 0
    PQ = []; heappush(PQ,(0,s,0))
    while PQ: 
        d,u,f = heappop(PQ)
        if u == e:
            return d
        if d == D[u][f]: # check if this is the superior copy
            for v in range(n):
                if v != u:
                    diff = h[v] - h[u]
                    if diff <= 0: #can fly over directly   
                        if D[v][f] > D[u][f] + adjMat[u][v]:
                            D[v][f] = D[u][f] + adjMat[u][v]
                            heappush(PQ,(D[v][f],v,f))
                    elif f + diff <= k and D[v][f + diff] > D[u][f] + adjMat[u][v]:
                        D[v][f + diff] = D[u][f] + adjMat[u][v]
                        heappush(PQ,(D[v][f + diff],v,f + diff))
    return -1

n,x,k = map(int,stdin.readline().split())
h = list(map(int,stdin.readline().split()))
adjMat = [list(map(int,stdin.readline().split())) for i in range(n)]
stdout.write(f"{modifiedDjikstra(adjMat,h,n,k,0,x - 1)}\n") #offset by 1 due to zero indexing
