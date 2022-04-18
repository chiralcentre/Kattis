from sys import stdin,stdout
from heapq import heappush,heappop
from math import sqrt

def distance(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)

def time(u,v,points):
    x1,y1 = points[u]; x2,y2 = points[v]
    D = distance(x1,y1,x2,y2)
    # check if starting point is a cannon 
    return min(2 + abs((D-50)/5),D/5) if 1 <= u <= n else D/5
        
start = tuple(map(float,stdin.readline().split())); end = tuple(map(float,stdin.readline().split()))
INF = 100000000 #use 1 billion to represent infinity
n = int(stdin.readline())
points = [start]
for _ in range(n):
    points.append(tuple(map(float,stdin.readline().split()))) # cannons are found in 1 to n index
points.append(end)
T = [INF for _ in range(n+2)] #keeps track of time array
T[0] = 0; PQ = []; heappush(PQ,(0,0)) #modified Djikstra is used
while PQ:
    t,u = heappop(PQ)
    if t == T[u]: #important check due to lazy DS
        for v in range(n+2):
            if v != u:
                w = time(u,v,points)
                if T[v] > T[u] + w:
                    T[v] = T[u] + w
                    heappush(PQ,(T[v],v))
stdout.write(f'{T[n+1]}\n')
                



