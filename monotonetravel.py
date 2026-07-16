from sys import stdin
from heapq import heappush,heappop,heapify

# code runs in O(m log m)
# invariant: After fully processing the batch for weight w_i, D[v] = minimum total weight of any valid non-decreasing path from vertex 0 to v, all of whose edges have weight ≤ w_i
INF = 1e18
def monotone_shortest_path(n,edges,increasing=True):
    D = [INF] * n
    D[0] = 0
    edges_sorted = sorted(edges, key=lambda e: e[2], reverse=not increasing)
    i = 0
    while i < len(edges_sorted):
        j = i
        w = edges_sorted[i][2]
        # run Djikstra for all same weight edges
        adjList,V = {},set()
        while j < len(edges_sorted) and edges_sorted[j][2] == w:
            u,v,_ = edges_sorted[j]
            adjList.setdefault(u,[]).append((v,w))
            V.add(u); V.add(v)
            j += 1
        PQ = [(D[u],u) for u in V if D[u] < INF]
        heapify(PQ)
        while PQ:
            d,u = heappop(PQ)
            if d == D[u]:
                for v,w in adjList.get(u,[]):
                    if D[v] > d + w:
                        D[v] = d + w
                        heappush(PQ,(D[v],v))
        i = j
    return D[n - 1]

n,m = map(int,stdin.readline().split())
edges = []
for _ in range(m):
    u,v,w = map(int,stdin.readline().split())
    edges.append((u - 1, v - 1, w))
ans = min(monotone_shortest_path(n,edges,True),monotone_shortest_path(n,edges,False))
print("impossible") if ans == INF else print(ans)
