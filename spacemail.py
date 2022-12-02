from sys import stdin,stdout
from math import sqrt,ceil

def distance(p1,p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

INF = 10**9 # use one billion to represent infinity
N = int(stdin.readline())
#Prim's variant for dense graphs is used
points = [tuple(map(int,stdin.readline().split())) for _ in range(N)]
A,taken = [(INF,v) for v in range(N)],[False for _ in range(N)]
A[0] = (0,0) #start from first point
taken[0] = True; cost = 0; counter = 1
while counter < N: #O(N)
    lowest,v = INF,0 # scan A to get v where A[v][0] is minimum in A
    for i in range(N): #O(N)
        if A[i][0] < lowest:
            lowest = A[i][0]
            v = i
    #add vertices to taken
    if not taken[v]:
        taken[v] = True
        counter += 1
    if not taken[A[v][1]]:
        taken[A[v][1]] = True
        counter += 1
    cost = max(cost,A[v][0]) #find maximin cost
    A[v] = (INF,A[v][1]) #prevent picking the same point
    for j in range(N): #O(N)
        if not taken[j] and A[j][0] > distance(points[j],points[v]): 
            A[j] = (distance(points[j],points[v]),v)
stdout.write(f'{ceil(cost)}\n')
