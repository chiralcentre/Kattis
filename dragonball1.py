from sys import stdin,stdout
from heapq import heappush,heappop
from itertools import permutations

def modifiedDjikstra(s,e,n,adjList):
    D = [INF for i in range(n)]
    D[s] = 0; PQ = [(0,s)]
    while PQ: 
        d,u = heappop(PQ)
        if u == e:
            return d #endpoint is reached
        if d == D[u]:
            for v,w in adjList[u]:
                if D[v] > D[u] + w:
                    D[v] = D[u] + w
                    heappush(PQ,(D[v],v))
    return D[e] #unreachable

def solve(n,db_cities,adjList):
    #sp[(a,b)] contains the length of the shortest path from a to b
    sp = {(0,0):0}
    #find shortest path between all cities containing dragon balls in O(m log n)
    #maximum number of pairs is 21
    for i in range(len(db_cities)):
        for j in range(i+1,len(db_cities)):
            s,e = db_cities[i],db_cities[j]
            sp[(s,e)] = sp[(e,s)] = modifiedDjikstra(s,e,n,adjList)
            if sp[(s,e)] == INF:
                return "-1"
    #find shortest path between city 0 and all cities containing dragon balls in O(m log n)
    #maximum of 7 iterations
    for city in db_cities:
        if city != 0:
            sp[(0,city)] = modifiedDjikstra(0,city,n,adjList)
    #go through the maximum 8! = 40320 permutations
    shortest = INF
    for combination in permutations(db_cities):
        cost = sp[(0,combination[0])]
        for i in range(len(combination)-1):
            cost += sp[(combination[i],combination[i+1])]
        if cost < shortest:
            shortest = cost   
    return str(shortest)

INF = 10**12 # use 1 trillion to represent infinity
n,m = map(int,stdin.readline().split())
adjList = [[] for _ in range(n)]
for i in range(m):
    u,v,w = map(int,stdin.readline().split())
    u -= 1; v -= 1; #offset by 1 due to zero indexing
    adjList[u].append((v,w))
    adjList[v].append((u,w))
#get list of unique cities
db_cities = set(map(lambda x: int(x) - 1,stdin.readline().split()))
db_cities = list(db_cities)
stdout.write(solve(n,db_cities,adjList))


