from sys import setrecursionlimit

# use top down dynamic programming with memoisation in O(NT) time
setrecursionlimit(1000000)

M = pow(10,9) + 9
N,K,T = map(int,input().split())
dp = [[-1 for i in range(T + 1)] for j in range(N + 1)]
for i in range(1,T + 1):
    dp[N][i] = 0
dp[N][0] = 1

def solve(index,curr):
    if curr < 0:
        return 0
    if dp[index][curr] != -1:
        return dp[index][curr]
    if index < N:
        res = 0
        for i in range(1,K + 1):
            res += solve(index + 1, curr - i)
            res %= M
        dp[index][curr] = res
    return dp[index][curr]

print(solve(0,T))
