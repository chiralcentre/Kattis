from sys import stdin,stdout

def possiblepositions(i,j,r,c,grid):
    movements = [(-1,0),(0,1),(1,0),(0,-1)]
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c) and grid[i+x][j+y] != '#']

def fire(r,c,grid):
    visited = [[False for j in range(c)] for i in range(r)]
    frontier_self,frontier_fire = [],[]
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '@':
                if i == 0 or i == r - 1 or j == 0 or j == c - 1:
                    return '1' #only one move needed to move out of border
                visited[i][j] = True
                frontier_self.append((i,j))
            elif grid[i][j] == '*':
                visited[i][j] = True
                frontier_fire.append((i,j))
    time = 0
    while frontier_self: #BFS
        time += 1
        new_frontier_self,new_frontier_fire = [],[] # go level by level
        for x2,y2 in frontier_fire:
            for i,j in possiblepositions(x2,y2,r,c,grid):
                if not visited[i][j]:
                    visited[i][j] = True
                    new_frontier_fire.append((i,j))
        for x,y in frontier_self:
            for m,n in possiblepositions(x,y,r,c,grid):
                if not visited[m][n]:
                    if m == 0 or m == r - 1 or n == 0 or n == c -1:
                        return str(time+1) # +1 since one more move needed to go out
                    visited[m][n] = True
                    new_frontier_self.append((m,n))
        frontier_self,frontier_fire = new_frontier_self,new_frontier_fire
    return 'IMPOSSIBLE'

for _ in range(int(stdin.readline())):  
    w,h = map(int,stdin.readline().split())
    grid = [stdin.readline().strip() for _ in range(h)]
    stdout.write(fire(h,w,grid)+'\n')
