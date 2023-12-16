from sys import stdin,stdout

n,m,k = map(int,stdin.readline().split())
cols = list(map(int,stdin.readline().split()))
grid = [list(stdin.readline().strip()) for i in range(n)]
obstacles = {"#", "?","~"}
for c in cols:
    frontier = [(0,c)]
    grid[0][c] = "~"
    while frontier:
        r,c = frontier.pop()
        if 0 <= r + 1 <= n - 1 and 0 <= c <= m - 1:
            if grid[r + 1][c] == "O":
                grid[r + 1][c] = "~"
                frontier.append((r + 1, c))
            # flow to left and right when an obstacle is met
            elif grid[r + 1][c] != "~": #obstacle met
                if 0 <= c - 1 <= m - 1 and grid[r][c - 1] not in obstacles:
                    grid[r][c - 1] = "~"
                    frontier.append((r, c - 1)) 
                if 0 <= c + 1 <= m - 1 and grid[r][c + 1] not in obstacles:
                    grid[r][c + 1] = "~"
                    frontier.append((r, c + 1))
stdout.write("\n".join("".join(row) for row in grid))
