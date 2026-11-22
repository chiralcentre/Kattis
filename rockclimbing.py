from sys import stdin

movements = [(-1,0),(0,1),(1,0),(0,-1)]
INF = pow(10,9)

def possiblepositions(i,j,r,c):
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c)]

# code runs in O(RC * 9RC) = O(R^2C^2) 
def is_feasible(grid,R,C,M,P):
    # best[i][j] represents the maximum energy with which Peter can be standing on (i,j)
    best = [[-INF for j in range(C)] for i in range(R + 2)]
    # seed starting cells with X or P
    frontier = []
    for i in range(C):
        best[R + 1][i] = min(M,P)
        frontier.append((R + 1,i))
    while frontier:
        a,b = frontier.pop()
        for x,y in possiblepositions(a,b,R + 2,C):
            e = min(best[a][b] - grid[x][y],P)
            if e >= 0 and e > best[x][y]:
                best[x][y] = e
                frontier.append((x,y))
    # if any top row cell has best >= 0
    return any(best[0][j] >= 0 for j in range(C))
    

R,C = map(int,stdin.readline().split())
stdin.readline() # ignore ending row
# pad grid with starting and ending row of zeroes
grid = [[0 for _ in range(C)]]
for _ in range(R):
    grid.append(list(map(int,stdin.readline().split())))
grid.append([0 for _ in range(C)])
# maixmum energy required to go through all cells is sum of positive cell values in grid
P = sum(grid[i][j] for i in range(R + 2) for j in range(C) if grid[i][j] > 0)
stdin.readline() # ignore starting row
# worst case is every cell in a column has 9
L,H,ans = 0,9 * R,None 
while L <= H:
    M = L + ((H - L) >> 1)
    if is_feasible(grid,R,C,M,P):
        ans = M
        H = M - 1
    else:
        L = M + 1
print(ans)
