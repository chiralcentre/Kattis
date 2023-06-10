from sys import stdin,stdout

def possiblepositions(i,j,r,c,grid):
    movements = [(-1,0),(0,1),(1,0),(0,-1)]
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c) and grid[i+x][j+y] == grid[i][j]] #last condition checks for same component
#iterative DFS
def DFS(i,j,r,c,visited,grid,components,CC):
    visited[i][j] = True; components[i][j] = CC;
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
for i in range(r): #total time complexity is O(5RC) = O(RC)
    for j in range(c):
        if not visited[i][j]: #perform DFS
            CC += 1
            DFS(i,j,r,c,visited,grid,components,CC)

for i in range(int(stdin.readline())): #each query can be answered in O(1) time
    x1,y1,x2,y2 = map(lambda x: int(x) - 1, stdin.readline().split()) #offset by 1 due to zero indexing
    if components[x1][y1] == components[x2][y2]:
        stdout.write("binary\n") if grid[x1][y1] == '0' else stdout.write("decimal\n")
    else:
        stdout.write("neither\n")
