from sys import stdin,stdout

N,M = map(int,stdin.readline().split())
grid = [list(stdin.readline().strip()) for _ in range(N)]
column_counts = [0 for _ in range(M)]
for i in range(M):
    for j in range(N):
        if grid[j][i] == "S":
            column_counts[i] += 1
            
for j in range(M):
    for i in range(N - 1, N - column_counts[j] - 1, -1):
        grid[i][j] = "S"
    for i in range(N - column_counts[j] - 1, -1, -1):
        grid[i][j] = "."

stdout.write("\n".join("".join(row) for row in grid))
