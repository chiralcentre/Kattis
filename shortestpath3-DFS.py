from sys import stdin,stdout

first = True
while True:
    n,m,q,s = map(int,stdin.readline().split())
    if n == m == q == s == 0:
        break
    if first:
        first = False
    else:
        stdout.write(f'\n') #print new line between test cases
    edgeList,adjList = [],[[] for _ in range(n)]
    for i in range(m):
        u,v,w = map(int,stdin.readline().split())
        edgeList.append((u,v,w))
        adjList[u].append(v)
    #Bellman Ford's algorithm is used with O(nm) time complexity
    INF = 1000000000 #use 1 billion to represent infinity
    D = [INF for _ in range(n)]; D[s] = 0
    for i in range(n-1): 
        for u,v,w in edgeList:
            if D[u] != INF and D[v] > D[u] + w:
                D[v] = D[u] + w
    #one pass Bellman Ford's to check for negative weight cycles
    negativeCycle,frontier = [False for _ in range(n)],[]
    for u,v,w in edgeList: 
        if D[u] != INF and D[v] > D[u] + w and not negativeCycle[v]:
            negativeCycle[v] = True
            frontier.append(v)
    while frontier: #DFS with O(n+m) time complexity
        u = frontier.pop()
        for v in adjList[u]:
            if not negativeCycle[v]:
                negativeCycle[v] = True
                frontier.append(v)
    for i in range(q): #O(q)
        end = int(stdin.readline())
        stdout.write(f'Impossible\n') if D[end] == INF else stdout.write(f'-Infinity\n') if negativeCycle[end] else stdout.write(f'{D[end]}\n')
