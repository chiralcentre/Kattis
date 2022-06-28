from sys import stdin,stdout

def DFS(u,p):
    visited[u] = True
    global timer
    timer += 1
    entry[u],low[u] = timer,timer
    for v in adjList[u]:
        if v != p:
            if visited[v]:
                low[u] = min(low[u],entry[v])
            else:
                DFS(v,u)
                low[u] = min(low[u],low[v])
                if low[v] > entry[u]: #bridge found
                    global bridgeFound
                    bridgeFound = True
                    return
                    

while True:
    p,c = map(int,stdin.readline().split())
    if p == c == 0:
        break
    adjList,visited = [[] for _ in range(p)],[False for _ in range(p)]
    #entry[i] denotes entry time for node i
    #low[i] is the minimum of entry[i], the entry times entry[p] for each node p that is connected to node v via a back-edge (v,p) and the values of low[to] for each vertex to which is a direct descendant of v in the DFS tree
    entry,low = [-1 for _ in range(p)],[-1 for _ in range(p)]
    timer,bridgeFound = 0,False
    for i in range(c):
        a,b = map(int,stdin.readline().split())
        adjList[a].append(b); adjList[b].append(a)
    #existence of a bridge means that it is possible that a pair could lose each other’s numbers and make it so that not everybody can be invited to the party
    #perform recursive DFS in O(p + c) time
    for i in range(p):
        if not visited[i]:
            DFS(i,-1) #parent set as -1
    stdout.write('Yes\n') if bridgeFound else stdout.write('No\n')
