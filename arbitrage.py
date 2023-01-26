from sys import stdin,stdout
from math import log

def possible(adjMat,C):
    for i in range(C):
        if adjMat[i][i] < 0:
            return "Arbitrage" #negative cycle found
    return "Ok"

INF = 10**9
while True:
    C = int(stdin.readline())
    if C == 0: break
    currencies = stdin.readline().split()
    mappings = {currencies[i] : i for i in range(C)}
    #use adjacency matrix to store edge information
    adjMat = [[INF for i in range(C)] for j in range(C)]
    for i in range(int(stdin.readline())):
        A,B,rate = stdin.readline().split()
        u,v = mappings[A],mappings[B]
        a,b = map(int,rate.split(":"))
        w = -log(b / a)
        adjMat[u][v] = w #weight of each edge is the negation of the natural logarithm of the exchange ratio
    #perform Floyd Warshall in O(C^3)
    for k in range(C):
        for i in range(C):
            for j in range(C):
                adjMat[i][j] = min(adjMat[i][j], adjMat[i][k] + adjMat[k][j])
    stdout.write(f"{possible(adjMat,C)}\n")
            
            
        


    
