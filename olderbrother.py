MAX = 1000000000
#use Miller Rabin's test to check if the number is prime in O(log q) time
def isPrime(n):
    if n < 5 or n & 1 == 0 or not n % 3:
        return 2 <= n <= 3
    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or not a % n:
            continue
        #for else construct: if p != n - 1 for i in range(s), return false
        for _ in range(s):
            p = (p * p) % n
            if p == n - 1:
                break
        else:
            return False
    return True

def SieveOfEratosthenes(n): #high memory requirements
    primes = [True for i in range(n+1)] #if p[i] == true, i is prime else false
    p = 2
    while p * p <= n:
        if primes[p]: 
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    primes[0],primes[1] = False,False #0 and 1 are not prime numbers
    return [i for i in range(n + 1) if primes[i]]

primes = SieveOfEratosthenes(31630) #sqrt(10^9) ~= 31622
finite_fields = set()
for p in primes:
    prod = p
    while prod <= MAX:
        prod *= p
        finite_fields.add(prod)
q = int(input())
print("yes") if isPrime(q) or q in finite_fields else print("no")
    
