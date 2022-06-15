from sys import stdin,stdout
from heapq import heappush,heappop
from math import ceil

INF  = 1000000000 #use 1 billion to represent infinity
def modifiedDjikstra(n,s,adjList):
    T = [INF for _ in range(n)]; T[s] = 0 #it takes 0 time units to reach starting node from starting node
    PQ = [(0,s)]
    while PQ:
        t,u = heappop(PQ)
        if t == T[u]:
            for v,t0,P,d in adjList[u]:
                if P != 0:
                    k = max(0,ceil((t-t0)/P))
                    nearestTime = t0 + k*P
                    if T[v] > nearestTime + d:
                        T[v] = nearestTime + d
                        heappush(PQ,(T[v],v))
                elif P == 0 and t <= t0:
                    if T[v] > t0 + d:
                        T[v] = t0 + d
                        heappush(PQ,(T[v],v))
    return T

first = True             
while True:
    n,m,q,s = map(int,stdin.readline().split())
    if n == m == q == s == 0:
        break
    if first:
        first = False
    else:
        stdout.write("\n") #print new line between consecutive test cases
    adjList = [[] for _ in range(n)]
    for i in range(m):
        u,v,t0,P,d = map(int,stdin.readline().split())
        adjList[u].append((v,t0,P,d))
    T = modifiedDjikstra(n,s,adjList)
    for j in range(q):
        e = int(stdin.readline())
        stdout.write(str(T[e])+'\n') if T[e] != INF else stdout.write("Impossible\n")
    
