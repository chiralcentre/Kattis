from math import sqrt,gcd
import sys

#prime factorisation 
def PrimeFactor(n):
    factors = {} #key is prime factor, value is exponent
    while not n%2:
        factors[2] = 1 if 2 not in factors else factors[2] +1
        n //= 2
    for i in range(3,int(sqrt(n))+1,2): #n must be odd now
        while not n%i:
            factors[i] = 1 if i not in factors else factors[i] + 1
            n //= i
    if n > 2: # if n is a prime number > 2
        factors[n] = 1
    return factors

for line in sys.stdin:
    n = int(line) 
    if n == 0:
        break
    positive = True if n > 0 else False
    exponents = list(PrimeFactor(abs(n)).values())
    res = exponents[0]
    for num in exponents[1:]:
        res = gcd(res,num)
    if positive or res%2: #gcd of exponents will return highest p such that x is a perfect pth power if x is positive
        print(res)
    else: #if x is negative, highest p must be odd and a factor of the gcd of exponents
        while not res%2: # if res is even, divide by 2 until it is odd; that will return highest odd factor
            res //= 2
        print(res)
    
