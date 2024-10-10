from sys import stdin

movements = [(-1,0),(0,1),(1,0),(0,-1)]

def possiblepositions(i,j,r,c,grid):
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c)]

def solve(n, grid):
    visited = [[False for i in range(n)] for j in range(n)]
    unblocked,lit = 0,0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "?":
                for u,v in movements:
                    x,y = i,j
                    while x + u in range(n) and y + v in range(n):
                        x += u
                        y += v
                        if grid[x][y] == ".":
                            visited[x][y] = True
                        elif grid[x][y] == "?":
                            return 0
                        else:
                            break
            elif grid[i][j].isnumeric():
                bulbs = 0
                for x,y in possiblepositions(i,j,n,n,grid):
                    if grid[x][y] == "?":
                        bulbs += 1
                if bulbs != int(grid[i][j]):
                    return 0
            elif grid[i][j] == ".":
                unblocked += 1
    return int(unblocked == sum(visited[i][j] for i in range(n) for j in range(n)))

n = int(stdin.readline())
grid = [stdin.readline().strip() for _ in range(n)]
print(solve(n,grid))
