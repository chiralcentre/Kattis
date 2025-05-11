from sys import stdin

# bottom up DP in O(hw) time
h,w = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for _ in range(h)]
dp = [[0 for i in range(w)] for j in range(h)]
# top left corner is guaranteed to have no iron
for i in range(1,w):
    dp[0][i] = dp[0][i - 1] + (grid[0][i] == "I")
for i in range(1,h):
    dp[i][0] = dp[i - 1][0] + (grid[i][0] == "I")
for i in range(1,h):
    for j in range(1,w):
        dp[i][j] = max(dp[i][j - 1],dp[i - 1][j]) + (grid[i][j] == "I")
print(dp[h - 1][w - 1])
        
