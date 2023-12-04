from sys import stdin,stdout

def solve(curr, lit):
    global memo,subAdjList,lamps
    # a represents number of lamps placed, and starts with 1 since we assume lamp is placed at curr
    # b and c start off at 0 since we assume lamps are not placed at curr
    a,b,c = 1,0,0
    if memo[curr][lit] != -1:
        return memo[curr][lit]
    for v in subAdjList[curr]:
        a += solve(v, 1) # choose to place lamp on neighbour
    ans = a
    # if current vertex is already lit or another vertex on the opposite endpoint of current vertex is lit
    if lit == 1:
        for v in subAdjList[curr]:
            b += solve(v, 0) # next vertex does not need to be lit
        ans = min(ans,b)
    # lamp is already placed
    if lamps[curr]:
        for v in subAdjList[curr]:
            c += solve(v, 1)
        ans = min(ans,c)
    memo[curr][lit] = ans
    return ans

N,S = map(int,stdin.readline().split())
adjList = [[] for _ in range(N)]
for i in range(N-1):
    u,v,d = map(int,stdin.readline().split())
    u -= 1; v -= 1 #offset by 1 due to zero indexing
    adjList[u].append((v,d))
    adjList[v].append((u,d))

lamps = [False for _ in range(N)]
L = int(stdin.readline())
existing = list(map(int,stdin.readline().split()))
for i in range(L):
    lamps[existing[i]-1] = True

visited,frontier = [False for _ in range(N)],[(0,0)]
visited[0],subAdjList = True,[[] for _ in range(N)]
while frontier:
    u,d1 = frontier.pop()
    if 2*d1 < S: #need to start and end at university campus
        for v,d2 in adjList[u]:
            if not visited[v]:
                visited[v] = True
                subAdjList[u].append(v)
                frontier.append((v,d1+d2))
                
# keep track of vertices adjacent to trail that a jogger may use
pos = [v for v in range(N) if visited[v]]
# find minimum vertex cover of subtree
memo = [[-1 for i in range(2)] for j in range(N)]
stdout.write(f"{min(solve(0,1),solve(0,0))}\n")
