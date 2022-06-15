from sys import stdin,stdout
from heapq import heappush,heappop

def modifiedDjikstra(s,t,k,V):
    # vertex splitting is performed here
    # D[a][b] represents the shortest path to a using b junctions
     #k is inclusive of s, so remove 1 from k, so that we can start at s with 0 junctions
    k -= 1
    D = [[INF for i in range(k+1)] for j in range(V)]
    for m in range(k+1): #prevent cycling back to start vertex 
        D[s][m] = 0
    # use 1 number to store shortest distance thus far,the number of junctions left to pass through, and the vertex number
    div = V**2 #the square of V is chosen since k <= V, and (k-1)*V is smaller than V**2
    # Let p be the integer inserted into PQ. p = D[u][a]*div + a*V + u, s stores the information for (u,a) = (s,0)
    PQ = [s]; sol = -1
    while PQ: #modified Djikstra on the state space graph
        p = heappop(PQ)
        #p = d*V**2 + a*V + u; p//V = d*V+a; (p//V)%V = a
        d,a,u = p//div,(p//V)%V,p%V
        if u == t: #end is reached
            sol = d
            return sol
        if a + 1 <= k and d == D[u][a]:
            for v,w in adjList[u]:
                if D[v][a+1] > d + w:
                    D[v][a+1] = d + w 
                    heappush(PQ, (D[v][a+1]*div + (a+1)*V + v))
    return sol

#perform modified Djikstra for each query in O(kE log kE) where E is number of edges
#total time complexity is O(kQE log kE)
INF = 1000000000 #use 1 billion to represent infinity
for a in range(int(stdin.readline())):
    if a > 0: stdout.write("\n") #print new line
    stdin.readline() # skip newline
    V = int(stdin.readline())
    adjList = [[] for _ in range(V)]
    for i in range(V):
        X,*edges = map(int,stdin.readline().split())
        for j in range(0,2*X,2):
            adjList[i].append((edges[j],edges[j+1]))
    for i in range(int(stdin.readline())):
        s,t,k = map(int,stdin.readline().split())
        if s != t and k < 2:
            stdout.write("-1\n")
        elif s == t:
            stdout.write("0\n")
        else:
            stdout.write(str(modifiedDjikstra(s,t,k,V))+'\n')
            
