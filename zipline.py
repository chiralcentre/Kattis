from sys import stdin,stdout
from math import sqrt

def zipline(x,w,g,h,r):
    return sqrt(x**2+(g-r)**2) + sqrt((h-r)**2+(w-x)**2)

def turning_x(w,g,h,r):
    # value of x for which L is minimum is derived from solution to Heron's problem
    return w*(g-r)/(h+g-2*r) if h + g - 2*r != 0 else 0

for _ in range(int(stdin.readline())):
    w,g,h,r = map(int,stdin.readline().split())
    minimum = zipline(turning_x(w,g,h,min(g,h)),w,g,h,min(g,h)) # attained when r is highest possible
    maximum = zipline(turning_x(w,g,h,r),w,g,h,r) # attained when r is smallest possible
    stdout.write(f'{minimum} {maximum}\n')
