from sys import stdin
from heapq import heappush,heappop

INF = pow(10,18)
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

N,M,K = map(int,stdin.readline().split())
adjList = [[] for _ in range(N)]
edges = []
for _ in range(M):
    a,b,c = map(int,stdin.readline().split())
    a -= 1; b -= 1
    adjList[a].append((b,c))
    adjList[b].append((a,c))
    edges.append((a,b,c))
# find d = shortest distance from vertex 1 to n using Djiksta in O(M log M) time
D = modifiedDjikstra(adjList,N,0)
d = D[N - 1]
# DFS from vertex 1 to n, and find all the edges in the component containing vertex 1 and n
# reuse Djikstra output from previous step to check reachability
# this component is guaranteed to exist, by question definition
# if there are less than k edges in the component, default to the answer from Djikstra
# else, take the k smallest edges and add up their sum in O(M log M) time
component_edges = [c for x, y, c in edges if D[x] < INF]
if len(component_edges) < K:
    print(d)
else:
    sorted_edges = sorted(component_edges)
    T = sum(sorted_edges[i] for i in range(K))
    print(min(d,T))
