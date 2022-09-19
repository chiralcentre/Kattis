from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    INF = 10**9 # use one billion to represent infinity
    M,C = map(int,stdin.readline().split())
    #Prim's variant for dense graphs is used
    adjMat = [[INF for i in range(C)] for j in range(C)]
    for i in range(C*(C-1)//2):
        u,v,w = map(int,stdin.readline().split())
        adjMat[u][v] = adjMat[v][u] = w
    A,taken = [(INF,v) for v in range(C)],[False for _ in range(C)]
    A[0] = (0,0) #start from first point
    taken[0] = True; cost = 0; counter = 1
    while counter < C: #O(C)
        lowest,v = INF,0 # scan A to get v where A[v][0] is minimum in A
        for i in range(C): #O(C)
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
        for j in range(C): #O(C)
            if not taken[j] and A[j][0] > adjMat[j][v]:
                A[j] = (adjMat[j][v],v)
    stdout.write("yes\n") if cost + C <= M else stdout.write("no\n")
