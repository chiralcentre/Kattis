from sys import stdin
from math import sin, cos, pi

S = sin(pi / 4)
C = cos(pi / 4)
n = int(stdin.readline())
x,y = map(int,stdin.readline().split())
for _ in range(n - 1):
    di,d = stdin.readline().split()
    d = int(d)
    if di == "N":
        y += d
    elif di == "S":
        y -= d
    elif di == "E":
        x += d
    elif di == "W":
        x -= d
    elif di == "NE":
        x += d * C
        y += d * S
    elif di == "SE":
        x += d * C
        y -= d * S
    elif di == "SW":
        x -= d * C
        y -= d * S
    else: # NW
        x -= d * C
        y += d * S
print(f"{x} {y}")
