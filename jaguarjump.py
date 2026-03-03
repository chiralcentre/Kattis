from sys import stdin

# assume only one occurrence of each character in grid exists
def find_pos(grid,chars):
    pos = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] in chars:
                pos[grid[i][j]] = (i,j)
    return pos

W,H,D = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for _ in range(H)]
pos = find_pos(grid,{"@","J"})
ax,ay = pos["@"]
bx,by = pos["J"]
d = (ax - bx) ** 2 + (ay - by) ** 2
print("no jumpscares here") if d > D ** 2 else print("the guide is right")
