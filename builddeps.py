from sys import stdin,stdout,setrecursionlimit
# increase recursion limit 
setrecursionlimit(10**7)

def DFSrec(u,visited,adjacency_lst,reversedToposort):
    visited[u] = True #avoid cycle
    for k in adjacency_lst[u]:
        if not visited[k]:
            DFSrec(k,visited,adjacency_lst,reversedToposort)
    reversedToposort.append(u)

n = int(stdin.readline())
files,filesIndex,counter = {},{},0
adjList = [[] for _ in range(n)]
for _ in range(n):
    f,rest = stdin.readline().split(":")
    if f not in files:
        files[f] = counter
        filesIndex[counter] = f
        counter += 1
    a = files[f]
    for f2 in rest.strip().split():
        if f2 not in files:
            files[f2] = counter
            filesIndex[counter] = f2
            counter += 1
        b = files[f2]
        adjList[b].append(a)
        
start = files[stdin.readline().strip()]
#graph is acyclic, do DFS toposort from start
visited,reversedToposort = [False for _ in range(n)],[]
DFSrec(start,visited,adjList,reversedToposort)
#print out order of recompilation such that all dependencies are satisfied           
for i in range(len(reversedToposort)-1,-1,-1):
    stdout.write(f'{filesIndex[reversedToposort[i]]}\n')
