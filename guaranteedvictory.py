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

N,R = map(int,stdin.readline().split())
mapper = {}
adjList,indeg = [],[]
for i in range(N):
    r = stdin.readline().strip()
    mapper[r] = i
    adjList.append([])
    indeg.append(0)
for i in range(R):
    x = int(stdin.readline())
    lst = stdin.readline().split()
    a = lst[0]
    if a not in mapper:
        mapper[a] = len(adjList)
        adjList.append([])
        indeg.append(0)
    u = mapper[a]
    for j in range(1,x):
        y = lst[j]
        if y not in mapper:
            mapper[y] = len(adjList)
            adjList.append([])
            indeg.append(0)
        v = mapper[y]
        adjList[v].append(u)
        indeg[u] += 1

toposort = kahnsAlgorithm(adjList,indeg)
# check for cycles, else output number of nodes not visited by Kahns algorithm
print("GUARANTEED VICTORY") if len(toposort) == len(adjList) else print(len(adjList) - len(toposort))
