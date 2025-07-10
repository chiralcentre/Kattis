from sys import stdin,stdout

n,m = map(int,stdin.readline().split())
matrix = [list(map(int,stdin.readline().split())) for _ in range(n)]
dp = [0 for _ in range(n)]
for i in range(m):
    dp[0] += matrix[0][i]
    for j in range(1,n):
        dp[j] = max(dp[j], dp[j - 1]) + matrix[j][i]
stdout.write(" ".join(str(elem) for elem in dp))
