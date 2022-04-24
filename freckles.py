from sys import stdin,stdout
from math import sqrt

def distance(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)

for _ in range(int(stdin.readline())):
    stdin.readline() # blank line
    n,INF = int(stdin.readline()),1000000000 # use 1 billion to represent infinity
    points = [tuple(map(float,stdin.readline().split())) for i in range(n)]
    # use Prim's variant for dense graphs in O(n^2) time
    A,taken = [(INF,v) for v in range(n)],[False for i in range(n)]
    #start from point 0
    A[0] = (0,0); taken[0] = True
    cost = 0; counter = 1
    while counter < n: #not all vertices are in MST
        #scan A to get v where A[v][0] is minimum in A
        lowest,u = INF,0
        for i in range(n):
            if A[i][0] < lowest:
                lowest = A[i][0]
                u = i
        if not taken[u]:
            taken[u] = True
            counter += 1
        if not taken[A[u][1]]:
            taken[A[u][1]] = True
            counter += 1
        cost += A[u][0]
        A[u] = (INF,A[u][1]) #prevent picking same point
        for j in range(n):
            if not taken[j] and A[j][0] > distance(points[u][0],points[u][1],points[j][0],points[j][1]):
                A[j] = (distance(points[u][0],points[u][1],points[j][0],points[j][1]),u)
    stdout.write("{:.2f}".format(cost) + '\n')
