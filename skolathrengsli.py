from sys import stdin,stdout

# reverse edges, BFS from destination in O(n + m) time
INF  = pow(10,9)
n,m = map(int,stdin.readline().split())
e = int(stdin.readline()) - 1 # classroom number
adjList = [[] for _ in range(n)]
for _ in range(m):
    u,v = map(lambda x: int(x) - 1,stdin.readline().split())
    adjList[v].append(u) # reverse edges
D = [INF for _ in range(n)]
D[e] = 0
frontier = [e]
while frontier:
    new_frontier = []
    for u in frontier:
        for v in adjList[u]:
            if D[v] > D[u] + 1:
                D[v] = D[u] + 1
                new_frontier.append(v)
    frontier = new_frontier
for _ in range(int(stdin.readline())):
    x = int(stdin.readline()) - 1
    stdout.write(f"{'O nei!' if D[x] == INF else D[x]}\n")  
