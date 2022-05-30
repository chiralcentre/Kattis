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

itemToIndex,indexToItem,N = {},{},int(stdin.readline())
for i in range(N):
    name = stdin.readline().strip()
    itemToIndex[name] = i #since all items are different
    indexToItem[i] = name
# perform bipartite colouring in O(N+M) time
# if graph is bipartite, buying the tiems is possible
isBipartite = True
adjList,colour = [[] for _ in range(N)],[2 for _ in range(N)] #colour 2 means not visited
for i in range(int(stdin.readline())):
    p1,p2 = stdin.readline().split()
    a,b = itemToIndex[p1],itemToIndex[p2]
    adjList[a].append(b); adjList[b].append(a)
for u in range(N):
    if isBipartite and colour[u] == 2: #not coloured
        DFS(u,0)
if isBipartite:
    firstGroup,secondGroup = [],[]
    for i in range(N):
        firstGroup.append(indexToItem[i]) if colour[i] == 0 else secondGroup.append(indexToItem[i])
    stdout.write(" ".join(item for item in firstGroup) + "\n")
    stdout.write(" ".join(item for item in secondGroup) + "\n")
else:
    stdout.write("impossible\n")

