from sys import stdin

movements = [(-1,0),(0,1),(1,0),(0,-1)]

def possiblepositions(i,j,r,c):
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c)]

def is_possible(r,c,sx,sy,ex,ey,du,dd,grid):
    visited = [[False for i in range(c)] for j in range(r)]
    visited[sx][sy] = True
    frontier = [(sx,sy)]
    while frontier:
        x,y = frontier.pop()
        if (x,y) == (ex,ey):
            return True
        for nx,ny in possiblepositions(x,y,r,c):
            if visited[nx][ny]:
                continue
            if (grid[nx][ny] >= grid[x][y] and grid[nx][ny] - grid[x][y] <= du) or (grid[x][y] >= grid[nx][ny] and grid[x][y] - grid[nx][ny] <= dd):
                frontier.append((nx,ny))
                visited[nx][ny] = True
    return False

    
du,dd = map(int,stdin.readline().split())
r,c = map(int,stdin.readline().split())
grid = [list(map(int,stdin.readline().split())) for _ in range(r)]
ex,ey = map(lambda x: int(x) - 1,stdin.readline().split()) # offset by 1 for zero indexing
res = is_possible(r,c,0,0,ex,ey,du,dd,grid) and is_possible(r,c,ex,ey,0,0,du,dd,grid)
print("Kvoldinu er bjargad!") if res else print("Nu er Eyleifur i bobba!")
