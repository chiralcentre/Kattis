from sys import stdin,stdout

def move(sx,sy,d,m):
    if m == "up":
        sy += d
    elif m == "down":
        sy -= d
    elif m == "left":
        sx -= d
    else:
        sx += d
    return sx,sy

r,c = map(int,stdin.readline().split())
x,y = map(int,stdin.readline().split())
dirty = {i for i in range(1,min(r,c) + 1)}
if x == y:
    dirty.discard(x)
for _ in range(int(stdin.readline())):
    if not dirty:
        break
    d,m = stdin.readline().split()
    d = int(d)
    nx,ny = move(x,y,d,m)
    # eg: (2,1) move to (2,3), cover (2,2)
    # OR (2,3) move to (2,1)
    if x == nx and min(y,ny) <= nx <= max(y,ny):
        dirty.discard(nx)
    # eg: (2,4) move to (5,4), cover (4,4)
    # OR (5,4) move to (2,4)
    elif y == ny and min(x,nx) <= ny <= max(x,nx):
        dirty.discard(ny)
    stdout.write(f"{nx} {ny}\n")
    x,y = nx,ny
