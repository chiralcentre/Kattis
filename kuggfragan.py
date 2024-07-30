from sys import stdin,stdout,setrecursionlimit
setrecursionlimit(10**9)
#DFS procedure has void return type
def DFS(u,c): #u is current vertex, c is colour to be assigned to u
    if colour[u] != 2:
        if colour[u] != c: #colour of node is different from colour to be assigned
            global isBipartite # modify the global isBipartite variable
            isBipartite = False
        return 
    else: #not coloured yet
        colour[u] = c
        for v in adjList[u]:
            if c == 1:
                DFS(v,0)
            else: #c = 0
                DFS(v,1)

N,M = map(int,stdin.readline().split())
# perform bipartite colouring in O(N+M) time
# if graph is bipartite, the gears can work together
isBipartite = True
adjList,colour = [[] for _ in range(N)],[2 for _ in range(N)] #colour 2 means not visited
for i in range(M):
    u,v = map(int,stdin.readline().split())
    adjList[u].append(v)
    adjList[v].append(u)
for u in range(N):
    if isBipartite and colour[u] == 2: #not coloured
        DFS(u,0)
stdout.write("attend here\n") if isBipartite else stdout.write("no way\n")