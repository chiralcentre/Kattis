from sys import stdin,stdout
from math import sqrt,ceil

def euclidDist(x1,y1,x2,y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

n,t = map(int,stdin.readline().split())
points = [tuple(map(int,stdin.readline().split())) for _ in range(n)]
highestTime = points[-1][-1]
actual = sum(euclidDist(points[i][0],points[i][1],points[i + 1][0],points[i + 1][1]) for i in range(n - 1))
est,px,py = 0,points[0][0],points[0][1]
for i in range(1,n):
    ox,oy,ot = points[i - 1]
    x,y,ct = points[i]
    lb,ub,T = ceil(ot / t), ct // t, ct - ot
    for j in range(lb * t, ub * t + 1, t):
        cx = ox + ((x - ox) * (j - ot) / T)
        cy = oy + ((y - oy) * (j - ot) / T)
        est += euclidDist(px,py,cx,cy)
        px,py = cx,cy
if highestTime % t: # not perfectly divisible, add in last point
    est += euclidDist(px,py,points[-1][0],points[-1][1])
stdout.write(f"{(actual - est) / actual * 100}\n")
