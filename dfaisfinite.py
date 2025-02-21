from sys import stdin
from collections import deque

def kahnsAlgorithm(adjList,indeg,useful):
    frontier = deque([])
    for v in range(len(indeg)):
        if indeg[v] == 0 and v in useful:
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

n,c,s,f = map(int,stdin.readline().split())
s -= 1
stdin.readline().strip()
final_states = set(map(lambda x: int(x) - 1, stdin.readline().split()))
adjMat = [set(map(lambda x: int(x) - 1, stdin.readline().split())) for _ in range(n)]
adjList,invAdjList,indeg = [set() for _ in range(n)],[set() for i in range(n)],[0 for _ in range(n)]
for u in range(n):
    for v in adjMat[u]:
        adjList[u].add(v)
        invAdjList[v].add(u)
        indeg[v] += 1

# perform DFS using adjacency list from start state to check which states are reachable in O(n + nc) time
visited,reachable = [False for _ in range(n)],{s}
visited[s],frontier = True,[s]
while frontier:
    u = frontier.pop()
    for v in adjList[u]:
        if not visited[v]:
            visited[v] = True
            frontier.append(v)
            reachable.add(v)
# check if there is a reachable final state
if reachable.intersection(final_states):
    # perform DFS using adjacency list from each reachable final state to check which states do not have a path to the final state in O(n + nc) time
    visited,possible = [False for _ in range(n)],set()
    for state in final_states:
        if state in reachable:
            visited[state] = True
            frontier = [state]
            while frontier:
                u = frontier.pop()
                possible.add(u)
                for v in invAdjList[u]:
                    if not visited[v]:
                        visited[v] = True
                        frontier.append(v)
            
    useful = reachable.intersection(possible)
    # remove all edges to useless states in O(nc)
    for u in range(n):
        if u in useful:
            new_edges = set()
            for v in adjList[u]:
                if v not in useful:
                    indeg[v] -= 1
                else:
                    new_edges.add(v)
            adjList[u] = new_edges
        else:
            for v in adjList[u]:
                indeg[v] -= 1
            adjList[u] = set()
    # use Kahn's algorithm to check if subgraph has cycles in O(n + nc) time
    toposort = kahnsAlgorithm(adjList,indeg, useful)
    print("finite") if len(toposort) == len(useful) else print("infinite")
else:
    print("finite")



