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
        adjList[u].append((v,w))
    #Bellman Ford's algorithm is used with O(nm) time complexity
    INF = 2000000000 #use 1 billion to represent infinity
    D = [INF for _ in range(n)]; D[s] = 0
    for i in range(n-1): 
        for u,v,w in edgeList:
            if D[u] != INF and D[v] > D[u] + w: #need to check if D[u] is reachable since w can be negative
                D[v] = D[u] + w
    negativeCycle = [False for _ in range(n)]
    cycleDetected = True
    while cycleDetected: #O(nm)
        cycleDetected = False
        for u,v,w in edgeList: 
            if D[u] != INF and D[v] > D[u] + w and not negativeCycle[v]:
                D[v] = -INF #arbitrarily small number so future relaxation can occur
                cycleDetected = True
                negativeCycle[v] = True
    for i in range(q): #O(q)
        end = int(stdin.readline())
        stdout.write(f'Impossible\n') if D[end] == INF else stdout.write(f'-Infinity\n') if negativeCycle[end] else stdout.write(f'{D[end]}\n')
