from sys import stdin,stdout

def possiblepositions(i,j,r,c,grid):
    movements = [(-1,0),(0,1),(1,0),(0,-1)]
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c)]
#iterative DFS
def DFS(i,j,r,c,grid,visited):
    visited[i][j] = True
    frontier = [(i,j)]
    while frontier:
        a,b = frontier.pop()
        for x,y in possiblepositions(a,b,r,c,grid):
            if not visited[x][y] and (grid[x][y] == 'L' or grid[x][y] == 'C'):
                visited[x][y] = True
                frontier.append((x,y))

r,c = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for _ in range(r)]
islands,visited = 0,[[False for i in range(c)] for j in range(r)]
for i in range(r):
    for j in range(c):
        if grid[i][j] == 'L' and not visited[i][j]: #current cell unvisited
            islands += 1
            DFS(i,j,r,c,grid,visited)

stdout.write(f'{islands}\n')
