from sys import stdin,stdout
from collections import deque

def possiblepositions(i,j,r,c):
    movements = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c)]

def BFS(start_x,start_y,end_x,end_y,r,c):
    if start_x == end_x and start_y == end_y: # start and end position are the same
        return 0
    visited = [[False for i in range(c)] for j in range(r)]
    frontier = deque([(start_x,start_y,0)]) #third coordinate keeps track of number of jumps
    visited[start_x][start_y] = True
    while frontier: 
        i,j,counter = frontier.popleft()
        for a,b in possiblepositions(i,j,r,c):
            if a == end_x and b == end_y:
                return counter + 1
            if not visited[a][b]:
                frontier.append((a,b,counter+1))
                visited[a][b] = True
    return "impossible" #if BFS does not lead to that particular square

while True:
    try:
        R,C,Gr,Gc,Lr,Lc = map(int,stdin.readline().split())
        stdout.write(f'{BFS(Gr-1,Gc-1,Lr-1,Lc-1,R,C)}\n') #offset by 1 due to zero indexing
    except:
        break
