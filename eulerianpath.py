from sys import stdin,stdout

def hierholzer(s,AL,N):
    ans,idx,st = [],[0 for _ in range(N)],[s]
    while st:
        u = st[-1]
        if idx[u] < len(AL[u]):
            st.append(AL[u][idx[u]])
            idx[u] += 1
        else:
            ans.append(u)
            st.pop()
    return ans[::-1]

# check if every vertex has the same number of incoming edges and outgoing edges, or if exactly one vertex has one extra outgoing edge and exactly one vertex has one extra incoming edge
# also check if graph is connected
# returns starting point for eulerian path, if it exists
def eulerian_path_check(indeg,outdeg,undirAL,n):
    nonzero_vertices,s,t,extra_in,extra_out = 0,-1,-1,0,0
    for i in range(n):
        if indeg[i] == outdeg[i] and indeg[i]:
            nonzero_vertices += 1
            t = i
        elif indeg[i] == outdeg[i] + 1:
            if extra_in == 1: # one vertex with indeg - outdeg = 1 has already been found
                return -1
            extra_in = 1
        elif outdeg[i] == indeg[i] + 1:
            if extra_out == 1: # one vertex with outdeg - indeg = 1 has already been found
                return -1
            extra_out = 1
            s = i #starting vertex should be vertex with extra outgoing edge, if it exists
        elif indeg[i] != outdeg[i]:
            return -1
    if s == -1:
        s = t # start at a random vertex with equal indegree and outdegree if there is no vertex with extra outgoing edge
    # check if all vertices with nonzero degree are connected in underlying undirected graph
    frontier,visited = [s],[False for _ in range(n)]
    visited[s],seen = True,1
    while frontier:
        u = frontier.pop()
        for v in undirAL[u]:
            if not visited[v]:
                visited[v] = True
                seen += 1
                frontier.append(v)
    return s if seen == nonzero_vertices + extra_in + extra_out else -1
    
while True:
    n,m = map(int,stdin.readline().split())
    if n == m == 0:
        break
    indeg,outdeg = [0 for i in range(n)],[0 for i in range(n)]
    adjList,undirAL = [[] for i in range(n)],[[] for i in range(n)]
    for i in range(m):
        u,v = map(int,stdin.readline().split())
        adjList[u].append(v)
        undirAL[u].append(v)
        undirAL[v].append(u)
        indeg[v] += 1
        outdeg[u] += 1
    res = eulerian_path_check(indeg,outdeg,undirAL,n)
    if res != -1:
        stdout.write(" ".join(str(elem) for elem in hierholzer(res,adjList,n)))
        stdout.write("\n")
    else:
        stdout.write("Impossible\n")
