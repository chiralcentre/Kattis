from sys import stdin,stdout
from heapq import heappush,heappop

# code runs in O(E log V) time
# V = O(n * k1 * k2), E = M
INF = pow(10,20)
def modifiedDjikstra(s,e,n,k1,k2,adjList): 
    #D[a][b][c] represents smallest distance to point a using b red tracks and c blue tracks
    D = [[[INF for j in range(k2 + 1)] for j in range(k1 + 1)] for i in range(n)]
    D[s][0][0] = 0; PQ = [(0,s,0,0)]
    while PQ:
        d,u,a,b = heappop(PQ)
        if d == D[u][a][b]:
            if u == T and a == k1 and b == k2:
                return d
            for v,w,c in adjList[u]:
                nd = d + w
                if c == 0 and D[v][a][b] > nd:
                    D[v][a][b] = nd
                    heappush(PQ,(D[v][a][b],v,a,b))
                elif c == 1 and a + 1 <= k1 and D[v][a + 1][b] > nd:
                    D[v][a + 1][b] = nd
                    heappush(PQ,(D[v][a + 1][b],v,a + 1,b))
                elif c == 2 and b + 1 <= k2 and D[v][a][b + 1] > nd:
                    D[v][a][b + 1] = nd
                    heappush(PQ,(D[v][a][b + 1],v,a,b + 1))
    return -1

N,M,k1,k2 = map(int,stdin.readline().split())
adjList = [[] for _ in range(N)]
for i in range(M):
    u,v,w,c = map(int,stdin.readline().split())
    u -= 1; v -= 1 #offset by 1
    adjList[u].append((v,w,c))
    adjList[v].append((u,w,c))
S,T = map(lambda x: int(x) - 1, stdin.readline().split()) 
print(modifiedDjikstra(S,T,N,k1,k2,adjList))
