from sys import stdin,stdout

N = int(stdin.readline())
adjMat = [list(map(int,stdin.readline().split())) for _ in range(N)]
dramaPotential = -1; triplet = (0,0,0)
for i in range(N): #O(N^3)
    for j in range(i+1,N):
        for k in range(j+1,N):
            if adjMat[i][j]*adjMat[j][k]*adjMat[k][i] > dramaPotential:
                dramaPotential = adjMat[i][j]*adjMat[j][k]*adjMat[k][i]
                triplet = (i,j,k)
            elif adjMat[i][j]*adjMat[j][k]*adjMat[k][i] == dramaPotential and (i,j,k) < triplet:
                triplet = (i,j,k)
stdout.write(' '.join(str(num+1) for num in triplet))
