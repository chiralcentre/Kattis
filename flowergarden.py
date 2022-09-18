from sys import stdin,stdout
from math import sqrt

def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if not n%2:
        return False
    for i in range(3,int(sqrt(n))+1,2): #n must be odd now
        if not n%i:
            return False
    return True

def euclidean_distance(p1,p2):
    x1,y1 = p1; x2,y2 = p2;
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def maximum_flowers(flowers,N,D):
    d,watered = 0,0
    origin = (0,0)
    d += euclidean_distance(origin,flowers[0])
    if d > D:
        return 0
    else:
        watered += 1
    for i in range(N-1):
        d += euclidean_distance(flowers[i],flowers[i+1])
        if d > D:
            break
        watered += 1
    while not isPrime(watered) and watered > 0:
        watered -= 1
    return watered
    
    
for _ in range(int(stdin.readline())):
    N,D = map(int,stdin.readline().split())
    flowers = [tuple(map(int,stdin.readline().split())) for i in range(N)]
    stdout.write(f"{maximum_flowers(flowers,N,D)}\n")
    
