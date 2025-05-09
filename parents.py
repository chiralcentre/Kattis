from sys import stdin,stdout

#perform BFS from roots
for _ in range(int(stdin.readline())):
    m = int(stdin.readline())
    adjList = [[] for i in range(m)]
    mappings,frontier = [],[]
    for i in range(m):
        p,item = stdin.readline().split()
        p = int(p)
        if p != -1:
            adjList[p].append(i)
        else:
            frontier.append(i)
        mappings.append(item)
    visited = [False for _ in range(m)]
    for u in frontier:
        visited[u] = True   
    while frontier:
        new_frontier = []
        for u in frontier:
            for v in adjList[u]:
                if not visited[v]:
                    visited[v] = True
                    new_frontier.append(v)
        if not new_frontier: # reached deepest layer
            stdout.write(" ".join(sorted(map(lambda x: mappings[x], frontier))))
            stdout.write("\n")
            break
        frontier = new_frontier
