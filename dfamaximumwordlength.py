from sys import stdin
from collections import deque

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

# assume there are no cycles on paths to final states
n,c,s,f = map(int,stdin.readline().split())
s -= 1
stdin.readline().strip()
final_states = set(map(lambda x: int(x) - 1, stdin.readline().split()))
adjMat = [list(map(lambda x: int(x) - 1, stdin.readline().split())) for _ in range(n)]
adjList,invAdjList,indeg = [set() for _ in range(n)],[set() for i in range(n)],[0 for _ in range(n)]
for u in range(n):
    for v in adjMat[u]:
        adjList[u].add(v)
        invAdjList[v].add(u)
        indeg[v] += 1
# perform DFS using inverted adjacency list from each final state to check which states do not have a path to the final state in O(n + nc) time
visited,reachable = [False for _ in range(n)],set()
for state in final_states:
    visited[state] = True
    frontier = [state]
    while frontier:
        u = frontier.pop()
        reachable.add(u)
        for v in invAdjList[u]:
            if not visited[v]:
                visited[v] = True
                frontier.append(v)
unreachable = {x for x in range(n) if x not in reachable}
# remove all edges to unreachable states in O(nc)
for u in range(n):
    if u not in unreachable:
        new_edges = set()
        for v in adjList[u]:
            if v in unreachable:
                indeg[v] -= 1
            else:
                new_edges.add(v)
        adjList[u] = new_edges

# graph should now be directed acyclic
# use Kahn's algorithm to find longest path in DAG in O(n + nc) time
toposort = kahnsAlgorithm(adjList,indeg)
INF = pow(10,9)
d = [INF for _ in range(n)]; d[s] = 0
for u in toposort:
    if d[u] != INF:
        for v in adjList[u]:
            if d[v] > d[u] - 1: # negate edges, edge weight = -1
                d[v] = d[u] - 1
longest = -1
for i in range(n):
    if i in final_states and d[i] != INF:
        longest = max(longest, -d[i])
print(longest)

