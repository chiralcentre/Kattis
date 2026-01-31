from sys import stdin

n = int(stdin.readline())
adjList = [[] for _ in range(n)]
for _ in range(n - 1):
    u,v = map(int,stdin.readline().split())
    adjList[u].append(v)
    adjList[v].append(u)
frontier,ans,best,level = [0],0,1,0
visited = [False for _ in range(n)]
visited[0] = True
while frontier:
    new_frontier = []
    level += 1
    for u in frontier:
        for v in adjList[u]:
            if not visited[v]:
                visited[v] = True
                new_frontier.append(v)
    if len(new_frontier) > best:
        best,ans = len(new_frontier),level
    frontier = new_frontier
print(ans)
