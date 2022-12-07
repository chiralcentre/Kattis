from sys import stdin,stdout,setrecursionlimit
#increase recursion limit to prevent stack overflow
setrecursionlimit(10**6)

#p is parent of current node
#condition v != p prevents visiting the same vertex again
def DFS(u,p):
    nodeInSubtree = u in nodes
    for v,w in adjList[u]:
        if v != p and DFS(v,u):
            global total
            total += w
            nodeInSubtree = True
    return nodeInSubtree
    
N,K = map(int,stdin.readline().split())
adjList = [[] for _ in range(N)]
for i in range(N - 1):
    u,v,w = map(int,stdin.readline().split())
    adjList[u].append((v,w))
    adjList[v].append((u,w))
#perform DFS from root, and keep track of total distance travelled in O(N) time   
nodes = set(map(int,stdin.readline().split()))
total = 0
DFS(0,-1)
#multiply by 2 because of return trip
stdout.write(f"{total * 2}")


