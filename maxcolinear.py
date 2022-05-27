from sys import stdin,stdout
from math import gcd

def gradient(p1,p2):
    #returns (rise,run) tuple in simplest form
    #the actual gradient is not returned to avoid floating point math, as well as to avoid undefined gradients
    x1,y1 = p1; x2,y2 = p2
    if x2 == x1: #undefined gradient
        return (1,0) #standardise undefined gradient tuple as (1,0)
    rise,run = y2 - y1, x2 - x1
    if run < 0:
        rise = -rise; run = -run #standardise so that run will never be negative
    d = gcd(abs(rise),run) #gcd only works on positive numbers
    return (rise//d,run//d)
    
def maxCollinearPoints(points,n): #O(n^2)
    # at least three points are needed to potentially have non-collinear points
    if n < 3:
        return n
    highest = 0
    for i in range(n-1):
        slopes = {}
        for j in range(i+1,n):
            g = gradient(points[i],points[j])
            slopes[g] = 2 if g not in slopes else slopes[g] + 1 #every two points form a line
            if slopes[g] > highest:
                highest = slopes[g]
    return highest
            
while True:
    n = int(stdin.readline())
    if n == 0:
        break
    points = [tuple(map(int,stdin.readline().split())) for _ in range(n)]
    stdout.write(str(maxCollinearPoints(points,n))+'\n')
