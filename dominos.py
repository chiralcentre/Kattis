from sys import stdin,stdout,setrecursionlimit
# increase recursion limit since default recursion limit is 1000 and m can be at most 100000
setrecursionlimit(10**8)

def DFSrec(u,visited,adjacency_lst,toposort):
    visited[u] = True #avoid cycle
    for k in adjacency_lst[u]:
        if not visited[k]:
            DFSrec(k,visited,adjacency_lst,toposort)
    toposort.append(u)

 
for i in range(int(stdin.readline())):
    n,m = map(int,stdin.readline().split())
    tiles = [[] for _ in range(n)]
    for j in range(m):
        a,b = map(int,stdin.readline().split())
        tiles[a-1].append(b-1) #offset by 1 due to zero indexing
    #DFS topological sort
    visited,toposort = [False for _ in range(n)],[]
    for key in range(len(tiles)):
        if not visited[key]:
            DFSrec(key,visited,tiles,toposort)
    # iterate through toposort from right to left, since it is in reverse order
    # For each vertex in toposort, if it is not visited already, add 1 to the answer, and perform graph traversal from
    # that vertex, marking any vertices found during the traversal as visited
    counter,visited2 = 0,[False for _ in range(n)]
    for v in range(len(toposort)-1,-1,-1):
        if not visited2[toposort[v]]:
            counter += 1
            stack = [toposort[v]]
            while stack:
                vertice = stack.pop()
                for neighbour in tiles[vertice]:
                    if not visited2[neighbour]:
                        stack.append(neighbour)
                        visited2[neighbour] = True
    stdout.write(f'{counter}\n')
