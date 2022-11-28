from sys import stdin,stdout
from math import sqrt

def PrimeFactor(n): #exponent form
    factors = {}
    while not n%2:
        factors[2] = factors[2] + 1 if 2 in factors else 1
        n //= 2
    for i in range(3,int(sqrt(n))+1,2): #n must be odd now
        while not n%i:
            factors[i] = factors[i] + 1 if i in factors else 1
            n //= i
    if n > 2: # if n is a prime number > 2
        factors[n] = 1
    return factors

for line in stdin:
    n = int(line)
    factors = PrimeFactor(n)
    neighbor = 1
    for key,value in factors.items():
        neighbor *= value ** key
    stdout.write(f"{n} {neighbor}\n")
