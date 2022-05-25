from sys import stdin,stdout
from heapq import heappush,heappop,heapify

first = True
while True:
    n = int(stdin.readline())
    if n == 0:
        break
    if first:
        first = False
    else:
        stdout.write("\n") #print out new line
    # a hash table is used instead of an array since the files are strings
    adjList,indeg = {},{}
    for i in range(n):
        a,*deps = stdin.readline().split()
        if a not in adjList:
            adjList[a] = []
            indeg[a] = 0
        for b in deps:
            if b not in adjList:
                adjList[b] = []
                indeg[b] = 0
            adjList[b].append(a) #a directed edge from b to a exists, since a is dependent on b
            indeg[a] += 1
    #Create a min heap and insert all vertices with indegree 0 in O(n) time
    #A min heap is used to ensure the lexicographically smallest vertex is picked every time
    PQ = [key for key,value in indeg.items() if value == 0]; heapify(PQ)
    toposort = []; V = 0
    while PQ: #O(n log n + E) where E is the number of edges
        u = heappop(PQ)
        toposort.append(u)
        for v in adjList[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                heappush(PQ,v)
        V += 1
    # cycle exists if V != n
    if V != n:
        stdout.write("cannot be ordered\n")
    else:
        stdout.write("\n".join(package for package in toposort) + "\n")
        
    
    
