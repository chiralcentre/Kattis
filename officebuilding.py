from sys import stdin

def rotate90Clockwise(m):
    return [[m[j][i] for j in range(len(m)-1,-1,-1)] for i in range(len(m[0]))]

# code runs in O(R^2C^2) 
r,c = map(int,stdin.readline().split())
grid = [list(map(int,stdin.readline().split())) for _ in range(r)]
s,t = map(int,stdin.readline().split())
initial = [list(stdin.readline().strip()) for _ in range(s)]
floorplans = [initial]
for i in range(3):
    floorplans.append(rotate90Clockwise(floorplans[-1]))
total = sum(grid[i][j] for i in range(r) for j in range(c))
best = -1
for fp in floorplans:
    for i in range(r - len(fp) + 1):
        for j in range(c - len(fp[0]) + 1):
            best = max(best,total - sum(grid[i + k][j + m] for k in range(len(fp)) for m in range(len(fp[0])) if fp[k][m] == "#"))
print(best)
