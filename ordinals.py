from sys import stdin,stdout

memo = {0: "{}"}
def solve(n):
    if n in memo:
        return memo[n]
    start = "{"
    for i in range(n):
        start += solve(i)
        if i < n - 1: start += ","
    ans = start + "}"
    memo[n] = ans
    return ans

n = int(input())
stdout.write(solve(n))
stdout.write("\n")
