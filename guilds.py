from sys import stdin,stdout
from collections import deque

#keep track of indegree of each node
adjList,indeg,small_guilds = {},{},[]
for _ in range(int(stdin.readline())):
    v,u = stdin.readline().split()
    if u not in adjList:
        adjList[u] = [v]
        indeg[u] = 0
    else:
        adjList[u].append(v)
    if v not in adjList:
        adjList[v] = []
        indeg[v] = 0
    small_guilds.append(v)
    indeg[v] += 1
    
#perform DFS from nodes with zero indegree in O(E + V) = O(n)
toplevel = {}; visited = {key: False for key in adjList}
Q = []
for key,value in indeg.items():
    if value == 0:
        visited[key] = True
        Q.append(key)
for a in Q:
    frontier = [a]
    while frontier:
        u = frontier.pop()
        for v in adjList[u]:
            if not visited[v]:
                visited[v] = True
                frontier.append(v)
                toplevel[v] = a
for guild in small_guilds:
    stdout.write(f"{guild} {toplevel[guild]}\n")
