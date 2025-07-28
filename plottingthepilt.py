from sys import stdin,stdout

movements = [(-1,0),(0,1),(1,0),(0,-1)]
    
def possiblepositions(i,j,r,c):
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c)]

R,C,d = map(int,stdin.readline().split())
A = [list(map(lambda x: int(x) // d,stdin.readline().split())) for _ in range(R)]
M = [[0 for i in range(C)] for j in range(R)]
for i in range(R):
    for j in range(C):
        M[i][j] = min(A[x][y] for x,y in possiblepositions(i,j,R,C))
for i in range(R):
    for j in range(C):
        if A[i][j] <= M[i][j]:
            stdout.write(" ")
        elif A[i][j] == M[i][j] + 1:
            stdout.write("+")
        elif A[i][j] == M[i][j] + 2:
            stdout.write("X")
        else:
            stdout.write("#")
    stdout.write("\n")

