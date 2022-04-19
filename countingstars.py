from sys import stdin,stdout

def possiblepositions(i,j,r,c,grid):
    movements = [(-1,0),(0,1),(1,0),(0,-1)]
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c) and grid[i+x][j+y] == '-']
#iterative DFS
def DFS(i,j,r,c,grid,visited):
    visited[i][j] = True
    frontier = [(i,j)]
    while frontier:
        a,b = frontier.pop()
        for x,y in possiblepositions(a,b,r,c,grid):
            if not visited[x][y]:
                visited[x][y] = True
                frontier.append((x,y))
                
counter = 1            
while True:
    try:
        m,n = map(int,stdin.readline().split())
    except: #EOF
       break
    grid = [stdin.readline().strip() for i in range(m)]
    stars,visited = 0,[[False for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '-' and not visited[i][j]:
                stars += 1
                DFS(i,j,m,n,grid,visited)
    stdout.write(f'Case {counter}: {stars}\n')
    counter += 1
