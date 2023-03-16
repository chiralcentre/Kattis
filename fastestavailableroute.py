from sys import stdin,stdout
from collections import deque

def possiblepositions(i,j,r,c,grid):
    movements = [(-1,0),(0,1),(1,0),(0,-1)]
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c) and (grid[i+x][j+y] == "." or grid[i + x][j + y] == "$")]

#perform BFS in O(hw) time
def solve(maze,r,c):
    visited = [[False for _ in range(c)] for j in range(r)]
    xs,ys,xe,ye = -1,-1,-1,-1
    for i in range(r):
        for j in range(c):
            if grid[i][j] == "@":
                xs,ys = i,j
            if grid[i][j] == "$":
                xe,ye = i,j
    frontier = deque([(xs,ys,0)]); visited[xs][ys] = True
    while frontier:
        i,j,m = frontier.popleft()
        for x,y in possiblepositions(i,j,r,c,maze):
            if x == xe and y == ye:
                return m + 1
            if not visited[x][y]:
                frontier.append((x,y,m + 1))
                visited[x][y] = True
    return -1 #unreachable

h,w,s = stdin.readline().split()
h,w = int(h),int(w)
grid = [stdin.readline().strip() for i in range(h)]
stdout.write(f"Your destination will arrive in {solve(grid,h,w)}")
for i in range(len(s) - 1): stdout.write("0")
stdout.write(" meters")
