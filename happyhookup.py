from sys import stdin

def DFS(s,adjList):
    frontier,visited = [s],[False for _ in range(len(adjList))]
    visited[s] = True
    while frontier:
        u = frontier.pop()
        for v in adjList[u]:
            if not visited[v]:
                frontier.append(v)
                visited[v] = True
    return {x for x in range(len(visited)) if visited[x]}
                
n,m = map(int,stdin.readline().split())
adjList = [[] for _ in range(n)]
for _ in range(m):
    u,v = map(lambda x: int(x) - 1,stdin.readline().split())
    adjList[u].append(v)
a,b = map(lambda x: int(x) - 1,stdin.readline().split())
# perform DFS from both a and b
r1,r2 = DFS(a,adjList),DFS(b,adjList)
for i in range(n):
    if i in r1 and i in r2:
        print(f"yes\n{i + 1}")
        break
else:
    print("no")
