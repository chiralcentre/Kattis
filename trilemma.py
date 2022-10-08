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

#SED stands for squared euclidean distance
def SED(p1,p2):
    x1,y1 = p1; x2,y2 = p2
    return (x2 - x1)**2 + (y2 - y1)**2

def classify(x1,y1,x2,y2,x3,y3):
    p1,p2,p3 = (x1,y1),(x2,y2),(x3,y3)
    #check if the points lie on the same line (degenerate triangle)
    gradients = {gradient(p1,p2),gradient(p1,p3),gradient(p2,p3)}
    if len(gradients) < 3:
        return "not a triangle"
    a,b,c = SED(p1,p2),SED(p2,p3),SED(p1,p3)
    a,b,c = sorted([a,b,c]) #reassign in ascending order
    lengthClasses = ["scalene","isosceles"]
    #there are sides that are equal
    pointer = 1 if len({a,b,c}) < 3 else 0
    #right triangle by Pythagoras' theorem
    if a + b == c:
        return f"{lengthClasses[pointer]} right triangle"
    elif a + b > c:
        return f"{lengthClasses[pointer]} acute triangle"
    else:
        return f"{lengthClasses[pointer]} obtuse triangle"

for i in range(int(stdin.readline())):
    x1,y1,x2,y2,x3,y3 = map(int,stdin.readline().split())
    stdout.write(f"Case #{i+1}: {classify(x1,y1,x2,y2,x3,y3)}\n")
