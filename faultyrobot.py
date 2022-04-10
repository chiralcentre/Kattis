from sys import stdin,stdout
from collections import deque

n,m = map(int,stdin.readline().split())
buggyMoves,forcedMoves = [[] for _ in range(n)],[[] for _ in range(n)]
for i in range(m):
    a,b = map(int,stdin.readline().split())
    if a > 0:
        buggyMoves[a-1].append(b-1)
    else:
        forcedMoves[-a-1].append(b-1)
        
restNodes = 0
#start from node 1, right attribute keeps track of whether a buggy move has been made along the path
frontier,visited = deque([(0,False)]),[False for _ in range(n)] 
visited[0] = True
while frontier: #BFS
    u,buggy =  frontier.popleft()
    if len(forcedMoves[u]) == 0: #no forced moves
        restNodes += 1
    for v in forcedMoves[u]: #there is maximum of one forced edge per vertex
        if not visited[v]:
            visited[v] = True
            frontier.append((v,buggy))
    if not buggy: # possible to make one buggy move
        for w in buggyMoves[u]:
            if not visited[w]:
                visited[w] = True
                frontier.append((w,True))
stdout.write(f"{restNodes}\n")
