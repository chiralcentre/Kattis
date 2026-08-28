from sys import stdin,setrecursionlimit

setrecursionlimit(10**9)
#DFS procedure has void return type
def DFS(u,c,L): #u is current vertex, c is colour to be assigned to u
    global colour,components,isBipartite
    components[u] = L
    if colour[u] != 2:
        if colour[u] != c: #colour of node is different from colour to be assigned
            isBipartite = False
        return 
    else: #not coloured yet
        colour[u] = c
        for v in adjList[u]:
            if c == 1:
                DFS(v,0,L)
            else: #c = 0
                DFS(v,1,L)

N,M,p = map(int,stdin.readline().split())
# perform bipartite colouring in O(N+M) time
# if graph is bipartite, assignments are possible
isBipartite = True
adjList,colour = [[] for _ in range(N)],[2 for _ in range(N)] #colour 2 means not visited
components,CC = [-1 for _ in range(N)],0
for i in range(M):
    u,v = map(int,stdin.readline().split())
    u -= 1; v -= 1
    adjList[u].append(v)
    adjList[v].append(u)
for u in range(N):
    if isBipartite and colour[u] == 2: #not coloured
        DFS(u,0,CC)
        CC += 1
print("impossible") if not isBipartite else print((pow(2,CC - 1,p) + 1) % p)
