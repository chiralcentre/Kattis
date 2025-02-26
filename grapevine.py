from sys import stdin

n,m,d = map(int,stdin.readline().split())
skepticism = [0 for _ in range(n)]
mappings = {}
for i in range(n):
    s,t = stdin.readline().split()
    mappings[s] = i
    skepticism[i] = int(t)

adjList = [[] for _ in range(n)]
for i in range(m):
    a,b = stdin.readline().split()
    u,v = mappings[a],mappings[b]
    adjList[u].append(v)
    adjList[v].append(u)

# perform BFS at a depth of d, O(n + m)
s = mappings[stdin.readline().strip()]
frontier,visited = [s],[False for _ in range(n)]
visited[s] = True
for i in range(d):
    temp = []
    for u in frontier:
        for v in adjList[u]:
            if skepticism[v] > 0:
                skepticism[v] -= 1
                if skepticism[v] == 0:
                    temp.append(v)
            visited[v] = True
    frontier = temp
print(sum(visited[i] for i in range(n)) - 1)
    
