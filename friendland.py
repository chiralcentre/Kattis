from sys import stdin,stdout
from random import getrandbits

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


N,Q = map(int,stdin.readline().split())
adjList = [[] for _ in range(N)]
for _ in range(N - 1):
    a,b = map(lambda x: int(x) - 1,stdin.readline().split())
    adjList[a].append(b)
    adjList[b].append(a)
val = [None for _ in range(N)]
for _ in range(N // 2):
    a,b = map(lambda x: int(x) - 1,stdin.readline().split())
    h = getrandbits(64)
    val[a] = h
    val[b] = h
# arbitrarily root tree at node 0
# find depths of all nodes from root in O(N) time
# path XOR is 0 only if no pair is split
INF = pow(10,18)
depth = [INF for _ in range(N)]
parent = [0 for _ in range(N)]
pre = [0 for _ in range(N)]
pre[0] = val[0]
depth[0] = 0
frontier = [0]
while frontier:
    u = frontier.pop()
    for v in adjList[u]:
        if depth[v] == INF:
            depth[v] = depth[u] + 1
            parent[v] = u
            pre[v] = pre[u] ^ val[v]
            frontier.append(v)
L = max(1,N.bit_length())
up = [parent]
for _ in range(L -1):
    prev = up[-1]
    curr = [prev[prev[v]] for v in range(N)]
    up.append(curr)

for _ in range(Q):
    a,b = map(lambda x: int(x) - 1,stdin.readline().split())
    c = lca(a,b)
    stdout.write(f":)\n") if (pre[a] ^ pre[b] ^ val[c]) == 0 else stdout.write(":(\n")
