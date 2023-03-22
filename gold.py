from sys import stdin,stdout

def possiblepositions(i,j,r,c,grid):
    movements = [(-1,0),(0,1),(1,0),(0,-1)]
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c) and grid[i+x][j+y] != "#"]

#it is assumed the map always has a player
def findPlayer(grid,H,W):
    for i in range(H):
        for j in range(W):
            if grid[i][j] == "P":
                return (i,j)
                     
def solve(grid,H,W):
    i,j = findPlayer(grid,H,W)
    visited = [[False for _ in range(W)] for l in range(H)]
    frontier = [(i,j)]; visited[i][j] = True
    gold = 0
    while frontier:
        x1,y1 = frontier.pop()
        if grid[x1][y1] == 'G':
            gold += 1
        pospn = possiblepositions(x1,y1,H,W,grid)
        trapped = False
        # What is the purpose of the following three lines of code?
        for x2,y2 in pospn:
            if grid[x2][y2] == 'T':
                trapped = True
        if not trapped:
            for x2,y2 in pospn:
                if not visited[x2][y2] and grid[x2][y2] != "T":
                    frontier.append((x2,y2))
                    visited[x2][y2] = True
    return gold


W,H = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for _ in range(H)]
stdout.write(f"{solve(grid,H,W)}\n")
