from sys import stdin

n,m = map(int,stdin.readline().split())
adjList,components = [[] for _ in range(n)],[-1 for _ in range(n)]
for _ in range(m):
    a,b = map(int,stdin.readline().split())
    adjList[a].append(b)
    adjList[b].append(a)

for i in range(n):
    if components[i] == -1:
        frontier = [i]
        components[i] = i
        while frontier:
            u = frontier.pop()
            for v in adjList[u]:
                if components[v] == -1:
                    components[v] = i
                    frontier.append(v)
print(" ".join(str(parent) for parent in components))
