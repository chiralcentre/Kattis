from sys import stdin,stdout
from collections import deque

def BFS(coins,S,e): #O(mS)
    frontier = deque([])
    visited = [[False for i in range(S)] for j in range(S)]
    for a,b in coins:
        if a**2 + b**2 < e and not visited[a][b]:
            visited[a][b] = True
            frontier.append((a,b,1))
        elif a**2 + b**2 == e:
            return "1" #only one coin is needed
    while frontier:
        a,b,c = frontier.popleft()
        for x,y in coins:
            if (a+x)**2 + (b+y)**2 < e and not visited[a+x][b+y]:
                visited[a+x][b+y] = True
                frontier.append((a+x,b+y,c+1))
            elif (a+x)**2 + (b+y)**2 == e:
                return str(c+1)
    return "not possible"
    
for i in range(int(stdin.readline())): #O(nmS)
    if i > 0: stdin.readline() #read in blank line between test cases
    m,S = map(int,stdin.readline().split()); e = S**2
    coins = [tuple(map(int,stdin.readline().split())) for _ in range(m)]
    stdout.write(BFS(coins,S,e)+'\n')
    
