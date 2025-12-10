from sys import stdin, stdout

x1, y1 = map(int, stdin.readline().split())
x2, y2 = map(int, stdin.readline().split())
H = int(stdin.readline())

dx1, dy1 = x2 - x1, y2 - y1

for _ in range(H):
    x3, y3 = map(int, stdin.readline().split())
    x4, y4 = map(int, stdin.readline().split())
    dx2, dy2 = x4 - x3, y4 - y3
    cross = dx1 * dy2 - dy1 * dx2
    if cross != 0:
        stdout.write("YES\n")
    else:
        # parallel - check collinearity
        if (x3 - x1) * dy1 - (y3 - y1) * dx1 == 0:
            stdout.write("NO\n")  # collinear => aliens refuse
        else:
            stdout.write("NO\n")  # distinct parallel => no intersection
