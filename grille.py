from sys import stdin,stdout

# short code for rotating 90 degrees clockwise
def rotate90Clockwise(m):
    return [[m[j][i] for j in range(len(m)-1,-1,-1)] for i in range(len(m[0]))]

def solve(grid,string,n):
    visited = [["" for i in range(n)] for j in range(n)]
    h = sum(grid[i][j] == "." for i in range(n) for j in range(n))
    # check if number of holes is correct
    if h * 4 != n * n:
        return "invalid grille"
    # rotate four times 90 degrees clockwise
    for i in range(4):
        p = i * h
        # go from top to bottom, left to right
        for j in range(n):
            for k in range(n):
                if grid[j][k] == ".":
                    if not visited[j][k]:
                        visited[j][k] = string[p]
                        p += 1
                    elif visited[j][k] != string[p]:
                        return "invalid grille"
        grid = rotate90Clockwise(grid)
    return "".join("".join(char for char in row) for row in visited)
        
n = int(stdin.readline())
grid = [list(stdin.readline().strip()) for _ in range(n)]
string = stdin.readline().strip()
stdout.write(solve(grid,string,n))
                
