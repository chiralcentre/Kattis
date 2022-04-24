from sys import stdin,stdout

def possiblepositions(i,j,r,c,grid):
    movements = [(-1,0),(0,1),(1,0),(0,-1)]
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c) and grid[i+x][j+y] != 'X']

def BFS(r,c,grid):
    visited = [[False for j in range(c)] for i in range(r)]
    floodFrontier,painterFrontier = [],[]
    Dx,Dy = -1,-1
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'S':
                visited[i][j] = True
                painterFrontier.append((i,j))
            elif grid[i][j] == '*':
                visited[i][j] = True
                floodFrontier.append((i,j))
            elif grid[i][j] == 'D':
                Dx,Dy = i,j
    time = 0
    while painterFrontier:
        time += 1
        newFloodFrontier,newPainterFrontier = [],[] #go level by level
        for x1,y1 in floodFrontier:
            for i,j in possiblepositions(x1,y1,r,c,grid):
                if not visited[i][j] and (i,j) != (Dx,Dy): #cannot flood beavers den
                    visited[i][j] = True
                    newFloodFrontier.append((i,j))
        for x2,y2 in painterFrontier:
            for m,n in possiblepositions(x2,y2,r,c,grid):
                if not visited[m][n]:
                    if m == Dx and n == Dy:
                        return str(time)
                    visited[m][n] = True
                    newPainterFrontier.append((m,n))
        floodFrontier,painterFrontier = newFloodFrontier,newPainterFrontier
    return "KAKTUS"

r,c = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for _ in range(r)]
stdout.write(f'{BFS(r,c,grid)}')
