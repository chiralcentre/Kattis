from sys import stdin,stdout

N,M = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for _ in range(N)]
for i in range(N):
    for j in range(M):
        if grid[i][j].isalpha():
            stdout.write(grid[i][j])
