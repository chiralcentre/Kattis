from sys import stdin

costs = {".": 20, "O": 10, "\\": 25, "/": 25,
         "A": 35, "^": 5, "v": 22}
n,m = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for _ in range(n)]
print(sum(costs[grid[i][j]] for i in range(n) for j in range(m)))
