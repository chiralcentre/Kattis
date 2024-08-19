from sys import stdin,stdout

R,S,K = map(int,stdin.readline().split())
grid = [list(stdin.readline().strip()) for _ in range(R)]
prefixSum = [[0 for i in range(S)] for j in range(R)]
if grid[0][0] == "*":
    prefixSum[0][0] = 1
# fill in first row and first column of prefix sum array
for i in range(1,S):
    prefixSum[0][i] = prefixSum[0][i - 1] + (grid[0][i] == "*")
for i in range(1,R):
    prefixSum[i][0] = prefixSum[i - 1][0] + (grid[i][0] == "*")
# compute prefix sums in O(RS) time
for i in range(1,R):
    for j in range(1,S):
        prefixSum[i][j] = prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1] + (grid[i][j] == "*")
# area covered by racket is (K - 2) x (K - 2)
L = K - 2
best,x,y = -1,None,None
for i in range(1, R - L):
    for j in range(1, S - L):
        f = prefixSum[i + L - 1][j + L - 1] - prefixSum[i + L - 1][j - 1] - prefixSum[i - 1][j + L -  1] + prefixSum[i - 1][j - 1]
        if f > best:
            best = f
            x,y = i,j

x -= 1; y -= 1;
stdout.write(f"{best}\n")
for i in range(K):
    grid[x][y + i] = "-"
    grid[x + K - 1][y + i] = "-"
for j in range(K):
    grid[x + j][y] = "|"
    grid[x + j][y + K - 1] = "|"
grid[x][y] = "+"
grid[x + K - 1][y] = "+"
grid[x][y + K - 1] = "+"
grid[x + K - 1][y + K - 1] = "+"
stdout.write("\n".join("".join(row) for row in grid))
