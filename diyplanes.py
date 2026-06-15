from sys import stdin

def solve(adjList,indeg):
    frontier = []
    for v in range(len(indeg)):
        if indeg[v] == 0:
            frontier.append(v)
    cleared = 0
    while frontier:
        cleared += len(frontier)
        if len(frontier) > 1:
            return "NO"
        new_frontier = []
        for u in frontier:
            for v in adjList[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    new_frontier.append(v)
        frontier = new_frontier
    return "YES" if cleared == len(adjList) else "NO"

#perform Kahns algorithm, and if at any time during the algorithm the frontier contains more than one node with zero indegree, the answer is no
#overall time complexity: O(N + M)
N,M = map(int,stdin.readline().split())
adjList,indeg = [[] for _ in range(N)],[0 for _ in range(N)]
#perform toposort with Kahn's algorithm in O(N + K) time
for _ in range(M):
    u,v = map(int,stdin.readline().split())
    adjList[u].append(v)
    indeg[v] += 1
print(solve(adjList,indeg))
