from sys import stdin,stdout

def nQueensVerifier(N):
    x,y = [False for _ in range(N)],[False for _ in range(N)]
    ld,rd = [False for _ in range(2*N)],[False for _ in range(2*N)]
    for i in range(N): #O(N)
        a,b = map(int,stdin.readline().split())
        #if queen lies in same row, column, left diagonal or right diagonal of previous queens, the solution is not valid
        #if a queen(a,b) lies on same left diagonal as (x,y), a - b + N = x - y + N
        #if a queen(a,b) lies on same right diagonal as (x,y), a + b = x + y
        if x[a] or y[b] or ld[a-b+N] or rd[a+b]:
            return "INCORRECT"
        x[a] = y[b] = ld[a-b+N] = rd[a+b] = True
    return "CORRECT"
    
stdout.write(nQueensVerifier(int(stdin.readline())))
