from sys import stdin,stdout

#graph is a DAG which passes through every node
n,m = map(int,stdin.readline().split())
satisfaction = list(map(int,stdin.readline().split()))
adjList = [[] for _ in range(n)]; maximum = [-1 for _ in range(n)]
for i in range(m):
    s,t = map(int,stdin.readline().split())
    adjList[s].append(t)
    
#perform DFS from source 0 in O(N + M) time
frontier = [0]; visited = [False for _ in range(n)]
while frontier:
    u = frontier.pop()
    if maximum[u] == -1:
        if visited[u]: #node has been visited, but it has not been processed yet
            maximum[u] = satisfaction[u]
            for v in adjList[u]:
                maximum[u] = max(maximum[u],maximum[v]) #skip pizza stand u and go to pizza stand v
                maximum[u] = max(maximum[u],maximum[v]/2 + satisfaction[u]) #eat pizza at u and move on to c
        else: #the node has not been visited yet
            visited[u] = True
            frontier.append(u)
            for v in adjList[u]:
                if maximum[v] == -1: #add the children of the node if they have not been processed yet
                    frontier.append(v)
stdout.write(str(maximum[0]))
