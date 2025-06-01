from sys import stdin,stdout

N = int(stdin.readline())
laser_pointers  = []
for i in range(N):
    x,y,m,name = stdin.readline().split()
    x,y,m = map(float,[x,y,m])
    if m != 0:
        # y = mx + c
        c = y - m * x
        # x intercept
        x0 = - c / m
        # laser pointers are pointing rightwards
        if x0 > x:
            laser_pointers.append((x0,name))
laser_pointers.sort()
for x0,name in laser_pointers:
    stdout.write(f"{name}\n")
