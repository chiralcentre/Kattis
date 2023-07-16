from sys import stdin,stdout
from math import log2

#use logarithms to avoid overflow errors since number can very quickly go above upper bound of 2 * 10^9
def fulfillsReqs(m,adjList,required):
    flow = [0 for _ in range(len(adjList))]
    flow[0] = log2(m) #start at root
    frontier = [0]
    while frontier:
        u = frontier.pop()
        for v,x,t in adjList[u]:
            if flow[v] == 0:
                frontier.append(v)
                f = flow[u] + log2(x) - log2(100)
                #always square the flow if flow > 1 -> f > 0
                if f > 0 and t == 1:
                    f *= 2
                flow[v] = f
    for i in range(len(adjList)):
        if required[i] != -1 and log2(required[i]) > flow[i]:
            return False
    return True


#total complexity as O(100N)
N = int(stdin.readline())
adjList = [[] for _ in range(N)]
for i in range(N - 1):
    a,b,x,t = map(int,stdin.readline().split())
    a -= 1; b -= 1;
    adjList[a].append((b,x,t))
    adjList[b].append((a,x,t))
required = list(map(float,stdin.readline().split()))
s,e,ans = 0,2 * pow(10,9),-1
#run 100 iterations of binary search
for i in range(100):
    m = (s + e) / 2
    if fulfillsReqs(m,adjList,required):
        e,ans = m,m
    else:
        s = m
stdout.write(f"{ans}\n")
