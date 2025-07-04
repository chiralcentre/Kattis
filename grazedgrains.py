from sys import stdin
import random

n = int(stdin.readline())
circles = [tuple(map(int,stdin.readline().split())) for _ in range(n)]

# monte carlo approach: generate r random points in the range [-10,20] x [-10,20]
# if x of the r points are inside a circle, area is estimated as x / r * 30^2
# runs in O(nr) time
P,T = pow(10,6),0
for i in range(P):
    a,b = random.uniform(-10,20),random.uniform(-10,20)
    for x,y,r in circles:
        D = (a - x) ** 2 + (b - y) ** 2
        if D <= (r ** 2):
            T += 1
            break
print(T / P * 900)
