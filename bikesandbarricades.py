from sys import stdin

best = None
for _ in range(int(stdin.readline())):
    x1,y1,x2,y2 = map(int,stdin.readline().split())
    # ensure x1 <= x2
    if x1 > x2:
        x1,x2 = x2,x1
        y1,y2 = y2,y1
    if x1 < 0 and x2 > 0 and x2 - x1 > 0:
        m = (y2 - y1) / (x2 - x1)
        c = y1 - m * x1
        if c >= 0:
            best = min(best, c) if best != None else c
print(best) if best != None else print(-1.0)
