def is_prime(n):
    """returns True if n is prime else False"""
    if n < 5 or n & 1 == 0 or n % 3 == 0:
        return 2 <= n <= 3
    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or a % n == 0:
            continue
        for _ in range(s):
            p = (p * p) % n
            if p == n - 1:
                break
        else:
            return False
    return True

def sieve_of_eratosthenes(n): #high memory requirements
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

def solve(primes,R):
    for p in primes:
        if is_prime(R - p):
            return f"3 {p} {R - p}"
    raise Exception("not supposed to happen")

# All odd numbers greater than 5 can be written as the sum of three primes. -> use 3 as one prime, and reduce to proposition that all even numbers greater than 2 can be written as the sum of two primes
N = int(input())
R = N - 3
sieve,count = sieve_of_eratosthenes(10000) # gather primes < 10000 for trial and error
primes = [i for i in range(len(sieve)) if sieve[i]]
print(solve(primes,R))
