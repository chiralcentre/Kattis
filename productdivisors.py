from sys import stdin,stdout
from math import sqrt

H,MOD = pow(10,6) + 1,pow(10,9) + 7
#pf[i] stores the exponent of prime factor i in product
lst,pf = [i for i in range(H)],[0 for _ in range(H)]

def factorSieve(size):
    for i in range(3, size, 2):
        if i * i > size: break
        if lst[i] == i:
            for j in range(i * i, size, 2 * i):
                lst[j] = i
                
def primeFactorise(n):
    while not n % 2:
        pf[2] += 1
        n //= 2
    while n > 1:
        f = lst[n]
        while not n % f:
            pf[f] += 1
            n //= f
        
n = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))
factorSieve(H)
for k in nums:
    primeFactorise(k)
ans = 1
for v in pf:
    if v:
        ans *= v + 1
        ans %= MOD
stdout.write(f"{ans}\n")
