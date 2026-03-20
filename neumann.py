def neumann(n):
    if memo[n] != None:
        return memo[n]
    ans = []
    for i in range(n):
        ans.append(neumann(i))
    memo[n] = "{" + ",".join(ans) + "}"
    return memo[n]

memo = [None for _ in range(21)]
memo[0] = "{}"
n = int(input())
print(neumann(n))
