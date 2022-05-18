from sys import stdin,stdout

K = int(stdin.readline())
adjList = [[] for _ in range(101)] #branch numbers are from 1 to 100
while True:
    a,*branches = map(int,stdin.readline().split())
    if a == -1:
        break
    for b in branches:
        adjList[b].append(a)
start = K; route = [K]
while adjList[start]: #while the root is not reached
    start = adjList[start][0] #only one outgoing edge from each vertex
    route.append(start)
stdout.write(' '.join(str(num) for num in route))
