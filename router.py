from sys import stdin

N = int(stdin.readline())
lx,mx,ly,my,cx,cy = 0,0,0,0,0,0
for _ in range(N):
    char,d = stdin.readline().split()
    d = int(d)
    if char == "U":
        cx += d
    elif char == "R":
        cy += d
    elif char == "L":
        cy -= d
    else:
        cx -= d
    lx = min(cx,lx)
    mx = max(cx,mx)
    ly = min(cy,ly)
    my = max(cy,my)
print(f"{my - ly + 40} {mx - lx + 40}")
    
