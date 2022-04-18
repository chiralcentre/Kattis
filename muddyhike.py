from sys import stdin,stdout
from heapq import heappush,heappop,heapify

def possiblepositions(i,j,r,c):
    movements = [(-1,0),(0,1),(1,0),(0,-1)]
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c)]

r,c = map(int,stdin.readline().split())
grid = [list(map(int,stdin.readline().split())) for _ in range(r)]
#Prim's algorithm is used to find maximum edge weight along minimax path with O(RC log RC) time complexity
taken = [[False for i in range(c)] for j in range(r)]
#(i,0) refers to leftmost column, multi source Prim's is conducted using all cells in leftmost column
PQ = [(grid[i][0],i,0) for i in range(r)]
heapify(PQ); maxDepth = 0
while PQ:
    depth,x,y = heappop(PQ)
    if not taken[x][y]:
        if depth > maxDepth:
            maxDepth = depth
        taken[x][y] = True
        if y == c - 1:
            break # rightmost column reached
        for x2,y2 in possiblepositions(x,y,r,c):
            if not taken[x2][y2]:
                heappush(PQ,(grid[x2][y2],x2,y2))
stdout.write(f'{maxDepth}')
