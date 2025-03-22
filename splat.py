from sys import stdin,stdout
from math import pi,sqrt

# code runs in O(cnm) time
for _ in range(int(stdin.readline())):
    drops = []
    for i in range(int(stdin.readline())):
        X,Y,V,C = stdin.readline().split()
        drops.append((float(X),float(Y),sqrt(float(V) / pi),C))
    for i in range(int(stdin.readline())):
        x,y = map(float,stdin.readline().split())
        ans = "white"
        for X,Y,R,C in drops:
            if (X - x) ** 2 + (Y - y) ** 2 <= R ** 2:
                ans = C
        stdout.write(f"{ans}\n")
