from sys import stdin
from collections import deque

movements = [(-1,0),(0,1),(1,0),(0,-1)]
    
def possiblepositions(i,j,r,c,grid):
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c) and grid[i+x][j+y] != "#"]

def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "*":
                return (i,j)
    raise Exception("not supposed to happen")

def solve():
    # 0-1 BFS in O(WH) time
    INF = pow(10,9)
    W,H = map(int,stdin.readline().split())
    grid = [stdin.readline().strip() for _ in range(H)]
    D = [[INF for j in range(W)] for i in range(H)]
    sx,sy = find_start(grid)
    D[sx][sy] = 0
    frontier = deque([(sx,sy)])
    while frontier:
        a,b = frontier.popleft()
        for x,y in possiblepositions(a,b,H,W,grid):
            w = int(grid[x][y] == "D")
            if D[a][b] + w < D[x][y]:
                D[x][y] = D[a][b] + w
                if w == 1:
                    frontier.append((x,y))
                else:
                    frontier.appendleft((x,y))
            if grid[x][y] == "E":
                return str(D[x][y])
    return "NOT POSSIBLE"

print(solve())
