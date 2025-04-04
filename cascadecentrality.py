from sys import stdin,stdout

N = int(stdin.readline())
adjList = [[] for _ in range(N)]
for i in range(N - 1):
    u,v = map(lambda x: int(x) - 1, stdin.readline().split())
    adjList[u].append(v)
    adjList[v].append(u)
# because there is only one path between node u and v, X_uv = X_vu
X = [[0 for i in range(N)] for j in range(N)]
# perform DFS from each node in O(N * (N + N - 1)) = O(N^2) 
for i in range(N):
    visited = [False for _ in range(N)]
    visited[i] = True
    frontier = [i]
    X[i][i] = 1
    while frontier:
        u = frontier.pop()
        for v in adjList[u]:
            if not visited[v]:
                visited[v] = True
                frontier.append(v)
                X[i][v] = X[i][u] * len(adjList[v])
total = 0
for i in range(N):
    total += 1
    for j in range(N):
        if i != j:
            total += 1 / X[i][j]
print(total / N)
        
