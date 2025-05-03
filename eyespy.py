from sys import stdin,stdout
from collections import deque

movements = [(-1,0),(0,1),(1,0),(0,-1)]

def possiblepositions(i,j,r,c,grid):
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c) and grid[i+x][j+y] != "#"]

#it is assumed the map always has a player
def findPlayer(grid,H,W):
    for i in range(H):
        for j in range(W):
            if grid[i][j] == "P":
                return (i,j)
                     
def solve(grid,H,W):
    i,j = findPlayer(grid,H,W)
    visited = [[None for _ in range(W)] for l in range(H)]
    frontier = deque([(i,j)]); visited[i][j] = (i,j)
    gold = 0
    while frontier:
        x1,y1 = frontier.pop()
        if grid[x1][y1] == 'G':
            gold += 1
        for x,y in possiblepositions(x1,y1,H,W,grid):
            if visited[x][y] == None:
                frontier.append((x,y))
                visited[x][y] = (x1,y1)
            if grid[x][y] == "A": # found
                x2,y2 = x1,y1
                while visited[x2][y2] != (x2,y2):
                    grid[x2][y2] = "X"
                    x2,y2 = visited[x2][y2]
                return "\n".join("".join(row) for row in grid)   
    return "call for help"


R,C = map(int,stdin.readline().split())
grid = [list(stdin.readline().strip()) for _ in range(R)]
stdout.write(f"{solve(grid,R,C)}\n")

