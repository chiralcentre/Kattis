from sys import stdin,stdout
from heapq import heappush,heappop,heapify

for _ in range(int(stdin.readline())):                   
    N,M,L,S = map(int,stdin.readline().split())
    frontier = list(map(lambda x: int(x) - 1,stdin.readline().split()))
    #run Prim's algorithm from the S stations and ensure n - S edges are chosen in O(M log N)
    #answer =  cost of N - S edges + (N - S) * L
    adjList,taken = [[] for _ in range(N)],[False for _ in range(N)]
    for i in range(M):
        u,v,w = map(int,stdin.readline().split())
        u -= 1; v -= 1
        adjList[u].append((v,w))
        adjList[v].append((u,w))
    #multi source Prim's algorithm
    cost,PQ,E = 0,[],0
    for u in frontier:
        for v,w in adjList[u]:
            PQ.append((w,v))
            taken[u] = True
    heapify(PQ)
    while PQ and E < N - S:
        w,u = heappop(PQ)
        if not taken[u]:
            cost += w
            E += 1
            taken[u] = True
            for v,w2 in adjList[u]:
                if not taken[v]:
                    heappush(PQ,(w2,v))
    stdout.write(f"{cost + (N - S) * L}\n")
