from sys import stdin,setrecursionlimit

setrecursionlimit(200000)

def dp(participate_before,i):
    if i >= n:
        return 0
    if memo[participate_before][i] != -1:
        return memo[participate_before][i]
    if participate_before:
        not_take = dp(not participate_before, i + 1)
        take = dp(participate_before, i + 1) + a[i]
        result = min(not_take,take)
    else:
       result = dp(True, i + 1) + a[i]
    memo[participate_before][i] = result
    return result

n = int(stdin.readline())
a = list(map(int,stdin.readline().split()))
memo = [[-1 for i in range(n)] for j in range(2)]
print(dp(True,0))
