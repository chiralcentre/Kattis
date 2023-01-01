from sys import stdin,stdout
from heapq import heappush,heappop,heapify
                    
n,m = map(int,stdin.readline().split())
#create m vertices to represent the power plants at the m possible locations
#the m vertices are connected to the respective locations for power plants, with the associated building cost
#run Prim's algorithm from the m vertices and ensure n edges are chosen in O((N + M) log (N + M)) = O(N log N)
adjList,frontier = [[] for _ in range(n+m)],[]
taken = [False for _ in range(n + m)]
for i in range(m):
    a,c = map(int,stdin.readline().split())
    a -= 1; frontier.append(i + n)
    adjList[a].append((n + i, c))
    adjList[n + i].append((a, c))
PL = list(map(int,stdin.readline().split()))
for i in range(n):
    adjList[i].append(((i + 1) % n, PL[i]))
    adjList[(i + 1) % n].append((i, PL[i]))
#multi source Prim's algorithm
cost,PQ,E = 0,[],0
for u in frontier:
    for v,w in adjList[u]:
        PQ.append((w,v))
        taken[u] = True
heapify(PQ)
while PQ and E < n:
    w,u = heappop(PQ)
    if not taken[u]:
        cost += w
        E += 1
        taken[u] = True
        for v,w2 in adjList[u]:
            if not taken[v]:
                heappush(PQ,(w2,v))
stdout.write(f"{cost}\n")
        
    

