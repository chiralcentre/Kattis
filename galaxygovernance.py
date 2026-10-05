from sys import stdin,stdout

n,m,k = map(int,stdin.readline().split())
adjList,deg = [[] for _ in range(n)],[0 for _ in range(n)]
for _ in range(m):
    a,b = map(int,stdin.readline().split())
    a -= 1; b -= 1
    adjList[a].append(b)
    adjList[b].append(a)
    deg[a] += 1
    deg[b] += 1
# original graph was a DAG with every vertex of in degree k
# in original graph, final vertex in topological order has no outgoing edges and has in degree k, so it has degree <= k in undirected graph too
# graph always contains at least one vertex with k or fewer neighbours, and that stays true no matter how many such vertices are deleted
# the idea is to arrange the colouring sequence such that every vertex, when its turn coms, faces at most k coloured neighbours. Then with k + 1 colours, one is always spare.
frontier = [v for v in range(n) if deg[v] <= k]
order = []
while frontier:
    u = frontier.pop()
    deg[u] = -1 # mark as visited
    order.append(u)
    for v in adjList[u]:
        if deg[v] >= 0:
            deg[v] -= 1
            if deg[v] == k:
                frontier.append(v)
# colour in reverse order
colour = [-1 for _ in range(n)]
# stamp[c] = u means that colour c is blocked by vertex u
# code runs in O(n + m) time
stamp = [-1 for _ in range(k + 1)]
for i in range(len(order) - 1, -1, -1):
    u = order[i]
    for v in adjList[u]:
        if colour[v] >= 0:
            stamp[colour[v]] = u
    c = 0
    while stamp[c] == u:
        c += 1
    colour[u] = c
stdout.write(" ".join(map(lambda x: str(x + 1),colour)))
    
