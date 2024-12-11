from sys import stdin,stdout
from collections import deque

#O(N)
def isUniqueToposort(toposort,adjList):
    for i in range(len(toposort) - 1):
        if toposort[i+1] not in adjList[toposort[i]]:
            return False
    return True

#check if an edge exists between consecutive vertices in topological order to ensure toposort is unique
#overall time complexity: O(N + K)
N,K = map(int,stdin.readline().split())
names = stdin.readline().split()
mappings = {}
for i in range(N):
    mappings[names[i]] = i
adjList,indeg = [set() for _ in range(N)],[0 for _ in range(N)]
#perform toposort with Kahn's algorithm in O(N + K) time
for _ in range(K):
    u,d,v = stdin.readline().split()
    u = mappings[u]
    v = mappings[v]
    if d == ">":
        adjList[v].add(u)
        indeg[u] += 1
    else:
        adjList[u].add(v)
        indeg[v] += 1
frontier,toposort = deque([v for v in range(N) if indeg[v] == 0]),[]
while frontier:
    u = frontier.popleft()
    toposort.append(u)
    for v in adjList[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            frontier.append(v)
stdout.write(" ".join(names[v] for v in toposort)) if isUniqueToposort(toposort,adjList) and len(toposort) == N else stdout.write("veit ekki")
