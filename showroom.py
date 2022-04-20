from sys import stdin,stdout
from heapq import heappush,heappop,heapify

def possiblepositions(i,j,r,c,grid):
    movements = [(-1,0),(0,1),(1,0),(0,-1)]
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c) and grid[i+x][j+y] != '#']

def modifiedDjikstra(a,b,R,C,grid):
    visited,PQ = [[False for i in range(C)] for j in range(R)],[]
    # enqueue all the doors at borders into PQ
    for i in range(R):
        if grid[i][0] == 'D':
            PQ.append((0,i,0))
        if grid[i][C-1] == 'D':
            PQ.append((0,i,C-1))
    for j in range(1,C-1): #start from 1 and end at C-1 to avoid double counting
        if grid[0][j] == 'D':
            PQ.append((0,0,j))
        if grid[R-1][j] == 'D':
            PQ.append((0,R-1,j))
    heapify(PQ)
    while PQ: #O(RClog(RC))
        counter,i,j = heappop(PQ)
        if not visited[i][j]:
            visited[i][j] = True
            for x,y in possiblepositions(i,j,R,C,grid):
                if x == a and y == b:
                    return str(counter+1) #(a,b) hasa car
                if not visited[x][y]:
                    heappush(PQ,(counter+1,x,y)) if grid[x][y] == 'c' else heappush(PQ,(counter,x,y)) #door

R,C = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for _ in range(R)]
a,b = map(lambda x: int(x) - 1,stdin.readline().split()) # offset by 1 due to zero indexing
stdout.write(modifiedDjikstra(a,b,R,C,grid))
