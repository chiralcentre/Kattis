from sys import stdin,stdout

n,k = map(int,stdin.readline().split())
# 2 rows
grid = [list(stdin.readline().strip()) for _ in range(2)]
# check for two cars diagonally across, and two cars in the same column
blockades = 0
for i in range(n):
    if grid[0][i] == "o": 
        if grid[1][i] == "o":
            blockades += 1
        if i > 0 and grid[1][i - 1] == "o":
            blockades += 1
        if i < n - 1 and grid[1][i + 1] == "o":
            blockades += 1
for _ in range(k):
    query = stdin.readline().split()
    if query[0] == "Q":
        stdout.write("Neibb\n") if blockades > 0 else stdout.write("Jebb\n")
    else:
        x,y = int(query[1]) - 1,int(query[2]) - 1
        r = 1 - x
        d = 1 if grid[x][y] == "." else -1
        new_symbol = "o" if grid[x][y] == "." else "."
        if grid[r][y] == "o":
            blockades += d
        if y > 0 and grid[r][y - 1] == "o":
            blockades += d
        if y < n - 1 and grid[r][y + 1] == "o":
            blockades += d
        grid[x][y] = new_symbol
