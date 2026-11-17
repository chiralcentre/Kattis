from sys import stdin,stdout

def lca(u,v):
    global L,depth,up
    # ensure that depth[u] >= depth[v]
    if depth[u] < depth[v]:
        u,v = v,u
    d = depth[u] - depth[v]
    while d:                       # lift deeper node, one set bit at a time
        k = (d & -d).bit_length() - 1 # get lowest set bit
        u = up[k][u]
        d &= d - 1
    if u == v:
        return u
    for k in range(L - 1, -1, -1):
        if up[k][u] != up[k][v]:
            u,v = up[k][u],up[k][v]
    return up[0][u]

mappings = {"P": 0, "C": 1, "I": 2}
n,k,q = map(int,stdin.readline().split())
adjList = [[] for _ in range(n)]
for i in range(n - 1):
    a,b = map(lambda x: int(x) - 1,stdin.readline().split())
    adjList[a].append((b,i))
    adjList[b].append((a,i))
roads = {}
for _ in range(k):
    x,r = stdin.readline().split()
    r = int(r) - 1
    if r not in roads:
        roads[r] = {mappings[x]}
    else:
        roads[r].add(mappings[x])
# arbitrarily root tree at node 0
# find depths of all nodes from root in O(N) time
INF = pow(10,18)
depth = [INF for _ in range(n)]
parent = [0 for _ in range(n)]
cnts = [[0 for _ in range(n)], [0 for _ in range(n)], [0 for _ in range(n)]]
depth[0] = 0
frontier = [0]
while frontier:
    u = frontier.pop()
    for v,r in adjList[u]:
        if depth[v] == INF:
            parent[v] = u
            depth[v] = depth[u] + 1
            frontier.append(v)
            venues = roads.get(r,set())
            for i in range(len(cnts)):
                cnts[i][v] = cnts[i][u]
                if i in venues:
                    cnts[i][v] += 1
L = max(1,n.bit_length())
up = [parent]
for _ in range(L - 1):
    prev = up[-1]
    curr = [prev[prev[v]] for v in range(n)]
    up.append(curr)
# the q queries are answered in O(q log n) time
for _ in range(q):
    u,v = map(lambda x: int(x) - 1, stdin.readline().split())
    c = lca(u,v)
    possible = True
    for i in range(len(cnts)):
        A = cnts[i][u] + cnts[i][v] - 2 * cnts[i][c]
        if A <= 0:
            possible = False
            break
    stdout.write("Y\n") if possible else stdout.write("N\n")
