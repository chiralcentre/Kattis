from sys import stdin

movements = [(-1,0),(0,1),(1,0),(0,-1),
             (1,1),(1,-1),(-1,-1),(-1,1)]

def possiblepositions(i,j,r,c,grid):
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c) and grid[i+x][j+y] == "#"]

#iterative DFS
def DFS(i,j,r,c,visited,grid,components,CC):
    visited[i][j] = True
    components[i][j] = CC
    frontier = [(i,j)]
    while frontier:
        a,b = frontier.pop()
        for x,y in possiblepositions(a,b,r,c,grid):
            if not visited[x][y]:
                visited[x][y] = True; components[x][y] = CC; #labelling components
                frontier.append((x,y))

r,c = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for _ in range(r)]
visited,components = [[False for i in range(c)] for j in range(r)],[[0 for i in range(c)] for j in range(r)]
CC = 0
for i in range(r): #total time complexity is O(9RC) = O(RC)
    for j in range(c):
        if grid[i][j] == "#" and not visited[i][j]: #perform DFS
            CC += 1
            DFS(i,j,r,c,visited,grid,components,CC)
print(CC)
