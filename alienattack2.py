from sys import stdin

# codes runs in O(n + m) time
n,m = map(int,stdin.readline().split())
adjList = [[] for i in range(n)]
for i in range(m):
    u,v = map(lambda x: int(x) - 1, stdin.readline().split())
    adjList[u].append(v)
    adjList[v].append(u)

# find largest size of all components
visited,CC,ans = [False for i in range(n)],0,-1
for i in range(n):
    if not visited[i]:
        frontier = [i]
        visited[i] = True
        size = 0
        while frontier:
            u = frontier.pop()
            size += 1
            for v in adjList[u]:
                if not visited[v]:
                    frontier.append(v)
                    visited[v] = True
        ans = max(ans,size)
print(ans)
