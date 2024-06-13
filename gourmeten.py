# runs in O(MN) time
M = int(input())
T = [int(input()) for _ in range(int(input()))]
dp = [0 for _ in range(M + 1)]
dp[0] = 1
for i in range(1, M + 1):
    for t in T:
        if t <= i:
            dp[i] += dp[i - t]
print(dp[M])
