from sys import stdin,stdout
from heapq import heappush,heappop

# code runs in O(2m log 2n) time
INF = pow(10,18) 
def modifiedDjikstra(adjList,n,s,t): 
    #D[a][b] represents smallest distance to point a,
    #b = 0 if coupon has been used, b = 1 otherwise
    D = [[INF for j in range(2)] for i in range(n)]
    D[s][0] = 0; PQ = [(0,s,0)]
    while PQ:
        d,u,c = heappop(PQ)
        if u == t:
            return d
        if d == D[u][c]:
            for v,w in adjList[u]:
                # use coupon
                if c == 0:
                    if D[v][1] > d + w // 2:
                        D[v][1] = d + w // 2
                        heappush(PQ,(D[v][1],v,1))
                if D[v][c] > d + w:
                    D[v][c] = d + w
                    heappush(PQ,(D[v][c],v,c))
    return -1

n,m = map(int,stdin.readline().split())
s,t = map(int,stdin.readline().split())
s -= 1; t -= 1
adjList = [[] for _ in range(n)]
for i in range(m):
    u,v,w = map(int,stdin.readline().split())
    u -= 1; v -= 1 #offset by 1
    adjList[u].append((v,w))
print(modifiedDjikstra(adjList,n,s,t))
