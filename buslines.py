from sys import stdin,stdout

#connect node 1 with all other nodes, thus creating a connected graph with n - 1 edges
#connect node n with all other nodes (except node 1), adding n - 2 edges to the graph
#All possible sums are covered, so it is not possible to add more edges.
#In other words, the maximum number of edges in the graph is 2n - 3.
#Minimum number of edges must be n - 1 for graph to be connected.

n,m = map(int,stdin.readline().split())
if n - 1 <= m <= 2*n - 3:
    #connect node 1 with all other nodes
    for i in range(2,n+1):
        stdout.write(f"{1} {i}\n")
    m -= (n - 1)
    #connect node n with other nodes to fill up remaining edges
    for i in range(2,m+2):
        stdout.write(f"{i} {n}\n")     
else:
    stdout.write("-1\n")
