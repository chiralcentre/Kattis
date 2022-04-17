from sys import stdin,stdout
from collections import deque
    
n,m = map(int,stdin.readline().split())
adjList,indeg = [[] for _ in range(n)],[0 for _ in range(n)]
for i in range(m):
    a,b = map(int,stdin.readline().split())
    a -= 1; b -= 1; #offset by 1 due to zero indexing
    adjList[a].append(b)
    indeg[b] += 1


#Kahn's algorithm is run to provide toposort with O(n+m) time complexity
frontier,toposort = deque([i for i in range(n) if indeg[i] == 0]),[]
while frontier:
    u = frontier.popleft()
    toposort.append(u)
    for v in adjList[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            frontier.append(v)
            
#no cycles if length of toposort = n
stdout.write('\n'.join(str(num+1) for num in toposort)) if len(toposort) == n else stdout.write(f'Impossible\n')
