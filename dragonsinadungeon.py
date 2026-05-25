from sys import stdin,stdout

movements = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
def possiblepositions(i,j,r,c,grid):
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c) and grid[i+x][j+y] != "M"]

def solve(r,c,grid):
    def find_start():
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "G":
                    return i,j
        raise Exception("not supposed to happen")
    sx,sy = find_start()
    frontier = [(sx,sy)]
    visited = [[False for j in range(c)] for i in range(r)]
    visited[sx][sy] = True
    while frontier:
        a,b = frontier.pop()
        for x,y in possiblepositions(a,b,r,c,grid):
            if not visited[x][y]:
                if grid[x][y] == "E":
                    return "YES"
                visited[x][y] = True
                frontier.append((x,y))
    return "NO"
    
r,c = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for _ in range(r)]
print(solve(r,c,grid))
