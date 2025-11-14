from sys import stdin
from heapq import heappush,heappop

INF = 1000000000 #use 1 billion to represent infinity
def modifiedDjikstra(adjList,N,s):
    D = [INF for _ in range(N)]; D[s] = 0
    PQ = []; heappush(PQ,(0,s))
    while PQ: #modified Djikstra's is used with O(M log M) time complexity
        d,u = heappop(PQ)
        if d == D[u]: # check if this is the superior copy
            for v,w in adjList[u]:
                if D[v] > D[u] + w: # can relax
                    D[v] = D[u] + w
                    heappush(PQ,(D[v],v))
    return D

# index 0 = Denver, index 1 = Ft.Collins, index 2 = Colorado Springs
costs = [[0 for _ in range(3)] for j in range(3)]
a,b,c = map(int,stdin.readline().split())
n = int(stdin.readline())
costs[0][1] = costs[1][0] = a
costs[0][2] = costs[2][0] = b
costs[1][2] = costs[2][1] = c
profits = [list(map(int,stdin.readline().split())) for _ in range(3)]
# node 0 is super node
# node 3 * i + 1, 3 * i + 2, 3 * i + 3 is location 0, 1 and 2 on the ith day (i is 0 indexed)
adjList = [[] for i in range(1 + n * 3)]
adjList[0].append((1,-profits[0][0]))
adjList[0].append((2,-profits[1][0]))
adjList[0].append((3,-profits[2][0]))
for i in range(n - 1):
    for j in range(3):
        for k in range(3):
            u = 3 * i + j + 1
            v = 3 * (i + 1) + k + 1
            adjList[u].append((v, -profits[k][i + 1] + costs[j][k]))
# code runs in O(E log V) = O(9N log 3N)
P = modifiedDjikstra(adjList,1 + n * 3, 0)
print(-min(P[-1],P[-2],P[-3]))
    
