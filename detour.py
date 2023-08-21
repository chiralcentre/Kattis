from sys import stdin,stdout
from heapq import heappush,heappop

INF = 1000000000 #use 1 billion to represent infinity
def modifiedDjikstra(adjList,parent,N,s):
    D = [INF for _ in range(N)]; D[s] = 0
    PQ = []; heappush(PQ,(0,s))
    while PQ: #modified Djikstra's is used with O(M log N) time complexity
        d,u = heappop(PQ)
        if d == D[u]: # check if this is the superior copy
            for v,w in adjList[u]:
                if D[v] > D[u] + w: # can relax
                    D[v] = D[u] + w
                    parent[v] = u
                    heappush(PQ,(D[v],v))
    return D

def reachable(source,dest,adjList,p,parent):
    frontier = [source]
    p[source] = source
    while frontier:
        u = frontier.pop()
        for v,w in adjList[u]:
            if p[v] == -1 and parent[u] != v:
                p[v] = u
                frontier.append(v)
                if v == dest:
                    return True
    return False

# run Djikstra from Amsterdam to find all shortest paths to it in O(M log N) time complexity
# remove those edges on any shortest path
# perform a traversal algorithm from Delft to Amsterdam to see if Amsterdam is still reachable in O(M + N) time
n,m = map(int,stdin.readline().split())
adjList,edges = [[] for i in range(n)],[]
for i in range(m):
    u,v,w = map(int,stdin.readline().split())
    adjList[u].append((v,w))
    adjList[v].append((u,w))
    edges.append((u,v))
# parent[u] = v indicates that u precedes v on shortest path
parent = [-1 for i in range(n)]
# Amsterdam is represented by number 1
modifiedDjikstra(adjList,parent,n,1)
p = [-1 for i in range(n)]
if reachable(0,1,adjList,p,parent):
    path,c = [1],1
    while p[c] != c:
        c = p[c]
        path.append(c)
    ans = [len(path)]
    for i in range(len(path) - 1, -1, -1):
        ans.append(path[i])
    stdout.write(" ".join(str(num) for num in ans))
else:
    stdout.write("impossible\n")
