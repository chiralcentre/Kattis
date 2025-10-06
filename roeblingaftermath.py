from sys import stdin


movements = [(-1,0),(0,1),(1,0),(0,-1),
             (-1,-1),(-1,1),(1,-1),(1,1)]

def possiblepositions(i,j,r,c,grid):
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c) and grid[i+x][j+y] != "X"]

def find_chicken(grid,m,n):
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "C":
                return (i,j)
    raise Exception("no chicken found")

def find_road_column(grid):
    for i in range(len(grid[0])):
        if grid[0][i] == "R":
            return i
    raise Exception("no road found")

def solve():
    m,n = map(int,stdin.readline().split())
    grid = [list(stdin.readline().split()) for _ in range(m)]
    road_col = find_road_column(grid)
    cx,cy = find_chicken(grid,m,n)
    frontier = [(cx,cy)]
    visited = [[False for i in range(n)] for j in range(m)]
    visited[cx][cy] = True
    while frontier:
        x,y = frontier.pop()
        for a,b in possiblepositions(x,y,m,n,grid):
            if not visited[a][b]:
                frontier.append((a,b))
                visited[a][b] = True
            if b > road_col:
                return "yes"
    return "no"

if __name__ == "__main__":
    print(solve())
