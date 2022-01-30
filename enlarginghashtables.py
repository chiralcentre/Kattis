from math import sqrt
import sys

def isPrime(n):
    if n == 2:
        return True
    if not n%2:
        return False
    for i in range(3,int(sqrt(n))+1,2): #n must be odd now
        if not n%i:
            return False
    return True

for line in sys.stdin:
    N = int(line)
    if N == 0:
        break
    #all primes are odd except 2
    S = 2*N+1
    while not isPrime(S):
        S += 2
    print(S) if isPrime(N) else print(f'{S} ({N} is not prime)')

        
