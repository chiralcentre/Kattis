from sys import stdin,stdout

#cannot pass through other entrances as well
def possiblepositions(i,j,r,c,grid):
    movements = [(-1,0),(0,1),(1,0),(0,-1)]
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c) and not grid[i+x][j+y].isalpha()]

def count_dots(grid,n,m):
    dots = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == ".":
                dots += 1
    return dots

def find_entrances(grid,n,m):
    return [(i,j) for i in range(n) for j in range(m) if grid[i][j].isalpha() and grid[i][j] != "X"]

n,m = map(int,stdin.readline().split())
maze = [stdin.readline().strip() for _ in range(n)]
total = count_dots(maze,n,m)
entrances = find_entrances(maze,n,m)

visited = [[False for _ in range(m)] for j in range(n)]
reachable,needed = 0,0
for a,b in entrances:
    frontier = [(a,b)]; visited[a][b] = True
    required = False 
    while frontier:
        u,v = frontier.pop()
        for x,y in possiblepositions(u,v,n,m,maze):
            if not visited[x][y]:
                visited[x][y] = True
                frontier.append((x,y))
                if maze[x][y] == ".":
                    reachable += 1
                    required = True
    if required:
        needed += 1
        
stdout.write(f"{needed} {total - reachable}\n")
