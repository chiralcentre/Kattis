from sys import stdin,stdout

R,C = map(int,stdin.readline().split())
quilt = [['.' for i in range(C)] for j in range(R)]
N = int(stdin.readline())
patches = []
for _ in range(N):
    r,c = map(int,stdin.readline().split())
    patch = [stdin.readline().strip() for i in range(r)]
    patches.append((r,c,patch))
for _ in range(int(stdin.readline())):
    q,t,p = map(int,stdin.readline().split())
    r,c,patch = patches[p - 1]
    for i in range(q,min(q + r,R)):
        for j in range(t,min(t + c,C)):
            quilt[i][j] = patch[i - q][j - t]
stdout.write("\n".join("".join(row) for row in quilt))
