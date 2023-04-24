from sys import stdin,stdout
from math import factorial,sqrt

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

def calculateExp(p,n):
    ans = 0
    while n // p > 0:
        ans += n // p
        n //= p
    return ans

#get list of primes from 0 to 431
sieve,count = SieveOfEratosthenes(432)
primes = [k for k in range(len(sieve)) if sieve[k]]
#Let e(p,n) = exponent of prime factor p in n!
#exponent of prime factor p in C(n,k) = e(p,n) - e(p,k) - e(p,n-k)
for line in stdin:
    n,k = map(int,line.split())
    counter = 1
    for p in primes:
        if p <= n:
            counter *= calculateExp(p,n) - calculateExp(p,k) - calculateExp(p,n - k) + 1
        else:
            break
    stdout.write(f"{counter}\n")

