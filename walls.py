from sys import stdin,stdout
from itertools import combinations

def dist_squared(p1,p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

def minimum_cranes(cranes,n):
    for k in range(1,min(n+1,5)): #from 1 crane to 4/n cranes, whichever is smaller
        choices = combinations(cranes,k)
        for group in choices:
            intersection = []
            for point in group:
                intersection.extend(cranes[point])
            if len(set(intersection)) == 4:
                return str(k)
    return "Impossible"

#perform brute force checking of all possible combinations of cranes up to 4 cranes, since a maximum of 4 cranes is required
l,w,n,r = map(int,stdin.readline().split())
centres = [(-l/2,0),(l/2,0),(0,-w/2),(0,w/2)]
cranes = {}
for _ in range(n):
    p1 = tuple(map(int,stdin.readline().split()))
    reachable = [p2 for p2 in centres if dist_squared(p1,p2) <= r**2]
    cranes[p1] = reachable
stdout.write(f"{minimum_cranes(cranes,n)}")
