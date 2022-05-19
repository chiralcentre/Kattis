from sys import stdin,stdout
from heapq import heappush,heappop

def modifiedDjikstra(n,s,t,adjList):
    INF = 1000000000000 #use 1 trillion to represent infinity
    #C[a][b] represents the smallest cost to reach city a using b flights
    C = [[INF for i in range(2)] for j in range(n)] 
    C[s][0] = 0; PQ = [(0,s,0)]
    while PQ:
        c,u,a = heappop(PQ)
        if u == t: #end city is reached, terminate early
            return str(c)
        if c == C[u][a]:
            for v,w in adjList[u]:
                if w > 0 and C[v][a] > c + w:
                    C[v][a] = c + w
                    heappush(PQ,(C[v][a],v,a))
                elif w == 0 and a == 0 and C[v][a+1] > c: #free flight only possible if a == 0
                    C[v][a+1] = c
                    heappush(PQ,(C[v][a+1],v,a+1))            

n,m,f,s,t = map(int,stdin.readline().split())
adjList = [[] for _ in range(n)]
for i in range(m):
    a,b,c = map(int,stdin.readline().split())
    adjList[a].append((b,c))
    adjList[b].append((a,c))
for i in range(f): #flight is free and directed from a to b
    a,b = map(int,stdin.readline().split())
    adjList[a].append((b,0))
#modified Djikstra is performed in O(2m log 2m) time.
stdout.write(modifiedDjikstra(n,s,t,adjList))
