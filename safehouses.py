from sys import stdin

N = int(stdin.readline())
grid = [stdin.readline().strip() for _ in range(N)]
houses,spy = [],[]
# O(N^2) time
for i in range(N):
    for j in range(N):
        if grid[i][j] == "H":
            houses.append((i, j))
        elif grid[i][j] == "S":
            spy.append((i,j))
# O(N^3) time
best = -1
for x,y in spy:
    lowest = pow(10,9)
    for a,b in houses:
        lowest = min(abs(a - x) + abs(b - y), lowest)
    best = max(lowest, best)
print(best)
