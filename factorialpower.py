from math import sqrt

def PrimeFactor(n): #exponent form
    factors = {}
    while not n%2:
        factors[2] = factors[2] + 1 if 2 in factors else 1
        n //= 2
    for i in range(3,int(sqrt(n))+1,2): #n must be odd now
        if n < 2: break #early termination
        while not n%i:
            factors[i] = factors[i] + 1 if i in factors else 1
            n //= i
    if n > 2: # if n is a prime number > 2
        factors[n] = 1
    return factors

#calculateExp(p,n) = exponent of prime factor p in n!
def calculateExp(p,n):
    ans = 0
    while n // p > 0:
        ans += n // p
        n //= p
    return ans

n,m = map(int,input().split())
#perform prime factorisation of n in O(sqrt(n)) time
pf = PrimeFactor(n)
ans = pow(10,14)
for p,v in pf.items():
    ans = min(ans, calculateExp(p,m) // v)
print(ans)

    
