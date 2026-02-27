from heapq import heappush,heappop
from sys import stdin

INF = 1000000000 #use 1 billion to represent infinity
def modifiedDjikstra(adjList,N,s,e):
    parents = [None for _ in range(N)]
    D = [INF for _ in range(N)]; D[s] = 0
    PQ = []; heappush(PQ,(0,s))
    while PQ: #modified Djikstra's is used with O(M log M) time complexity
        d,u = heappop(PQ)
        if u == e:
            return parents,d
        if d == D[u]: # check if this is the superior copy
            for v,w in adjList[u]:
                if D[v] > D[u] + w: # can relax
                    D[v] = D[u] + w
                    parents[v] = u
                    heappush(PQ,(D[v],v))
    return parents,-1

def reconstruct_path(parents, start, end):
    path = []
    current = end
    while current != start:
        path.append(current)
        current = parents[current]
    path.append(start)
    return path[::-1] # Reverse the path

# code runs in O(E log V) time = O(n^2 log n) time
n = int(stdin.readline())
adjList = [[] for _ in range(n)]
for i in range(n - 1):
    costs = list(map(int,stdin.readline().split()))
    for j in range(len(costs)):
        adjList[i].append((i + 1 + j, costs[j]))
parents,cost = modifiedDjikstra(adjList,n,0,n - 1)
print(" ".join(str(num + 1) for num in reconstruct_path(parents,0,n - 1)))
print(cost)
