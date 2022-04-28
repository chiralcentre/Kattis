from sys import stdin,stdout
from collections import deque

def BFS(N,adjList):
    #Perform BFS from source node 1. Bob will take shortest path from node 0 to node N - 1
    #Maximum number of color changes = number of edges on shortest path - 1
    visited,frontier = [False for _ in range(N)],deque([(0,0)]) #right attribute contains number of edges traversed so far
    visited[0] = True
    while frontier:
        u,e = frontier.popleft()
        for v in adjList[u]:
            if not visited[v]:
                if v == N - 1:
                    return str(e)
                visited[v] = True
                frontier.append((v,e+1))
    
N,M = map(int,stdin.readline().split())
adjList = [[] for _ in range(N)]
for i in range(M):
    a,b = map(int,stdin.readline().split())
    a -= 1; b -= 1 #offset by 1 due to zero indexing
    adjList[a].append(b)
    adjList[b].append(a)

stdout.write(BFS(N,adjList))
