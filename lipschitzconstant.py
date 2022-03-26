from sys import stdin,stdout
# this problem is equivalent to finding absolute value of maximum slope between two points
N = int(stdin.readline())
points = [(lambda x: (int(x[0]),float(x[1])))(stdin.readline().split()) for _ in range(N)]
points.sort(key = lambda y: y[0]) #sort points by x value, O(N log N)
maximum = -1
# it suffices to check pairs of consecutive points instead of checking every point
for i in range(N-1): #O(N)
    a,b = points[i]; c,d = points[i+1]
    slope = (d - b)/(c - a)
    if abs(slope) > maximum:
        maximum = abs(slope)
stdout.write(f"{maximum}\n")
    
