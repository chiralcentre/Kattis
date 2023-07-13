from sys import stdin,stdout,setrecursionlimit

setrecursionlimit(pow(10,6))

#perform DFS topological sort
def DFSrec(u):
    global adjList,rToposort
    visited[u] = True
    for v in adjList[u]:
        if not visited[v]:
            DFSrec(v)
    rToposort.append(u)

#perform Kosaraju's algorithm to label every SCC
def kosaraju(n):
    global visited,rToposort,adjList,transpose
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            DFSrec(i)
    labels = [0 for _ in range(n)]; SCC = 0
    for i in range(len(rToposort) - 1, -1, -1):
        if labels[rToposort[i]] == 0:
            SCC += 1
            frontier = [rToposort[i]]
            labels[rToposort[i]] = SCC
            while frontier:
                u = frontier.pop()
                for v in transpose[u]:
                    if not labels[v]:
                        labels[v] = SCC
                        frontier.append(v)
    return labels,SCC

for _ in range(int(stdin.readline())):
    #run Kosaraju's algorithm to label all SCCs
    n,m = map(int,stdin.readline().split())
    adjList,transpose,rToposort,visited = [[] for i in range(n)],[[] for i in range(n)],[],[]
    for i in range(m):
        u,v = map(int,stdin.readline().split())
        u -= 1; v -= 1
        adjList[u].append(v)
        transpose[v].append(u)
    labels,SCC = kosaraju(n)
    #Consider each SCC as a new vertex, and link an edge between the new vertices according to original graph to get a new DAG
    #in the DAG, find number of vertices whose indegree is 0, denoted as X, and number of vertices with outdegree 0, denoted as Y
    #if DAG only has one vertice, answer = 0, else answer = max(X,Y)
    if SCC == 1:
        stdout.write("0\n")
    else:
        indeg,outdeg = [0 for i in range(SCC)],[0 for i in range(SCC)]
        #perform DFS to find indegree and outdegree of new graph
        for i in range(n):
            for v in adjList[i]:
                #offset by 1 due to zero indexing
                if labels[i] != labels[v]:
                    indeg[labels[i] - 1] += 1
                    outdeg[labels[v] - 1] += 1
        stdout.write(f"{max(sum(p == 0 for p in indeg),sum(p == 0 for p in outdeg))}\n")
    
