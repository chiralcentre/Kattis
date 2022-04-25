from sys import stdin,stdout
from heapq import heappush,heappop

V,E,C,K,M = map(int,stdin.readline().split())
adjList = [[] for _ in range(V)]
for i in range(E):
    u,v,w = map(int,stdin.readline().split())
    u -= 1; v -= 1
    adjList[u].append((v,w))
    adjList[v].append((u,w))
# perform modified Djikstra in O(E log V) time
INF = 1000000000000 #use 1 trillion to represent infinity since maximum length is 20000*10000000 = 20 billion
D = [INF for _ in range(V)]; D[0] = 0 #start from clearing 1
PQ = [(0,0)]
while PQ:
    d,u = heappop(PQ)
    if d == D[u]:
        for v,w in adjList[u]:
            if D[v] > D[u] + w:
                D[v] = D[u] + w
                heappush(PQ,(D[v],v))
                
fruitClearings = list(map(lambda x: int(x) - 1,stdin.readline().split()))
reachableClearings = []
for f in fruitClearings: #O(C)
    if D[f] != INF: #filter out unreachable clearings
        reachableClearings.append(D[f])
reachableClearings.sort() #O(C log C)

#let B be the number of reachable clearings
#if B < M, this means there are not enough fruit to be plucked without regrowing the fruit
#if B < K, this means the first fruit taken will not regenerate in time to be plucked on day C + 1
#if B >= min(M,K), fruits are chosen in ascending order of distance from reachableClearings
if len(reachableClearings) < M and len(reachableClearings) < K:
    stdout.write('-1')
else: #multiply by 2 because of back journey
    stdout.write(f'{2*reachableClearings[min(M,K)-1]}') #offset by 1 due to zero indexing
