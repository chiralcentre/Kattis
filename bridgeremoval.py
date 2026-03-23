from sys import stdin,stdout
from math import ceil

N = int(stdin.readline())
adjList = [[] for _ in range(N)]
for _ in range(N - 1):
    u,v = map(lambda x: int(x) - 1,stdin.readline().split())
    adjList[u].append(v)
    adjList[v].append(u)
# perform DFS from node 0
# find all leaves of tree
# view adding an edge as “covering” all edges on the path between its endpoints (they are no longer bridges)
# we need to add the fewest edges to cover all tree edges.
leaves,frontier,visited = [],[0],[False for _ in range(N)]
visited[0] = True
while frontier:
    u = frontier.pop()
    if len(adjList[u]) == 1:
        leaves.append(u)
    for v in adjList[u]:
        if not visited[v]:
            visited[v] = True
            frontier.append(v)
stdout.write(f"{ceil(len(leaves) / 2)}\n")
for i in range(len(leaves) // 2):
    stdout.write(f"{leaves[i] + 1} {leaves[i + len(leaves) // 2] + 1}\n")
# add node 0 as dummy node to connect last node if last node cannot be paired with existing leaf
if len(leaves) % 2:
    stdout.write(f"1 {leaves[-1] + 1}\n")
   
