from sys import stdin

INF = pow(10,18)
n,m,s = map(int,stdin.readline().split())
M = sorted(map(int,stdin.readline().split()))
# greedily choose to smite the more time consuming monsters
t1 = sum(M[i] for i in range(n - s))
# run Floyd Warshall in O(n^3) time
adjMat = [[INF for i in range(n)] for j in range(n)]
for i in range(n):
    adjMat[i][i] = 0
for _ in range(m):
    u,v,w = map(int,stdin.readline().split())
    u -= 1; v -= 1
    t = min(adjMat[u][v],w) # in case of multiple edges
    adjMat[u][v] = adjMat[v][u] = t
for i in range(n):
    for j in range(n):
        for k in range(n):
            if adjMat[i][k] + adjMat[k][j] < adjMat[i][j]:
                adjMat[i][j] = adjMat[i][k] + adjMat[k][j]
# run Held Karp Bitmask DP in O(2^n * n^2) time
dp = [[INF for i in range(n)] for j in range(1 << n)]
dp[1][0] = 0
for mask in range(1,1 << n):
    for v in range(n):
        if dp[mask][v] == INF:
            continue
        for u in range(n):
            if not (mask >> u & 1) and adjMat[v][u] < INF:
                dp[mask | 1 << u][u] = min(dp[mask | 1 << u][u],dp[mask][v] + adjMat[v][u])
t2 = min(dp[(1 << n) - 1][v] for v in range(n))
print(t1 + t2)
