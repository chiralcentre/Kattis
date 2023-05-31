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

primes = SieveOfEratosthenes(32000)
primeSet = set(primes)
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    ans = []
    for p in primes:
        if p <= n // 2:
            if n - p in primeSet:
                ans.append(f"{p}+{n-p}\n")
        else:
            break
    stdout.write(f"{n} has {len(ans)} representation(s)\n")
    for l in ans:
        stdout.write(l)
    stdout.write("\n")
    
