from sys import stdin,stdout

while True:
    try:
        M,N,C = stdin.readline().split()
    except:
        break
    M,N,C = int(M),int(N),C[1:-1]
    old = [stdin.readline().strip() for i in range(M)]
    silhouette_old,silhouette_new = [],[]
    stdin.readline()
    new = [stdin.readline().strip() for i in range(M)]
    background = [["" for i in range(N)] for j in range(M)]
    for i in range(M):
        for j in range(N):
            if old[i][j] != C:
                background[i][j] = old[i][j]
            else:
                silhouette_old.append((i,j))
            if new[i][j] != C:
                background[i][j] = new[i][j]
            else:
                silhouette_new.append((i,j))
    a = silhouette_new[0][0] - silhouette_old[0][0]
    b = silhouette_new[0][1] - silhouette_old[0][1]
    for x,y in silhouette_new:
        if 0 <= x + a < M and 0 <= y + b < N:
            background[x + a][y + b] = C
    stdout.write("\n".join("".join(char for char in row) for row in background))
    stdout.write("\n")
