from sys import stdin,stdout

def possiblepositions(i,j,r,c,wallpoints):
    movements = [(-1,0),(0,1),(1,0),(0,-1)]
    return [(i+x,j+y) for x,y in movements if i + x in range(c) and j + y in range(r) and (i+x,j+y) not in wallpoints]

while True:
    line = list(map(int,stdin.readline().split()))
    if len(line) == 1:
        break
    X,Y,T,L,W = line #X refers to number of columns, Y refers to number of rows
    leaks,walls,counter1,counter2 = [],[],0,0
    while counter1 < 2*L:
        leakLine = list(map(lambda x: int(x) - 1,stdin.readline().split())) #offset by 1 due to zero indexing
        counter1 += len(leakLine)
        leaks.extend(leakLine)
    while counter2 < 4*W:
        wallLine = list(map(lambda x: int(x) - 1,stdin.readline().split())) #offset by 1 due to zero indexing
        counter2 += len(wallLine)
        walls.extend(wallLine)
    # storing coordinates of wall
    wallpoints = set()
    for i in range(0,4*W,4):
        x1,y1,x2,y2 = walls[i],walls[i+1],walls[i+2],walls[i+3]
        a,b,c,d = min(x1,x2),min(y1,y2),max(x1,x2),max(y1,y2)
        if x1 == x2: #vertical wall
            for j in range(d-b+1):
                wallpoints.add((x1,b+j))
        elif y1 == y2: #horizontal wall
            for j in range(c-a+1):
                wallpoints.add((a+j,y1))
        else: # diagonal wall
            gradient = (y2-y1)//(x2-x1)
            
            for j in range(c-a+1):
                wallpoints.add((a+j,b+j)) if gradient == 1 else wallpoints.add((a+j,d-j))
    #BFS
    visited,frontier = [[False for i in range(Y)] for j in range(X)],[]
    wetTiles,time = L,1
    for i in range(0,2*L,2):
        frontier.append((leaks[i],leaks[i+1]))
        visited[leaks[i]][leaks[i+1]] = True
    while time < T and frontier:
        newFrontier = []
        for i,j in frontier:
            for a,b in possiblepositions(i,j,Y,X,wallpoints):
                if not visited[a][b]:
                    visited[a][b] = True
                    newFrontier.append((a,b))
        wetTiles += len(newFrontier)
        frontier = newFrontier
        time += 1
    stdout.write(f'{wetTiles}\n')
    
