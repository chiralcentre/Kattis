from sys import stdin
from heapq import heappush,heappop

INF = 1000000000 #use 1 billion to represent infinity
def modifiedDjikstra(adjList,N,s,e):
    D = [INF for _ in range(N)]; D[s] = 0
    P = [-1 for _ in range(N)]
    PQ = []; heappush(PQ,(0,s))
    while PQ: #modified Djikstra's is used with O(M log M) time complexity
        d,u = heappop(PQ)
        if u == e:
            return d,P
        if d == D[u]: # check if this is the superior copy
            for v,w in adjList[u]:
                if D[v] > D[u] + w: # can relax
                    P[v] = u
                    D[v] = D[u] + w
                    heappush(PQ,(D[v],v))
    return -1,P

a = int(stdin.readline())
u,v = stdin.readline().strip(),stdin.readline().strip()
m,rm,adjList = [u,v],{u: 0, v: 1},[[] for _ in range(2)]
for _ in range(a):
    x,y,z = stdin.readline().split()
    if x not in rm:
        rm[x] = len(m)
        m.append(x)
        adjList.append([])
    if y not in rm:
        rm[y] = len(m)
        m.append(y)
        adjList.append([])
    adjList[rm[x]].append((rm[y],int(z)))
d,P = modifiedDjikstra(adjList,len(adjList),0,1)
total,curr = 0,1
while P[curr] != -1:
    total += 1
    curr = P[curr]
print(total - 1)

