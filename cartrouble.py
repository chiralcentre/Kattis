from sys import stdin,stdout

n = int(stdin.readline())
#since max street id is 999
adjList,adjListTranspose = [[] for _ in range(1000)],[[] for _ in range(1000)]
problems, usedIDs = [],[] #usedIDs stores the street ids used in order
for i in range(n):
    s,m,*reachable = map(int,stdin.readline().split())
    for v in reachable: #O(m)
        adjList[s].append(v)
        adjListTranspose[v].append(s)
    usedIDs.append(s)

#perform DFS on transposed graph to check which streets can reach surrounding circular riad system in O(n + E) time where E is the total number of edges
visited = [False for _ in range(1000)]; visited[0] = True
frontier = [0]
while frontier:
    u = frontier.pop()
    for v in adjListTranspose[u]:
        if not visited[v]:
            visited[v] = True
            frontier.append(v)
for ID in usedIDs: #O(n)
    if not visited[ID]:
        problems.append(f"TRAPPED {ID}")
#perform DFS on original graph from the surrounding circular road system to check which road systems are reachable in O(n + E) time
visited = [False for _ in range(1000)]; visited[0] = True
frontier = [0]
while frontier: 
    u = frontier.pop()
    for v in adjList[u]:
        if not visited[v]:
            visited[v] = True
            frontier.append(v)
for ID in usedIDs: #O(n)
    if not visited[ID]:
        problems.append(f"UNREACHABLE {ID}")
stdout.write("NO PROBLEMS") if not problems else stdout.write("\n".join(p for p in problems))
    
