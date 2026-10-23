from sys import stdin

N,M = map(int,stdin.readline().split())
W,V = list(map(int,stdin.readline().split())),list(map(int,stdin.readline().split()))
adjList = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(lambda x: int(x) - 1, stdin.readline().split())
    adjList[a].append(b)
    adjList[b].append(a)
# components[a] = list of members in component a
# perform component labelling in O(V + E) = O(N + M) time
components,visited = [],[False for _ in range(N)]
for i in range(N):
    if not visited[i]:
        visited[i] = True
        members,frontier = [i],[i]
        while frontier:
            u = frontier.pop()
            for v in adjList[u]:
                if not visited[v]:
                    visited[v] = True
                    members.append(v)
                    frontier.append(v)
        components.append(members)
# within each connected component, greedily assign largest value to largest weight
# code runs in O(N log N) time
total = 0
for comp in components:
    w = sorted([W[i] for i in comp],reverse = True)
    v = sorted([V[i] for i in comp],reverse = True)
    for j in range(len(comp)):
        total += w[j] * v[j]
print(total)
