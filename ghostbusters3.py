from math import comb

n,m = map(int,input().split())
MOD = pow(10,9) + 7
#m > n, there are n - 1 partitions for ghostbusters and m - 1 partitions for ghosts
print(comb(m,n) % MOD) if n <= m else print(comb(n - 1, m - 1) % MOD)
