from sys import stdin,setrecursionlimit

setrecursionlimit(2000)
# note that you never need to exchange more than 9 coins of value 10^k, because for 10 exchanges we can use a single 10^(k + 1) coin
# maximum 1000 calls needed
# consider 1254x. If we can do 12540 in a exchanges, and 12550 in b, then we can do min(a + x, b + 10 - x)
memo = {0 : 0}
def solve(s):
    if s in memo: return memo[s]
    d = s % 10
    a = d + solve(s // 10) if d < 5 else 10 - d + solve(s // 10 + 1) if d > 5 else 5 + min(solve(s // 10), solve(s // 10 + 1))
    memo[s] = a
    return a

print(solve(int(stdin.readline())))
