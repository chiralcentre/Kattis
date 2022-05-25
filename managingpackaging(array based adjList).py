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
    files,filesIndex,counter = {},{},0
    adjList,indeg = [[] for _ in range(n)],[0 for _ in range(n)]
    for i in range(n):
        f,*deps = stdin.readline().split()
        if f not in files:
            files[f] = counter
            filesIndex[counter] = f
            counter += 1
        a = files[f]
        for f2 in deps:
            if f2 not in files:
                files[f2] = counter
                filesIndex[counter] = f2
                counter += 1
            b = files[f2]
            adjList[b].append(a) #a directed edge from b to a exists, since a is dependent on b
            indeg[a] += 1
    #Create a min heap and insert all vertices with indegree 0 in O(n) time
    #A min heap is used to ensure the lexicographically smallest vertex is picked every time
    PQ = [filesIndex[i] for i in range(n) if indeg[i] == 0]; heapify(PQ)
    toposort = []; V = 0
    while PQ: #O(n log n + E) where E is the number of edges
        u = heappop(PQ)
        toposort.append(u)
        for v in adjList[files[u]]:
            indeg[v] -= 1
            if indeg[v] == 0:
                heappush(PQ,filesIndex[v])
        V += 1
    # cycle exists if V != n
    if V != n:
        stdout.write("cannot be ordered\n")
    else:
        stdout.write("\n".join(package for package in toposort) + "\n")
