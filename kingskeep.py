from sys import stdin
from math import sqrt

# code runs in O(n^2)
n = int(stdin.readline())
points = [tuple(map(int,stdin.readline().split())) for _ in range(n)]
D = pow(10,18)
for x,y in points:
    d = sum(sqrt((x - px) ** 2 + (y - py) **2) for px,py in points)
    D = min(d,D)
print(D / (n - 1))
