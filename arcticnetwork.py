from sys import stdin,stdout
from math import sqrt
from heapq import heappush,heappop,heapify

INF = 10**9 # use one billion to represent infinity
for _ in range(int(stdin.readline())): #Prim's variant for dense graphs is used
    S,P = map(int,stdin.readline().split())
    points = [tuple(map(int,stdin.readline().split())) for _ in range(P)]
    A,taken = [(INF,v) for v in range(P)],[False for _ in range(P)]
    A[0] = (0,0) #start from first point
    taken[0] = True; cost = []; counter = 1
    while counter < P: #O(P)
        lowest,v = INF,0 # scan A to get v where A[v][0] is minimum in A
        for i in range(P): #O(P)
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
        cost.append(-A[v][0]) ## since default heap in Python is a min heap, a minus sign is required to turn it into max heap
        A[v] = (INF,A[v][1]) #prevent picking the same point
        for j in range(P): #O(P)
            if not taken[j] and A[j][0] > sqrt((points[v][0]-points[j][0])**2+(points[v][1]-points[j][1])**2):
                A[j] = (sqrt((points[v][0]-points[j][0])**2+(points[v][1]-points[j][1])**2),v)
    heapify(cost) #O(P)
    for i in range(S-1):
        heappop(cost) # with S channels, S - 1 edges can be removed
    stdout.write("{:.2f}".format(-heappop(cost))+'\n') # heappop(cost) to remove largest edge weight D in remaining edges; all remaining edges will have weights < D
    
