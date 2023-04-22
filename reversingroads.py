from sys import stdin,stdout

adjList,edgeList,rToposort,visited = [],[],[],[]

#perform DFS topological sort
def DFSrec(u):
    visited[u] = True
    for v in adjList[u]:
        if not visited[v]:
            DFSrec(v)
    rToposort.append(u)

#perform Kosaraju's algorithm for every edge reversed in O(n(m + n)) time
def kosaraju(adjList,transpose,m):
    global visited
    visited = [False for _ in range(m)]
    for i in range(m):
        if not visited[i]:
            DFSrec(i)
    #count number of SCCs, and check if it is equal to 1
    visited = [False for _ in range(m)]; SCC = 0
    for i in range(len(rToposort) - 1, -1, -1):
        if not visited[rToposort[i]]:
            SCC += 1
            frontier = [rToposort[i]]
            visited[rToposort[i]] = True
            while frontier:
                u = frontier.pop()
                for v in transpose[u]:
                    if not visited[v]:
                        visited[v] = True
                        frontier.append(v)
    return SCC

def solve(adjList,edgeList,transpose,m):
    if kosaraju(adjList,transpose,m) == 1:
        return "valid"
    else:
        for u,v in edgeList:
            adjList[u].remove(v)
            adjList[v].append(u)
            transpose[v].remove(u)
            transpose[u].append(v)
            if kosaraju(adjList,transpose,m) == 1:
                return f"{u} {v}"
            #undo changes in O(1) time
            adjList[u].append(v)
            adjList[v].pop()
            transpose[v].append(u)
            transpose[u].pop()
        return "invalid"
    
c = 1
while True:
    try:
        m,n = map(int,stdin.readline().split())
    except:
        break
    adjList = [[] for _ in range(m)]
    transpose = [[] for _ in range(m)]
    edgeList = []
    for _ in range(n):
        u,v = map(int,stdin.readline().split())
        adjList[u].append(v)
        transpose[v].append(u)
        edgeList.append((u,v))
    stdout.write(f"Case {c}: {solve(adjList,edgeList,transpose,m)}\n")
    c += 1
