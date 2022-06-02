from sys import stdin,stdout
from collections import deque

N = int(stdin.readline())
adjList = {}
for _ in range(N):
    u,*links = stdin.readline().split()
    if u not in adjList:
        adjList[u] = set() #set is used to avoid duplicates
    for v in links:
        if v not in adjList:
            adjList[v] = set()
        adjList[u].add(v);adjList[v].add(u)
        
s,e = stdin.readline().split()
#perform DFS from start to end in O(N**2) time since V = N and max E = N*(N-1)
p,visited = {},set()
frontier = [s]; visited.add(s)
while frontier:
    u = frontier.pop()
    if u in adjList:
        for v in adjList[u]:
            if v not in visited:
                visited.add(v)
                p[v] = u
                frontier.append(v)
            
if e not in visited:
    stdout.write("no route found")
else:
    route = deque([e]) # a deque is used for O(1) insertion to the left
    while e in p:
        route.appendleft(p[e])
        e = p[e]
    stdout.write(' '.join(station for station in route))
