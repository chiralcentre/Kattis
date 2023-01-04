from sys import stdin,stdout
from math import sqrt

def dist(x1,y1,x2,y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

#f is decreasing and increasing function 
def f(x,y,houses):
    return max(dist(houses[i][0],houses[i][1],x,y) for i in range(len(houses)))

EPSILON = 10**(-5)
while True:
    n = int(stdin.readline())
    if n == 0:
        break
    houses = [tuple(map(float,stdin.readline().split())) for _ in range(n)]
    L,H = -200000,200000
    while H - L > EPSILON: #perform ternary search
        d = (H - L) / 3
        m1,m2 = L + d, H - d
        if f(m1,0,houses) > f(m2,0,houses):
            L = m1
        else:
            H = m2
    ans = (L + H) / 2
    stdout.write(f"{ans:.7f} {f(ans,0,houses):.7f}\n") 
    stdin.readline() #read in blank line
