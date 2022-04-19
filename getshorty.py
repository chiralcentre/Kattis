from sys import stdin,stdout
from heapq import heappush,heappop

while True:
    n,m = map(int,stdin.readline().split())
    if n == m == 0:
        break
    adjList,size = [[] for _ in range(n)],[0 for _ in range(n)]
    for i in range(m):
        a,b,f = stdin.readline().split()
        a = int(a); b = int(b); f = float(f)
        adjList[a].append((b,f))
        adjList[b].append((a,f))
    #modified Djikstra's is used starting from intersection 0 and a max heap is used
    size[0] = -1; PQ = [(-1,0)]
    while PQ: #O(m log m)
        s,u = heappop(PQ)
        if s == size[u]:
            for v,f in adjList[u]:
                if size[v] > size[u]*f:
                    size[v] = size[u]*f
                    heappush(PQ,(size[v],v))
    stdout.write("{:.4f}".format(-size[n-1])+'\n')
