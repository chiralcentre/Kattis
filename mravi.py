from sys import stdin,stdout

def fulfillsReqs(m,adjList,required):
    flow = [0 for _ in range(len(adjList))]
    flow[0] = m #start at root
    frontier = [0]
    while frontier:
        u = frontier.pop()
        for v,x,t in adjList[u]:
            if flow[v] == 0:
                frontier.append(v)
                f = flow[u] * x / 100
                #always square the flow if flow > 1
                if f > 1 and t == 1:
                    f *= f
                flow[v] = f
    for i in range(len(adjList)):
        if required[i] != -1 and required[i] > flow[i]:
            return False
    return True

#total complexity as O(log_2(2 * 10^9) * N)
N = int(stdin.readline())
adjList = [[] for _ in range(N)]
for i in range(N - 1):
    a,b,x,t = map(int,stdin.readline().split())
    a -= 1; b -= 1;
    adjList[a].append((b,x,t))
    adjList[b].append((a,x,t))
required = list(map(int,stdin.readline().split()))
s,e,ans = 0,2 * pow(10,9),-1
while abs(s - e) > 0.00001:
    m = (s + e) / 2
    if fulfillsReqs(m,adjList,required):
        e,ans = m,m
    else:
        s = m
stdout.write(f"{ans}\n")
