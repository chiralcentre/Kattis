from sys import stdin,stdout
from heapq import heappush,heappop

def possiblepositions(i,j,r,c):
    movements = [(-1,0),(1,0),(0,1),(0,-1)]
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c)]

# initial water level is 1
# water level required to reach exit is maximum height along minimax path from start to exit + 1
N = int(stdin.readline())
grid = [list(map(int,stdin.readline().split())) for _ in range(N)]
#find minimax path from (0,0) to (N-1,N-1) which can be done using Prim's algorithm
PQ,largestHeight = [(0,0,0)],0
taken = [[False for i in range(N)] for j in range(N)]
while PQ:
    w,x,y = heappop(PQ)
    if not taken[x][y]:
        taken[x][y] = True
        if w > largestHeight:
            largestHeight = w
        if x == N - 1 and y == N - 1: #endpoint reached
            break
        for a,b in possiblepositions(x,y,N,N):
            if not taken[a][b]:
                heappush(PQ,(grid[a][b],a,b))
stdout.write(str(largestHeight))
