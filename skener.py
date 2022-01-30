R,C,ZR,ZC = map(int,input().split())
article = [input().strip() for _ in range(R)]
matrix = [[0 for i in range(C*ZC)] for j in range(R*ZR)]
for i in range(R):
    for j in range(C):
        for k in range(ZR*i,ZR*(i+1)):
            for m in range(ZC*j,ZC*(j+1)):
                matrix[k][m] = article[i][j]
print('\n'.join(''.join(row) for row in matrix))

