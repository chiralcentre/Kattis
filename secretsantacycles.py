from sys import stdin,stdout

#treat graph as undirected, and count number of components, C
#number of assignments within each component = sum(indeg[i] - 1 for i in lst if indeg[i] > 1)
def DFS(s,visited,components,adjList):
    visited[s] = True
    lst,frontier = [s],[s]
    while frontier:
        u = frontier.pop()
        for v in adjList[u]:
            if not visited[v]:
                visited[v] = True
                lst.append(v)
                frontier.append(v)
    components.append(lst)

N = int(stdin.readline())
#adjList[i] contains the node that i is pointing towards
adjList,UDadjList,indeg = [-1 for _ in range(N)],[[] for _ in range(N)],[0 for _ in range(N)]
for i in range(N):
    a = int(stdin.readline()) - 1
    adjList[i] = a; indeg[a] += 1
    UDadjList[i].append(a); UDadjList[a].append(i)
#count number of components in O(N) time
components,visited = [],[False for _ in range(N)]
for i in range(N):
    if not visited[i]:
        DFS(i,visited,components,UDadjList)
assignments = 0
for lst in components:
    counter = sum(indeg[i] - 1 for i in lst if indeg[i] > 1)
    # add to assignments by minimum of 1 if there are at least two components
    assignments += max(counter,1) if len(components) > 1 else counter
stdout.write(f"{assignments}\n") 
