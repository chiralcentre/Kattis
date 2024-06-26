from sys import stdin,stdout
from math import sqrt,pi

def distance(a,b):
    return sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))

for _ in range(int(stdin.readline())):
    r,n = map(int,stdin.readline().split())
    points = [tuple(map(int,stdin.readline().split())) for i in range(n)]
    track_length = 0
    for i in range(1,n):
        track_length += distance(points[i - 1], points[i])
    track_length += distance(points[-1],points[0])
    f = (track_length - 2 * r * pi) / track_length
    stdout.write(f"{f}\n") if f > 0 else stdout.write("Not possible\n")
    
