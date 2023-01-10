from sys import stdin,stdout
from collections import deque

#preconditions:
#1) graph must be directed acyclic
#2) adjList is a list of lists representing the graph in adjaceny list form
#3) indeg is a list of length V where indeg[v] represents the indegree of vertex v
#postconditions:
#1) indeg array is modified such that every entry is now 0
#2) returns an list of vertices in topological order
def kahnsAlgorithm(adjList,indeg):
    frontier = deque([])
    for v in range(len(indeg)):
        if indeg[v] == 0:
            frontier.append(v)
    toposort = []
    while frontier:
        u = frontier.popleft()
        toposort.append(u)
        for v in adjList[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                frontier.append(v)
    return toposort    

INF = 10**9
V,E = map(int,stdin.readline().split())
adjList,indeg = [[] for _ in range(V)],[0 for _ in range(V)]
for _ in range(E):
    u,v = map(lambda x: int(x) - 1, stdin.readline().split())
    adjList[u].append(v)
    indeg[v] += 1
#longest path must start from vertices with 0 indeg
d,p = [INF for _ in range(V)],[-1 for _ in range(V)]
for i in range(V):
    if indeg[i] == 0:
        d[i] = 0
#carry out toposort with Kahn's algorithm in O(V + E) time
toposort = kahnsAlgorithm(adjList,indeg)
#relax edges in topological order
for u in toposort:
    if d[u] != INF:
        for v in adjList[u]:
            if d[v] > d[u] - 1: #negate edges, edge weight = -1
                d[v] = d[u] - 1
                p[v] = u
#find ending vertex on longest path
lowest,index = 1,-1
for i in range(V):
    if d[i] < lowest:
        index = i
        lowest = d[i]
#reconstruct path
path = deque([])
while p[index] != -1:
    path.appendleft(index)
    index = p[index]
path.appendleft(index)
stdout.write(f"{len(path)}\n")
stdout.write(" ".join(str(u + 1) for u in path))
stdout.write("\n")
        
        

                

