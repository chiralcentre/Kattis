from sys import stdin

def solve(adjList,counter):
    frontier = [0]
    visited = [False for _ in range(counter)]
    visited[0] = True
    d = 0
    while frontier:
        new_frontier = []
        d += 1
        for u in frontier:
            for v in adjList[u]:
                if v == 0:
                    return str(d)
                if not visited[v]:
                    visited[v] = True
                    new_frontier.append(v)
        frontier = new_frontier
    return "NO BLACK HOLE"

N = int(stdin.readline())
mappings,counter = {},0
start = stdin.readline().strip()
mappings[start] = counter
counter += 1
adjList = [[]]
for _ in range(N):
    a,b = stdin.readline().split()
    if a not in mappings:
        mappings[a] = counter
        counter += 1
        adjList.append([])
    if b not in mappings:
        mappings[b] = counter
        counter += 1
        adjList.append([])
    adjList[mappings[a]].append(mappings[b])
print(solve(adjList,counter))
