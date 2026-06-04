from sys import stdin

memo = [[0 for _ in range(1001)] for j in range(1001)]
def dp(s1,s2,i,j):
    global memo
    if i < 0 or j < 0:
        return 0
    if memo[i][j] != 0:
        return memo[i][j]
    if s1[i] != s2[j]:
        memo[i][j] = 0
    else:
        memo[i][j] = 1 + dp(s1,s2,i - 1,j - 1)
    return memo[i][j]

def solve(s1,s2):
    ans = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            ans = max(ans,dp(s1,s2,i,j))
    return ans
    
# problem decomposes to finding length of longest common substring between two strings once s2 is reversed
# code runs in O(n^2) time
s1,s2 = stdin.readline().strip(),stdin.readline().strip()
s2 = s2[::-1] # reverse s2
print(solve(s1,s2))
