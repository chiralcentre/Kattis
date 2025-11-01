from sys import stdin,stdout

movements = [(-1,0),(0,1),(1,0),(0,-1),
             (-1,-1),(-1,1),(1,-1),(1,1)]
INF = pow(10,9)

def possiblepositions(i,j,r,c,grid):
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c)]

# code runs in O(V + E) = O(mn + 8mn) = O(mn)
def solve(n,m,grid,sx,sy,ex,ey):
    D = [[[INF for k in range(2)] for i in range(m)] for j in range(n)]
    frontier = []
    for x,y in possiblepositions(sx,sy,n,m,grid):
        if grid[x][y] == grid[sx][sy]: # equal altitude invalid
            continue
        c = int(grid[x][y] > grid[sx][sy])
        frontier.append((x,y,c))
        D[x][y][c] = 1
    while frontier:
        new_frontier = []
        for a,b,c in frontier:
            for x,y in possiblepositions(a,b,n,m,grid):
                if grid[x][y] == grid[a][b]:
                    continue
                res = int(grid[x][y] > grid[a][b])
                if res + c == 1 and D[x][y][res] > D[a][b][c] + 1:
                    D[x][y][res] = D[a][b][c] + 1
                    new_frontier.append((x,y,res))
                    if (x,y) == (ex,ey):
                        return D[x][y][res]
        frontier = new_frontier
    return -1

n,m = map(int,stdin.readline().split())
grid = [list(map(int,stdin.readline().split())) for _ in range(n)]
sx,sy,ex,ey = map(lambda x: int(x) - 1,stdin.readline().split())
print(solve(n,m,grid,sx,sy,ex,ey))
