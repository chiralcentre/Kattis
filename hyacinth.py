from sys import stdin,stdout

class Node:
    def __init__(self,a=0,b=0):
        self.f1 = a
        self.f2 = b
        
def findleaf(deg):
    for i in range(len(deg)):
        if deg[i] == 1:
            return i
     
n = int(stdin.readline())
NIC,adjList,deg = [Node() for _ in range(n)],[[] for _ in range(n)],[0 for _ in range(n)]
for _ in range(n-1): #offset by 1 due to zero indexing
    i,j = map(int,stdin.readline().split())
    adjList[i-1].append(j-1)
    adjList[j-1].append(i-1)
    deg[j-1] += 1; deg[i-1] += 1
leaf = findleaf(deg) #O(n)

#start from leaf
frontier,visited = [leaf],[False for _ in range(n)]
visited[leaf] = True; NIC[leaf].f1 = 1; NIC[leaf].f2 = 2; #initialise starting vertex frequencies to 1 and 2
# number of unique frequencies = number of internal nodes + 1
counter = 2
while frontier: #do DFS
    u = frontier.pop()
    for key,v in enumerate(adjList[u]):
        if not visited[v]:
            visited[v] = True
            if deg[v] == 1: #v is a leaf, copy frequencies from parent
                NIC[v].f1, NIC[v].f2 = NIC[u].f1, NIC[u].f2
            else: 
                counter += 1
                NIC[v].f1 = NIC[u].f2
                NIC[v].f2 = counter
                frontier.append(v)
            
for i in range(n):
        stdout.write(f'{NIC[i].f1} {NIC[i].f2}\n')

