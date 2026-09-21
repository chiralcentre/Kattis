from sys import stdin
from heapq import heappush,heappop

INF = pow(10,18)
def dji(adjList,N,s,hi):
    D = [INF for _ in range(N)]; D[s] = 0
    PQ = []; heappush(PQ,(0,s))
    while PQ: 
        d,u = heappop(PQ)
        if d == D[u]: 
            for v,lw,hw in adjList[u]:
                nd = d + (hw if hi else lw)
                if D[v] > nd:
                    D[v] = nd
                    heappush(PQ,(D[v],v))
    return D

n,m = map(int,stdin.readline().split())
b,g = map(lambda x: int(x) - 1, stdin.readline().split()) # offset by 1 due to zero indexing
adjList = [[] for _ in range(n)]
for _ in range(m):
    u,v,w,s = map(int,stdin.readline().split())
    u -= 1; v -= 1
    adjList[u].append((v,w - s,w + s))

blo = dji(adjList,n,b,False)
bhi = dji(adjList,n,b,True)
glo = dji(adjList,n,g,False)
ghi = dji(adjList,n,g,True)
# blue's arrival time at p ranges over [blo, bhi], yellow's over [glo, ghi]
# each team can take different times over the same edge as long as it is within range
res = [p + 1 for p in range(n) if blo[p] != INF and glo[p] != INF and blo[p] <= ghi[p] and glo[p] <= bhi[p]]
if not res:
    print("Thessi leikur verdur sennilega leidinlegur")
else:
    print(" ".join(str(node) for node in sorted(res)))
