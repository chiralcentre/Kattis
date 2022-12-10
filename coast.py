from sys import stdin,stdout
from collections import deque

def possiblepositions(i,j,r,c):
    movements = [(-1,0),(0,1),(1,0),(0,-1)]
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c)]

#surround given map with empty squares, and perform flood fill to determine coastline
N,M = map(int,stdin.readline().split())
grid = [[] for i in range(N+2)]
grid[0],grid[N+1] = ['0' for _ in range(M+2)],['0' for _ in range(M+2)]
for i in range(1,N+1):
    row = ['0']
    row.extend(list(stdin.readline().strip()))
    row.append('0')
    grid[i] = row
#perform BFS flood fill from top left corner in O(NM) time
frontier = deque([(0,0)]); grid[0][0] = "2"
while frontier:
    i,j = frontier.popleft()
    for x,y in possiblepositions(i,j,N+2,M+2):
        if grid[x][y] == "0":
            frontier.append((x,y))
            grid[x][y] = "2"
#perform BFS again, with a visited array in O(NM) time
frontier,visited = deque([(0,0)]),[[False for i in range(M+2)] for j in range(N+2)]
visited[0][0] = True
coastline = 0
while frontier:
    i,j = frontier.popleft()
    for x,y in possiblepositions(i,j,N+2,M+2):
        if grid[x][y] == "1":
            coastline += 1
        elif grid[x][y] == "2" and not visited[x][y]:
            visited[x][y] = True
            frontier.append((x,y))
stdout.write(f"{coastline}")
