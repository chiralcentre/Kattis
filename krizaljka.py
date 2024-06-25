from sys import stdin,stdout

A,B = input().strip().split()
N,M = len(A),len(B)
grid = [["." for i in range(N)] for j in range(M)]
B_letters = set(B)
r,c = 10000,10000
for i in range(N):
    if A[i] in B_letters:
        b = B.index(A[i])
        r,c = b,i
        break
for i in range(N):
    grid[r][i] = A[i]
for i in range(M):
    grid[i][c] = B[i]
stdout.write("\n".join("".join(row) for row in grid))
