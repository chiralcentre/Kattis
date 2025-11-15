from sys import stdin,stdout

W,H,N = map(int,stdin.readline().split())
y,x = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for _ in range(H)]
seesaws = {}
for i in range(H):
    for j in range(W):
        if grid[i][j] in ["-","|"]:
            seesaws[(i,j)] = True
for i in range(N):
    sx,sy = x,y
    stop = False
    while not stop:
        if grid[sx][sy] == "<":
            sy -= 1
        elif grid[sx][sy] == ">":
            sy += 1
        elif grid[sx][sy] == "^":
            sx -= 1
        elif grid[sx][sy] == "v":
            sx += 1
        elif grid[sx][sy] == "-":
            left = seesaws[(sx,sy)]
            seesaws[(sx,sy)] = not left
            sy += -1 if left else 1
        elif grid[sx][sy] == "|":
            up = seesaws[(sx,sy)]
            seesaws[(sx,sy)] = not up
            sx += -1 if up else 1
        elif grid[sx][sy] == ".":
            stop = True
        else:
            raise Exception("unaccounted for")
        if not (0 <= sx < H) or not (0 <= sy < W):
            stop = True
    stdout.write(f"{sy} {sx}\n")
