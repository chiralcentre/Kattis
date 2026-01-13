from sys import stdin,stdout

movements = [(-1,0),(0,1),(1,0),(0,-1)]

def possiblepositions(i,j,r,c,grid):
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c)]

# x is column, y is row
c,r,y,x = map(int,stdin.readline().split())
grid = [stdin.readline().split() for _ in range(r)]
frontier = [(x,y)]
visited = [[False for j in range(c)] for i in range(r)]
visited[x][y] = True
while frontier:
    a,b = frontier.pop()
    for u,v in possiblepositions(a,b,r,c,grid):
        if grid[u][v] == grid[x][y] and not visited[u][v]:
            frontier.append((u,v))
            visited[u][v] = True
for a in range(r):
    for b in range(c):
        if visited[a][b]:
            stdout.write(f"{b} {a}\n")
