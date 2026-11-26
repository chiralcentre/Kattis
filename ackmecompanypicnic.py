from sys import stdin,setrecursionlimit

setrecursionlimit(1000000)

# runs in O(n) time
def maximum_weight_independent_set(n,adjList,W):
    dp = [[0, 0] for _ in range(n)]
    def dfs(u, parent):
        dp[u][1] = W[u]
        dp[u][0] = 0
        for v in adjList[u]:
            if v == parent or v == u:
                continue
            dfs(v, u)
            # Select u -> cannot select v
            dp[u][1] += dp[v][0]
            # Don't select u -> choose best state of v
            dp[u][0] += max(dp[v][0], dp[v][1])
    dfs(0, -1)
    return max(dp[0][0], dp[0][1])

n = int(stdin.readline())
adjList = [[] for _ in range(n)]
W = [-1 for _ in range(n)]
for i in range(n):
    f,b = map(int,stdin.readline().split())
    adjList[b].append(i)
    W[i] = f
print(maximum_weight_independent_set(n,adjList,W))
