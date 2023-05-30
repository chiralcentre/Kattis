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

def isPrime(n):
    global primes
    for p in primes:
        if p * p <= n:
            if not n % p:
                return False
        else:
            break
    return True

primes = SieveOfEratosthenes(31630) #sqrt(10^9) = 31622.7766
while True:
    p,a = map(int,stdin.readline().split())
    if p == a == 0:
        break
    stdout.write("yes\n") if not isPrime(p) and pow(a,p,p) == a else stdout.write("no\n")
