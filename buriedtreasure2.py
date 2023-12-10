from sys import stdin,stdout,setrecursionlimit

setrecursionlimit(1000000)

#assume visited,rToposort,adjList,transpose arrays are constructed already

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

def check_satisfiability(labels,m):
    for i in range(0, m << 1, 2):
        if labels[i] == labels[i + 1]:
            return "NO"
    return "YES"

def negate(v):
    return v - 1 if v % 2 else v + 1

# source: https://en.wikipedia.org/wiki/2-satisfiability
# given problem is a 2 SAT problem
# create a vertex for every literal and NOT literal
# There are two literals (denoted as x and y) in each treasure map, at least one of which needs to be satisfied (x OR y)
# x OR y is equivalent to (NOT x -> y) AND (NOT y -> x) in implication form
# an edge in the directed graph exists for every implication
# to check if implication graph is satisfiable, find all SCCs using Kosaraju's algorithm
# check if x and NOT x are in the same SCC for all literals in the implication graph

n,m = map(int,stdin.readline().split())
# vertex i and vertex i + 1 represents literal and NOT literal for every location for i in range(0,2n,2)
adjList,transpose = [[] for i in range(2 * m)],[[] for i in range(2 * m)] 
for i in range(n):
    u,v = map(int,stdin.readline().split())
    a = (u - 1) << 1 if u > 0 else((abs(u) - 1) << 1) + 1
    b = (v - 1) << 1 if v > 0 else((abs(v) - 1) << 1) + 1
    adjList[negate(a)].append(b)
    adjList[negate(b)].append(a)
    transpose[b].append((negate(a)))
    transpose[a].append((negate(b)))
    
visited,rToposort = [],[]
labels,SCC = kosaraju(m << 1)
stdout.write(f"{check_satisfiability(labels,m)}\n")
