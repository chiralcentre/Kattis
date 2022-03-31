from sys import stdin,stdout

N,M = map(int,stdin.readline().split())
adjList,notConnected = [[] for _ in range(N)],{num for num in range(N)}
for i in range(M): #O(M)
    a,b = map(int,stdin.readline().split())
    adjList[a-1].append(b-1)
    adjList[b-1].append(a-1)
#start from house 1; -1 due to zero indexing
frontier,visited = [0],[False for _ in range(N)]
visited[0] = True; notConnected.remove(0)
while frontier: #perform DFS with O(N+M) time complexity
    house = frontier.pop()
    for neighbour in adjList[house]:
        if not visited[neighbour]:
            visited[neighbour] = True
            frontier.append(neighbour)
            notConnected.remove(neighbour)
# elements in set are already in order
stdout.write("Connected\n") if len(notConnected) == 0 else stdout.write('\n'.join(str(h+1) for h in notConnected))
