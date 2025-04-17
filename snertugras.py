from sys import stdin,stdout

movements = [(-1,0),(0,1),(1,0),(0,-1)]
INF = pow(10,9)

def possiblepositions(i,j,r,c,grid):
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c) and grid[i+x][j+y] != "#"]

def findStart(grid,h,w):
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "S":
                return (i,j)
# code runs in O(hw) time
def solve(grid,h,w):
    x,y = findStart(grid,h,w)
    d = [[INF for i in range(w)] for j in range(h)]
    d[x][y] = 0
    frontier = [(x,y)]
    while frontier:
        new_frontier = []
        for i,j in frontier:
            for x,y in possiblepositions(i,j,h,w,grid):
                if d[x][y] > d[i][j] + 1:
                    d[x][y] = d[i][j] + 1
                    new_frontier.append((x,y))
                if grid[x][y] == "G":
                    return str(d[x][y])
        frontier = new_frontier
    return "thralatlega nettengdur"
    
h,w = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for _ in range(h)]
print(solve(grid,h,w))
