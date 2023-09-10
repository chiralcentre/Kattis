from sys import stdin,stdout
from collections import deque

# rephrase the problem: check if it is possible for target vertex k to have degree <= 1 by only removing edges where at least one end point has degree <= 1 at any time
def solve(adjList,deg,n,k):
    #perform BFS from vertices with degree 1, vertices with degree 0 can be ignored
    frontier = deque([])
    for i in range(n):
        if deg[i] <= 1:
            if i + 1 == k:
                return "YES"
            elif deg[i] == 1:
                frontier.append(i)
                deg[i] -= 1
    while frontier:
        u = frontier.popleft()
        for v in adjList[u]:
            if deg[v] > 0:
                deg[v] -= 1
                if deg[v] == 1:
                    frontier.append(v)
                    if v + 1 == k:
                        return "YES"
    return "NO"
        
                    
n,k,m = map(int,stdin.readline().split())
adjList,deg = [[] for _ in range(n)],[0 for _ in range(n)]
for i in range(m):
    u,v = map(lambda x: int(x) - 1, stdin.readline().split())
    adjList[u].append(v)
    adjList[v].append(u)
    deg[u] += 1; deg[v] += 1
stdout.write(f"{solve(adjList,deg,n,k)}\n")
    
