from sys import stdin,stdout

first = True
while True:
    n,m,q = map(int,stdin.readline().split())
    if n == m == q == 0:
        break
    if first:
        first = False
    else:
        stdout.write('\n') #print new line
    # Floyd Warshall's algorithm is used  
    INF = 1000000000 # use 1 billion to reprsent infinity
    D = [[INF for i in range(n)] for j in range(n)]
    for i in range(n): #initialise diagonals with 0, O(n)
        D[i][i] = 0
    for _ in range(m):
        u,v,w = map(int,stdin.readline().split())
        D[u][v] = min(w,D[u][v])
    # first iteration of Floyd Warshall
    for k in range(n): #O(n^3) time complexity
        for i in range(n):
            for j in range(n):
                total = INF if D[i][k] == INF or D[k][j] == INF else D[i][k]+D[k][j] #this line is to guard against large negative numbers
                D[i][j] = min(D[i][j],total)
    # second iteration of Floyd Warshall
    for k in range(n): #O(n^3) time complexity
        for i in range(n):
            for j in range(n):
                if D[i][k] != INF and D[k][j] != INF and D[k][k] < 0: #can be relaxed
                    D[i][j] = -INF
    for i in range(q): #O(q)
        u,v = map(int,stdin.readline().split())
        stdout.write("Impossible\n") if D[u][v] == INF else stdout.write("-Infinity\n") if D[u][v] == -INF else stdout.write(f'{D[u][v]}\n')
        
                
