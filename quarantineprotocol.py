from sys import stdin

movements = [(-1,0),(1,0)]
    
def possiblepositions(i,j,r,c,grid):
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c) and grid[i+x][j+y] != "#"]

n,m = map(int,stdin.readline().split())
grid = [list(stdin.readline().split()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if grid[i][j] == "X":
            frontier = [(i,j)]
            while frontier:
                x,y = frontier.pop()
                for u,v in possiblepositions(x,y,n,m,grid):
                    if grid[u][v] == "O":
                        frontier.append((u,v))
                        grid[u][v] = "X"
print(sum(grid[i][j] != "X" for i in range(n) for j in range(m)))
