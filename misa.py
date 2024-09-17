from sys import stdin

movements = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def getNeighbours(i,j,grid):
    return sum(grid[i + x][j + y] == "o"  for x,y in movements if i + x in range(R) and j + y in range(S))

R,S = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for _ in range(R)]
ans = sum(getNeighbours(i,j,grid) for i in range(R) for j in range(S) if grid[i][j] == "o")
ans >>= 1
best = 0
for i in range(R):
    for j in range(S):
        if grid[i][j] == ".":
            best = max(getNeighbours(i,j,grid),best)
print(ans + best)
            
