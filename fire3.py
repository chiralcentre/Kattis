from sys import stdin,stdout
from collections import deque

def possiblepositions(i,j,r,c,grid):
    movements = [(-1,0),(0,1),(1,0),(0,-1)]
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c) and grid[i+x][j+y] != '#']

def fire(r,c,grid):
    visited = [[False for j in range(c)] for i in range(r)]
    frontier_Joe,frontier_fire = deque([]),deque([])
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'J':
                if i == 0 or i == r - 1 or j == 0 or j == c - 1:
                    return '1' #only one move needed to move out of border
                visited[i][j] = True
                frontier_Joe.append(((i,j),0))
            elif grid[i][j] == 'F':
                visited[i][j] = True
                frontier_fire.append(((i,j),0))         
    while frontier_Joe: #BFS
        if len(frontier_fire) == 0: #fire is contained or no fire
            while frontier_Joe:
                position,counter = frontier_Joe.popleft()
                x,y = position
                for i,j in possiblepositions(x,y,r,c,grid):
                    if not visited[i][j]:
                        if i == 0 or i == r - 1 or j == 0 or j == c - 1:
                            return str(counter+2) # +2 since one move is needed to get the cell (i,j) and one more move needed to go out
                        visited[i][j] = True
                        frontier_Joe.append(((i,j),counter+1))
        else:    
            time = frontier_fire[0][1]
            while frontier_fire and frontier_fire[0][1] == time: #for every minute that passes
                firepos,counter = frontier_fire.popleft()
                x2,y2 = firepos
                for i,j in possiblepositions(x2,y2,r,c,grid):
                    if not visited[i][j]:
                        visited[i][j] = True
                        frontier_fire.append(((i,j),counter+1))
            while frontier_Joe and frontier_Joe[0][1] == time:
                position,counter2 = frontier_Joe.popleft()
                x,y = position
                for m,n in possiblepositions(x,y,r,c,grid):
                    if not visited[m][n]:
                        if m == 0 or m == r - 1 or n == 0 or n == c -1:
                            return str(counter2+2) # +2 since one move is needed to get the cell (i,j) and one more move needed to go out
                        visited[m][n] = True
                        frontier_Joe.append(((m,n),counter2+1))
    return 'IMPOSSIBLE'
            
        
r,c = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for _ in range(r)]
stdout.write(fire(r,c,grid)+'\n')

    
        

