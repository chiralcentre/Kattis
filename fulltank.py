from sys import stdin,stdout
from heapq import heappush,heappop

def modifiedDjikstra(c,s,e,n):
    if s == e:
        return "0" #no fuel required
    INF = 1000000000 #use 1 billion to represent infinity
    P = [[INF for i in range(c+1)] for j in range(n)] # P[a][b] represents the lowest price of reaching city a with fuel level b
    P[s][0] = 0; PQ = [(0,s,0)]
    lowest = INF
    while PQ:
        cost,u,f = heappop(PQ)
        if u == e: #end city is reached and lowest cost is attained
            return str(cost)
        if cost == P[u][f]:
            #refueling 1 unit of fuel at u
            if f < c and P[u][f+1] > cost + fuelPrices[u]:
                P[u][f+1] = cost + fuelPrices[u]
                heappush(PQ,(P[u][f+1],u,f+1))
            for v,d in adjList[u]:
                if f >= d and P[v][f-d] > P[u][f]: #if fuel >= distance, no additional cost required
                    P[v][f-d] = P[u][f]
                    heappush(PQ,(P[v][f-d],v,f-d))
    return "impossible" 

#number of vertices = n, number of edges = m
n,m = map(int,stdin.readline().split())
fuelPrices = list(map(int,stdin.readline().split()))
adjList = [[] for _ in range(n)]
for i in range(m):
    u,v,w = map(int,stdin.readline().split())
    adjList[u].append((v,w))
    adjList[v].append((u,w))

# modified Djikstra's is run for each query in O(m log m) time and q queries are run
# total time complexity is O(qm log m)
for _ in range(int(stdin.readline())):
    c,s,e = map(int,stdin.readline().split())
    stdout.write(modifiedDjikstra(c,s,e,n)+'\n')
    
    
