from sys import stdin,stdout,setrecursionlimit
setrecursionlimit(10**9)

def DFS(u,c): #u is current vertex, c is colour to be assigned to u
    if colour[u] == 2: #not coloured yet
        colour[u] = c
        for v in adjList[u]:
            if c == 1:
                DFS(v,0)
            else: #c = 0
                DFS(v,1)

#graph given is undirected tree, and undirected tree is bipartite
# perform bipartite colouring in O(N+N-1) = O(N) time
N = int(stdin.readline()); colour = [2 for _ in range(N)] #colour 2 means not visited yet
adjList = [[] for _ in range(N)]; edgeList = []
for i in range(N-1):
    a,b = map(int,stdin.readline().split())
    a -= 1; b -= 1;
    adjList[a].append(b); adjList[b].append(a)
    edgeList.append((a,b))
for u in range(N):
    if colour[u] == 2: #not coloured
        DFS(u,0)
#all edges are directed from 0 to 1
for u,v in edgeList: #O(N)
    stdout.write("1\n") if colour[u] == 0 and colour[v] == 1 else stdout.write("0\n")
        
