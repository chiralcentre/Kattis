from sys import stdin,stdout

def C(n,k):
    global memo
    if memo[n][k] != -1:
        return memo[n][k]
    if k == 0 or k == n:
        memo[n][k] = 1
        return 1
    if k > n:
        memo[n][k] = 0
        return 0
    memo[n][k] = (C(n - 1, k - 1) % MOD + C(n - 1, k) % MOD) % MOD
    return memo[n][k]

N,K = map(int,stdin.readline().split())
MOD = pow(10,9) + 7
memo = [[-1 for i in range(51)] for j in range(100001)]
#sort numbers in ascending number
#note that the ith number will be maximal in an array of K numbers if all other K - 1 numbers are located to its left
#hence, number of times ith number is maximal = C(i, K - 1) #assuming i is zero indexed
lst = sorted(map(int,stdin.readline().split()))
ans = 0
for i in range(N):
    ans += C(i, K - 1) * lst[i]
    ans %= MOD
stdout.write(f"{ans}\n")
