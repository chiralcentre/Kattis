from sys import stdin,stdout
from collections import deque

for i in range(int(stdin.readline())):
    n,m = map(int,stdin.readline().split())
    labs = list(map(int,stdin.readline().split()))
    adjList,indeg1,indeg2 = [[] for _ in range(n)],[0 for _ in range(n)],[0 for _ in range(n)]
    #graph is acyclic, perform modified Kahn's algorithm in O(n+m) time
    for j in range(m):
        u,v = map(int,stdin.readline().split())
        u -= 1; v -= 1; #offset by 1 due to zero indexing
        adjList[u].append(v)
        indeg1[v] += 1; indeg2[v] += 1;
    shortest = n
    for start in range(1,3): #starting laboratory can be 1 or 2
        indeg = indeg1 if start == 1 else indeg2 #use a different indeg array for each starting laboratory    
        frontier = deque([])
        for j in range(n):
            if indeg[j] == 0:
                frontier.appendleft(j) if labs[j] == start else frontier.append(j) #perform conservation on drawings in the starting lab first
        currLab,moves = start,0
        while frontier:
            u = frontier.popleft()
            if labs[u] != currLab:
                moves += 1
                currLab = labs[u]
            for v in adjList[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    frontier.appendleft(v) if labs[v] == currLab else frontier.append(v) #perform conservation on drawings in lab same as current lab first to minimise number of moves
        if moves < shortest:
            shortest = moves
    stdout.write(f'{shortest}\n')
    
    
