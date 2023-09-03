from sys import stdin,stdout
from itertools import combinations
from math import gcd

n = int(stdin.readline())
#note that product of the first fifteen primes ~= 6 * 10^17 is the largest product of primes < 10^18
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
# let a be the value that maximises g(n) -> g(a) is maximum value
a,chosen = 1,0
for i in range(len(primes)):
    if a * primes[i] <= n:
        chosen = i + 1
        a *= primes[i]
    else:
        break
# use inclusion exclusion principle to find value of numerator
pf = [primes[i] for i in range(chosen)]
numerator = sum(a // p for p in pf)
for i in range(2,chosen + 1):
    m = 1 if i % 2 else -1
    for combi in combinations(pf,i):
        prod = 1
        for c in combi:
            prod *= c
        numerator += m * a // prod
hcf = gcd(numerator,a)
stdout.write(f"{numerator // hcf}/{a // hcf}\n")
