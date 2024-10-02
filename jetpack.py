from sys import stdin,stdout

class State:
    def __init__(self,parent,curr):
        self.parent = parent
        self.curr = curr
    
movements = [(1,1),(-1,1)]

def possiblepositions(x,y,r,c,grid):
    pos = [(x + i,y + j) for i,j in movements if x + i in range(r) and y + j in range(c) and grid[x + i][y + j] != "X"]
    # horizontal movement can only happen on the ceiling or floor
    if (x == r - 1 or x == 0) and y + 1 in range(c) and grid[x][y + 1] != "X":
        pos.append((x,y + 1))
    return pos

def DFS(grid,N):
    # start from bottom left
    visited = [[False for _ in range(N)] for j in range(10)]
    frontier = [State(None,(9,0))]
    visited[9][0] = True
    while frontier:
        s = frontier.pop()
        a,b = s.curr
        for x,y in possiblepositions(a,b,10,N,grid):
            if y == N - 1: #reached the right:
                return State(s,(x,y))
            if not visited[x][y]:
                visited[x][y] = True
                frontier.append(State(s,(x,y)))
    return None
            
N = int(stdin.readline())
grid = [stdin.readline().strip() for _ in range(10)]
ans = DFS(grid,N)
path,c = [],ans
while c != None:
    path.append(c.curr)
    c = c.parent
path.reverse()
moves,i,consec = [],0,0
while i < len(path) - 1:
    a,b = path[i]
    c,d = path[i + 1]
    if (a - 1 == c and b + 1 == d) or (a == c == 0 and b + 1 == d):
        consec += 1
    elif consec > 0: # no longer ascending
        moves.append((i - consec, consec))
        consec = 0
    i += 1
if consec > 0:
    moves.append((i - consec,consec))
stdout.write(f"{len(moves)}\n")
for start,length in moves:
    stdout.write(f"{start} {length}\n")

    
