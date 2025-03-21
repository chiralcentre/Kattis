from sys import stdin,stdout
from math import sin,cos,radians

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    x,y,angle = 0,0,0
    for i in range(n):
        a,d = map(float,stdin.readline().split())
        angle = (angle - a) % 360
        x += d * sin(radians(angle))
        y += d * cos(radians(angle))
    stdout.write(f"{x} {y}\n")
        
