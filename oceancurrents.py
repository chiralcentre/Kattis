from sys import stdin,stdout
from collections import deque

INF = pow(10,9)
movements = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
def possiblepositions(i,j,r,c,grid):
    return [((i+x) * c + j + y,int(movements[int(grid[i][j])] != (x,y)))for x,y in movements if i + x in range(r) and j + y in range(c)]

def solve(grid,r,c,rs,cs,rd,cd):
    if rs == rd and cs == cd:
        return 0
    s,e = rs * c + cs, rd * c + cd
    frontier,d = deque([s]),[INF for i in range(c * r + 1)]
    d[s] = 0
    while frontier:
        u = frontier.popleft()
        if u == e:
            return d[e]
        # 0 - 1 BFS: append to front if weight is 0 else append to back
        for n,ne in possiblepositions(u // c, u % c,r,c,grid):
            if d[u] + ne < d[n]: 
                d[n] = d[u] + ne
                frontier.append(n) if ne == 1 else frontier.appendleft(n)
    return d[e]

r,c = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for _ in range(r)]
for _ in range(int(stdin.readline())):
    rs,cs,rd,cd = map(lambda x: int(x) - 1,stdin.readline().split())
    stdout.write(f"{solve(grid,r,c,rs,cs,rd,cd)}\n")

