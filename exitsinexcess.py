from sys import stdin,stdout,setrecursionlimit

setrecursionlimit(1000000)
def DFS(u,p):
    global status,hasCycle,adjList,removed
    status[u] = 1
    for v,r in adjList[u]:
        if v != p:
            if status[v] == 1:
                hasCycle = True
                removed.append(r)
            elif status[v] == -1:
                DFS(v,u)
        else:
            hasCycle = True
            removed.append(r)
    status[u] = 2
    
n,m = map(int,stdin.readline().split())
adjList = [[] for _ in range(n)]
for i in range(1,m + 1):
    u,v = map(lambda x: int(x) - 1, stdin.readline().split()) # offset by 1 due to zero indexing
    adjList[u].append((v,i))

# -1 = NOT_VISITED, 1 = VISITING, 2 = VISITED
status,removed = [-1 for i in range(n)],[]
hasCycle = False
for u in range(n):
    if status[u] == -1:
        DFS(u,-1)
if len(removed) <= (m >> 1):
    stdout.write(f"{len(removed)}\n")
    for r in removed:
        stdout.write(f"{r}\n")
else:
    # choose to remove complement set of edges
    stdout.write(f"{m - len(removed)}\n")
    removed = set(removed)
    for i in range(1,m + 1):
        if i not in removed:
            stdout.write(f"{i}\n")
