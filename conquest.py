from sys import stdin,stdout
from heapq import heappop,heappush

def compress(w,u):
    return w * 200000 + u

def decompress(d):
    return d // 200000, d % 200000

def process(u):
    global taken,adjList,sizes
    taken[u] = True
    for v in adjList[u]:
        if not taken[v]:
            heappush(PQ,compress(sizes[v],v))
                
N,M = map(int,stdin.readline().split())
adjList = [[] for _ in range(N)]
for i in range(M):
    u,v = map(lambda x: int(x) - 1, stdin.readline().split())
    adjList[u].append(v)
    adjList[v].append(u)
sizes = [int(stdin.readline()) for _ in range(N)]
taken = [False for _ in range(N)]
PQ = []
process(0)
while PQ:
    s,u = decompress(heappop(PQ))
    if not taken[u]:
        if sizes[0] <= sizes[u]:
            break
        sizes[0] += sizes[u]
        sizes[u] = 0
        process(u)
stdout.write(f"{sizes[0]}\n")
