from sys import stdin,stdout

def SieveOfEratosthenes(n):
    primes = [True for i in range(n+1)] #if p[i] == true, i is prime else false
    p = 2
    while p * p <= n:
        if primes[p]: 
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    primes[0],primes[1] = False,False #0 and 1 are not prime numbers
    #return list of primes
    return [i for i in range(n + 1) if primes[i]]

def PrimeFactor(n): #exponent form
    global primes
    factors = {}
    for p in primes:
        if n < 2: break # early termination
        if not n % p: factors[p] = 0
        while not n % p:
            factors[p] += 1
            n //= p
    if n > 2:
        factors[n] = 1
    return factors

primes = SieveOfEratosthenes(46350) #sqrt(2^31 - 1) = 46340.95
for line in stdin:
    num = int(line)
    positive = num > 0
    ans = []
    if not positive:
        num = -num
        ans.append("-1")
    for k,v in PrimeFactor(num).items():
        ans.append(f"{k}^{v}") if v > 1 else ans.append(str(k))
    stdout.write(" ".join(s for s in ans))
    stdout.write("\n")
