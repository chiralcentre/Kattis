from sys import stdin,stdout
from collections import deque

def possiblepositions(i,j,r,c,grid):
    movements = {(-1,0):'D',(0,1):'L',(1,0):'U',(0,-1):'R'}
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c) and (grid[i+x][j+y] == '0' or grid[i+x][j+y] == movements[(x,y)])]

def start(R,C,grid):
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'S':
                return i,j
            
def atBorder(i,j,R,C):
    return True if i == 0 or i == R - 1 or j == 0 or j == C - 1 else False

def BFS(x,y,R,C,t,grid):
    if atBorder(x,y,R,C):
        return '0'
    visited = [[False for i in range(C)] for j in range(R)]
    visited[x][y] = True
    frontier = deque([(x,y,0)])
    while frontier:
        x1,y1,counter = frontier.popleft()
        if counter == t:
            return "NOT POSSIBLE"
        for a,b in possiblepositions(x1,y1,N,M,grid):
            if not visited[a][b]:
                if atBorder(a,b,R,C):
                    return str(counter + 1)
                visited[a][b] = True
                frontier.append((a,b,counter+1))
    return "NOT POSSIBLE" #no exit
                   
t,N,M = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for _ in range(N)]
x,y = start(N,M,grid)
stdout.write(BFS(x,y,N,M,t,grid)+'\n')
