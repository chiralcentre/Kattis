from sys import stdin,stdout
from collections import deque

def BFS(edges,start,E):
    found = [False for _ in range(E)]
    frontier = deque([start])
    found[start] = True; nodes = 0
    while frontier:
        vertex = frontier.popleft()
        for neighbour in edges[vertex]:
            if not found[neighbour]:
                frontier.append(neighbour)
                found[neighbour] = True
                nodes += 1
    return nodes
    
A,B,E,P = map(int,stdin.readline().split())
predecessors,successors = [0 for _ in range(E)],[0 for _ in range(E)]
inEdges,outEdges = [[] for _ in range(E)],[[] for _ in range(E)]
for i in range(P):
    u,v = map(int,stdin.readline().split())
    inEdges[v].append(u); outEdges[u].append(v)
#O(E(E+P)) -  Do BFS for every vertex to find number of predecessors and successors for each node
for j in range(E):
    predecessors[j] = BFS(inEdges,j,E)
    successors[j] = BFS(outEdges,j,E)
# Let N be number of promotions
# Node x has no possibility of being promoted if number of predecessors >= N
# Node y will certainly be promoted if number of successors >= E - N
firstAnswer,secondAnswer,thirdAnswer = 0,0,0
for k in range(E): #O(E)
    if successors[k] >= E - A:
        firstAnswer += 1
    if successors[k] >= E - B:
        secondAnswer += 1
    if predecessors[k] >= B:
        thirdAnswer += 1
stdout.write(f'{firstAnswer}\n')
stdout.write(f'{secondAnswer}\n')
stdout.write(f'{thirdAnswer}\n')
    
