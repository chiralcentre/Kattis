from sys import stdin

movements = [(-1,0),(0,1),(1,0),(0,-1)]

INF = pow(10,9)

def possiblepositions(i,j,r,c,d,grid):
    positions = []
    # move straight
    mx,my = movements[d]
    if i + mx in range(r) and j + my in range(c) and grid[i + mx][j + my] != "X":
        positions.append((i + mx, j + my, d))
    # right turn
    nd = (d + 1) % 4
    mx,my = movements[nd]
    if i + mx in range(r) and j + my in range(c) and grid[i + mx][j + my] != "X":
        positions.append((i + mx, j + my, nd))
    return positions

# 0,1,2,3 -> N,E,S,W
def solve(n,m,grid,sx,sy,ex,ey):
    D = [[[INF for k in range(4)] for i in range(m)] for j in range(n)]
    frontier = []
    for i in range(3):
        D[sx][sy][i] = 0
        frontier.append((sx,sy,i))
    while frontier:
        new_frontier = []
        for a,b,c in frontier:
            for x,y,d in possiblepositions(a,b,n,m,c,grid):
                if D[x][y][d] > D[a][b][c] + 1:
                    D[x][y][d] = D[a][b][c] + 1
                    new_frontier.append((x,y,d))
                    if (x,y) == (ex,ey):
                        return D[x][y][d]
        frontier = new_frontier
    return -1

w,h = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for _ in range(h)]
sx,sy,ex,ey = -1,-1,-1,-1
for i in range(h):
    for j in range(w):
        if grid[i][j] == "A":
            sx,sy = i,j
        elif grid[i][j] == "B":
            ex,ey = i,j
print(solve(h,w,grid,sx,sy,ex,ey))
