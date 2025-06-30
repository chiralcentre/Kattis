from sys import stdin,setrecursionlimit

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

#run Kosaraju's algorithm to label all SCCs
n,m = map(int,stdin.readline().split())
adjList,transpose,rToposort,visited = [[] for i in range(n)],[[] for i in range(n)],[],[]
edge_list = []
for i in range(m):
    u,v = map(int,stdin.readline().split())
    u -= 1; v -= 1
    # if there is an exit to be closed from room a, there is an edge from b to a
    adjList[v].append(u)
    transpose[u].append(v)
    edge_list.append((v,u))
labels,SCC = kosaraju(n)
#Consider each SCC as a new vertex, and link an edge between the new vertices according to original graph to get a new DAG
#Use a linear pass to count SCCs with no outgoing edges
if SCC == 1:
    # minimum 1 exit needed
    print(1)
else:
    outdeg = [0 for i in range(SCC)]
    for u,v in edge_list:
        if labels[u] != labels[v]:
            # outdeg[i] here exceeds the true outdegree in new graph due to duplicates
            outdeg[labels[u]] += 1 
    print(sum(1 for deg in outdeg if deg == 0))
