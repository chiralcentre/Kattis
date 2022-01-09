from math import sin,cos,radians
for _ in range(int(input())):
    v0,angle,x1,h1,h2 = map(float,input().split())
    t = x1/(v0*cos(radians(angle)))
    y = v0*t*sin(radians(angle)) - 9.81*t**2/2
    print('Safe') if h1 + 1 <= y <= h2 - 1 else print('Not Safe')
