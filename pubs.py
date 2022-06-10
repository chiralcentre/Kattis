from sys import stdin,stdout
from collections import deque

n,m = map(int,stdin.readline().split())
adjList = [[] for _ in range(n)]
for i in range(m):
    x,y = map(int,stdin.readline().split())
    x -= 1; y -= 1; #offset by 1 due to zero indexing
    adjList[x].append(y); adjList[y].append(x)
#0 is unvisited, 1 is for building a pub and 2 is for building a house
layout = [0 for _ in range(n)]
isolated = False
for j in range(n): #O(n + m)
    #BFS from source j. Sites of odd distance get pubs, sites of even distance get houses.
    if not layout[j]:
        if not adjList[j]: # if there is an isolated node, it is not possible to have any arrangement
            isolated = True
            break
        frontier = deque([(j,0)]); layout[j] = 2
        while frontier:
            u,d = frontier.popleft()
            for v in adjList[u]:
                if not layout[v]:
                    frontier.append((v,d+1))
                    layout[v] = 2 - (d+1)%2

if isolated:
    stdout.write("Impossible")
else:
    stdout.write(' '.join("pub" if layout[i] == 1 else "house" for i in range(n)))
            
