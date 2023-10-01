from sys import stdin,stdout

winners = {"B": 1, "R": 0}

def checkRow(grid,X,Y,N):
    prev,consec = "-",0
    for i in range(X):
        for j in range(Y):
            if grid[i][j] == prev:
                consec += 1
                if consec >= N and grid[i][j] in winners:
                    return winners[grid[i][j]]
            else:
                prev = grid[i][j]
                consec = 1
    return -1 # indicate no winners

def checkCol(grid,X,Y,N):
    prev,consec = "-",0
    for i in range(Y):
        for j in range(X):
            if grid[j][i] == prev:
                consec += 1
                if consec >= N and grid[j][i] in winners:
                    return winners[grid[j][i]]
            else:
                prev = grid[j][i]
                consec = 1
    return -1 # indicate no winners

def checkDiag(grid,X,Y,N):
    # check right diagonals
    for i in range(X - N + 1):
        for j in range(Y - N + 1):
            curr = grid[i][j]
            a,b = i,j
            for k in range(N - 1):
                a += 1; b += 1
                if grid[a][b] != curr:
                    break
            else:
                if curr in winners:
                    return winners[curr]
    # check left diagonals
    for i in range(X - N + 1, X):
        for j in range(Y - N + 1):
            curr = grid[i][j]
            a,b = i,j
            for k in range(N - 1):
                a -= 1; b += 1
                if grid[a][b] != curr:
                    break
            else:
                if curr in winners:
                    return winners[curr]
    return -1
            
X,Y,N = map(int,stdin.readline().split())
grid = [stdin.readline().split() for i in range(X)]
ans = {checkRow(grid,X,Y,N),checkCol(grid,X,Y,N),checkDiag(grid,X,Y,N)}
if 1 in ans:
    stdout.write("BLUE WINS\n")
elif 0 in ans:
    stdout.write("RED WINS\n")
else:
    stdout.write("NONE\n")
