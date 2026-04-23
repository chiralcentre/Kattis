from sys import stdin,stdout
from collections import deque

class State:
    def __init__(self,prev = None,value=None):
        self.prev = prev
        self.value = value

INF = pow(10,9)
def possiblepositions(i,j,r,c,S,grid):
    output = []
    # move right, possible to still move right if on edge
    if j + 1 in range(c + 1):
        output.append((i,j + 1,int(grid[i][j] == "H"),S))
    # move up
    if grid[i][j] == "^" and i - 1 in range(r):
        output.append((i - 1,j,0,State(S,f"{j + 1}u")))
    # move down
    if grid[i][j] == "v" and i + 1 in range(r):
        output.append((i + 1,j,0,State(S,f"{j + 1}d")))
    return output

def solve(N,L,K,grid):
    frontier,d = deque([(K - 1,0,State())]),[[INF for i in range(L + 1)] for j in range(N)]
    d[K - 1][0] = 0
    while frontier:
        x,y,S = frontier.popleft()
        if y == L:
            return d[x][y],S
        # 0 - 1 BFS: append to front if weight is 0 else append to back
        for a,b,c,s in possiblepositions(x,y,N,L,S,grid):
            if d[x][y] + c < d[a][b]: 
                d[a][b] = d[x][y] + c
                frontier.append((a,b,s)) if c == 1 else frontier.appendleft((a,b,s))
    raise Exception("not supposed to reach here")


N,L = map(int,stdin.readline().split())
K = int(stdin.readline())
grid = [stdin.readline().strip() for _ in range(N)]
d,S = solve(N,L,K,grid)
stdout.write(f"{d}\n")
instructions = []
while S.prev != None:
    instructions.append(S.value)
    S = S.prev
for i in range(len(instructions) - 1,-1,-1):
    stdout.write(f"{instructions[i]}\n")
