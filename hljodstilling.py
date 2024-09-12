from sys import stdin
from itertools import combinations

# returns number of numbers divisible by divisors from 1 to upper, inclusive
# use inclusion exclusion principle
# there are at most 2^20 - 1 = 1048575 combinations of prime factors
def solve(upper, divisors, k):
    if upper == 0:
        return 0
    ans = 0
    for i in range(1,k + 1):
        for comb in combinations(divisors, i):
            # all factors are prime, LCM is product of all factors
            prod = 1
            for factor in comb:
                prod *= factor
            ans += pow(-1, i + 1) * (upper // prod)
    return ans
    
L,R,k = map(int,stdin.readline().split())
divisors = sorted(map(int,stdin.readline().split()))
print(solve(R, divisors, k) - solve(L - 1, divisors, k))
