from sys import stdin,stdout
from heapq import heappush,heappop,heapify

INF = pow(10,9)
N,M,X,Y = map(int,stdin.readline().split())
X -= 1; Y -= 1 # offset by 1 for zero indexing
adjList = [[] for _ in range(N)]
for _ in range(M):
    a,b,w,c = map(int,stdin.readline().split())
    a -= 1; b -= 1
    adjList[a].append((b,w,c))
    adjList[b].append((a,w,c))

D = [(INF,INF,INF) for _ in range(N)]
D[X] = (0,0,0)
#perform Djikstra but modify the tuple stored into priority queue as (t,s,d,v)
PQ = []; heappush(PQ,(0,0,0,X))
while PQ:
    t,s,d,u = heappop(PQ)
    if u == Y:
        break
    if (t,s,d) == D[u]:
        for v,w,c in adjList[u]:
            t2,s2 = t,s
            if c == 2: t2 += 1
            elif c == 1: s2 += 1
            if D[v] > (t2,s2,d + w):
                D[v] = (t2,s2,d + w)
                heappush(PQ,(t2,s2,d + w,v))
                
#check if location is reachable
stdout.write("IMPOSSIBLE\n") if D[Y] == (INF,INF,INF) else stdout.write(f"{D[Y][2]} {D[Y][1]} {D[Y][0]}\n")
