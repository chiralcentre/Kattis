from sys import stdin,stdout

# code runs in O(N + Q) time
N,D,Q = map(int,stdin.readline().split())
points = list(map(int,stdin.readline().split()))
adjList = [[] for _ in range(N + 1)]
for _ in range(N):
    u,v = map(lambda x: int(x) - 1,stdin.readline().split())
    adjList[u].append(v)
    adjList[v].append(u)
P = [None for _ in range(N + 1)]
# perform DFS from root of city centre to find sum of points from city centre to each building
frontier = [N]
P[N] = points[N]
while frontier:
    u = frontier.pop()
    for v in adjList[u]:
        if P[v] is None:
            P[v] = P[u] + points[v]
            frontier.append(v)
neighbours = [None for _ in range(N)]
for _ in range(Q):
    t = int(stdin.readline()) - 1
    if neighbours[t] is None:
        # there are at most 3 + 9 + 27 + 81 + 243 = 363 eligible candidates who will steal, since D is limited to 5 and each node has a maximum degree of 3
        # perform DFS again in O(1) time to find the neighbours
        frontier,steps,seen = [t],0,{t}
        while steps < D:
            new_frontier = []
            for u in frontier:
                for v in adjList[u]:
                    if v not in seen:
                        new_frontier.append(v)
                        seen.add(v)
            frontier = new_frontier
            steps += 1
        neighbours[t] = len(seen) - 1 # remove starting node
        if N in seen:
            neighbours[t] -= 1
    stdout.write(f"{P[t] - neighbours[t] * points[t]}\n")      
    
