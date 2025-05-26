from sys import stdin

# DFS in O(RC) time
movements = [(-1,0),(0,1),(1,0),(0,-1)]
def possiblepositions(i,j,r,c,grid):
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c) and grid[i+x][j+y] == "#"]

def findStart(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                return (i,j)
    return (-1,-1)

R,C = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for _ in range(R)]
visited = [[False for i in range(C)] for j in range(R)]
sx,sy = findStart(grid)
visited[sx][sy] = True
frontier,area = [(sx,sy)],1
while frontier:
    i,j = frontier.pop()
    for x,y in possiblepositions(i,j,R,C,grid):
        if not visited[x][y]:
            visited[x][y] = True
            area += 1
            frontier.append((x,y))
print(area)
