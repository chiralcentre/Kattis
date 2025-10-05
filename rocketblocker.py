from sys import stdin
from math import sqrt,pi

def shoelaceformula(x,y): #assuming coordinates of first point have been added
    return sum(x[i]*y[i+1] - y[i]*x[i+1] for i in range(len(x)-1))/2

r = float(stdin.readline())
x,y,points = [],[],[]
for _ in range(int(stdin.readline())):
    a,b = map(float,stdin.readline().split())
    x.append(a)
    y.append(b)
    points.append((a,b))
x.append(x[0])
y.append(y[0])
points.append(points[0])
P = 0
for i in range(1,len(points)):
    x1,y1 = points[i - 1]
    x2,y2 = points[i]
    P += sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
A = shoelaceformula(x,y)
print((A + r * P + pi * r * r) / 1000000)
