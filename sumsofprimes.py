def SieveOfEratosthenes(n): #high memory requirements
    primes = [True for i in range(n+1)] #if p[i] == true, i is prime else false
    p,count = 2,n+1
    while p * p <= n:
        if primes[p]: 
            for i in range(p * p, n + 1, p):
                if primes[i]:
                    count -= 1
                primes[i] = False
        p += 1
    primes[0],primes[1] = False,False #0 and 1 are not prime numbers
    return primes,count-2 #exclude 0 and 1

n = int(input())
if n < 2:
    print(0)
else:
    sieve,_ = SieveOfEratosthenes(n - 1)
    total = 0
    for i in range(1,n):
        if sieve[i]:
            total += i
    print(total)
