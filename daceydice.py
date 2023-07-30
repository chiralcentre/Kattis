from sys import stdin,stdout

# state 0: top
# state 1: right
# state 2: downwards
# state 3: upwards
# state 4: left
# state 5: bottom
opposite = {"U": "D", "D": "U", "L": "R", "R": "L"}
def diceState(s,m):
    if s == 0 or s == 5:
        if s == 5:
            m = opposite[m]
        return {"U": 3, "D": 2, "L": 4, "R": 1}[m]
    elif s == 1 or s == 4:
        if s == 4:
            m = opposite[m]
        if m == "L":
            return 0
        elif m == "R":
            return 5
        else:
            return s
    elif s == 2 or s == 3:
        if s == 3:
            m = opposite[m]
        if m == "U":
            return 0
        elif m == "D":
            return 5
        else:
            return s
        
def possiblepositions(i,j,r,c,grid,s):
    movements = [(-1,0,"U"),(0,1,"R"),(1,0,"D"),(0,-1,"L")]
    return [(i+x,j+y,diceState(s,m)) for x,y,m in movements if i + x in range(r) and j + y in range(c) and grid[i+x][j+y] != "*"]

#it is assumed the map always has an initial location
def findStart(grid,H,W):
    for i in range(H):
        for j in range(W):
            if grid[i][j] == "S":
                return (i,j)

def solve(grid,N):
    i,j = findStart(grid,N,N)
    #there are six possible states for the 5 face on die at any possible location
    visited = [[[False for m in range(6)] for _ in range(N)] for k in range(N)]
    frontier = [(i,j,4)]; visited[i][j][0] = True
    while frontier:
        x,y,s = frontier.pop()
        for a,b,ns in possiblepositions(x,y,N,N,grid,s):
            if not visited[a][b][ns]:
                if grid[a][b] == "H" and ns == 5:
                    return "Yes"
                visited[a][b][ns] = True
                frontier.append((a,b,ns))
    return "No"

for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    grid = [list(stdin.readline().strip()) for i in range(N)]
    stdout.write(f"{solve(grid,N)}\n")
    
