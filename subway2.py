from sys import stdin,stdout
from heapq import heappush,heappop
from math import sqrt

def distance(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)

INF = 1000000000 #use 1 billion to represent infinity
xs,ys,xe,ye = map(int,stdin.readline().split())
points,subway,counter = [(xs,ys),(xe,ye)],[-1,-1],0 
for line in stdin:
    coordinates = line.split()
    for i in range(0,len(coordinates)-2,2):
        points.append((int(coordinates[i]),int(coordinates[i+1])))
        subway.append(counter)
    counter += 1 #counter keeps track which subway line a point belongs to
T = [INF for _ in range(len(points))]; T[0] = 0
PQ = [(0,0)] #start from point 0
# modified Djikstra is used with O(n**2log(n)) time where n is number of points
while PQ:
    t,u = heappop(PQ)
    if t == T[u]:
        for v in range(len(points)):
            if v != u:
                d = distance(points[u][0],points[u][1],points[v][0],points[v][1])
                #belong to same subway line and the stops are adjacent
                if subway[v] == subway[u] and subway[u] != -1 and abs(v-u) == 1 and T[v] > T[u] + 60*d/40000:
                    T[v] = T[u] + 60*d/40000
                    heappush(PQ,(T[v],v))
                #walk
                elif T[v] > T[u] + 60*d/10000:
                    T[v] = T[u] + 60*d/10000
                    heappush(PQ,(T[v],v))
stdout.write(f'{round(T[1])}')
