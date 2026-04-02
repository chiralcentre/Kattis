from sys import stdin
from heapq import heappush,heappop

INF = pow(10,9)
movements = [(-1,0),(0,1),(1,0),(0,-1)]

def possiblepositions(i,j,r,c,grid):
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c) and grid[i+x][j+y] != "#"]

def modifiedDjikstra(n,m,sx,sy,ex,ey,grid):
    #D[a][b][c] represents the smallest time to reach block (a,b) using c shortcuts
    D = [[[INF for k in range(2)] for i in range(m)] for j in range(n)] 
    D[sx][sy][0] = 0; PQ = [(0,sx,sy,0)]
    while PQ:
        d,x,y,j = heappop(PQ)
        if x == ex and y == ey: #end block is reached, terminate early
            return d
        if d == D[x][y][j]:
            for nx,ny in possiblepositions(x,y,n,m,grid):
                w = 0 if grid[x][y] == "S" else int(grid[x][y])
                if j == 0 and D[nx][ny][j + 1] > D[x][y][j] + 1:
                    D[nx][ny][j + 1] = D[x][y][j] + 1
                    heappush(PQ,(D[nx][ny][j + 1],nx,ny,j + 1))
                if D[nx][ny][j] > D[x][y][j] + w:
                    D[nx][ny][j] = D[x][y][j] + w
                    heappush(PQ,(D[nx][ny][j],nx,ny,j))
    return -1

n,m = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for _ in range(n)]
sx,sy,ex,ey = -1,-1,-1,-1
for i in range(n):
    for j in range(m):
        if grid[i][j] == "S":
            sx,sy = i,j
        elif grid[i][j] == "E":
            ex,ey = i,j
print(modifiedDjikstra(n,m,sx,sy,ex,ey,grid))
