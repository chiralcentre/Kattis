from sys import stdin,stdout
from heapq import heappop,heappush,heapify
#Approach:
#use Prim's to form a maximum spanning tree
#remove all streets incident to vertices on the maximin path from vertex 0 to vertex m - 1 in the maxST

n,m = map(int,stdin.readline().split())
adjList = [[] for _ in range(n)]
#i is road number
for i in range(m):
    u,v,w = map(int,stdin.readline().split())
    adjList[u].append((v,w,i))
    adjList[v].append((u,w,i))
#start from vertex 0, the train station
taken = [False for _ in range(n)]; taken[0] = True
#negate to convert into max heap
PQ = [(-w,v,0,r) for v,w,r in adjList[0]]; heapify(PQ)
parent,E = [(-1,-1) for _ in range(n)],0
#perform Prim's algorithm in O(m log m) time
while PQ:
    nw,u,p,r = heappop(PQ)
    if not taken[u]:
        taken[u] = True; parent[u] = (p,r); E += 1
        if E == n - 1: #full maxST is formed
            break
        for v,w,r in adjList[u]:
            if not taken[v]:
                heappush(PQ,(-w,v,u,r))
#maximinVertices stores the vertices on the maximin path from vertex 0 to vertex n - 1
#maximinPath stores the numbers of the streets on the maximin path from vertex 0 to vertex n - 1
#perform backtracking 
maximinVertices,maximinPath,start = {n-1},set(),n-1
while parent[start] != (-1,-1): #O(n) as there is maximum of n backtracking steps taken
    start,r = parent[start]
    maximinVertices.add(start)
    maximinPath.add(r)
#remove all streets incident to vertices on the maximin path from vertex 0 to vertex m - 1 in the maxST
blockedStreets = set() #set is used to prevent duplicates
for u in maximinVertices: #O(n + m)
    for v,w,r in adjList[u]:
        if r not in maximinPath: #can remove the street from usage
            blockedStreets.add(r)
#O(m log m) since there can be at most m - 1 blocked streets
stdout.write(' '.join(str(r) for r in sorted(blockedStreets))) if blockedStreets else stdout.write("none")


    
    
