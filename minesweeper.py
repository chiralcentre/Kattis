from sys import stdin,stdout

n,m,k = map(int,stdin.readline().split())
grid = [["." for i in range(m)] for j in range(n)]
for _ in range(k):
    x,y = map(lambda x: int(x) - 1, stdin.readline().split())
    grid[x][y] = "*"
stdout.write("\n".join("".join(row) for row in grid))
