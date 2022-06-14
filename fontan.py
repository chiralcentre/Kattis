from sys import stdin,stdout
from collections import deque

N,M = map(int,stdin.readline().split())
grid = [list(stdin.readline().strip()) for _ in range(N)]
frontier = deque([])
for i in range(N):
    for j in range(M):
        if grid[i][j] == "V":
            frontier.append((i,j))

#perform BFS from all water locations
while frontier:
    i,j = frontier.popleft()
    if i+1 in range(N): #cell directly below the water cell exists
        if grid[i+1][j] == ".": #air cell directly below water cell
            grid[i+1][j] = "V"
            frontier.append((i+1,j))
        if grid[i+1][j] == "#": #stone cell directly below water cell
            movements = [(0,-1),(0,1)] #move directly left or right
            for x,y in movements:
                if j + y in range(M) and grid[i][j+y] == ".":
                    grid[i][j+y] = "V"
                    frontier.append((i,j+y))
stdout.write('\n'.join(''.join(char for char in row) for row in grid))
            
