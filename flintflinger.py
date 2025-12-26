from sys import stdin,stdout

N = int(stdin.readline())
# get rid of decimal to prevent floating point imprecision
cities = [tuple(map(lambda x: int(float(x) * 10),stdin.readline().split())) for _ in range(N)]
attack = [0 for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        ax,ay,r = cities[i]
        bx,by,_ = cities[j]
        D = pow(ax - bx, 2) + pow(ay - by, 2)
        if D <= pow(r, 2):
            attack[j] += 1
for num in attack:
    stdout.write(f"{num}\n")
