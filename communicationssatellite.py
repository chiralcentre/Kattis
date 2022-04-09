from sys import stdin,stdout
from math import sqrt

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
    cost += A[v][0]
    A[v] = (INF,A[v][1]) #prevent picking the same point
    for j in range(N): #O(N)
        if not taken[j] and A[j][0] > sqrt((points[v][0]-points[j][0])**2+(points[v][1]-points[j][1])**2) - points[v][2] - points[j][2]: #subtract radius of two circles from distance between their two centres
            A[j] = (sqrt((points[v][0]-points[j][0])**2+(points[v][1]-points[j][1])**2) - points[v][2] - points[j][2],v)
stdout.write(f'{cost}\n')
