from sys import stdin,stdout
from heapq import heappush,heappop

first = True
while True:
    n,m,q,s = map(int,stdin.readline().split())
    if n == m == q == s == 0:
        break
    if first:
        first = False
    else:
        stdout.write(f'\n') #print new line between test cases
    adjList = [[] for _ in range(n)]
    for i in range(m):
        u,v,w = map(int,stdin.readline().split())
        adjList[u].append((v,w))
    INF = 1000000000 #use 1 billion to represent infinity
    D = [INF for _ in range(n)]; D[s] = 0
    PQ = []; heappush(PQ,(0,s))
    while PQ: #modified Djikstra's is used with O(m log m) time complexity
        d,u = heappop(PQ)
        if d == D[u]: # check if this is the superior copy
            for v,w in adjList[u]:
                if D[v] > D[u] + w: # can relax
                    D[v] = D[u] + w
                    heappush(PQ,(D[v],v))
    for i in range(q): #O(q)
        end = int(stdin.readline())
        stdout.write(f'Impossible\n') if D[end] == INF else stdout.write(f'{D[end]}\n')
