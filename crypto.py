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

# runs in O(sqrt(N)) time
# find highest exponent in prime factorisation
N = int(input())
factors = PrimeFactor(N)
highest_exp,best = -1,pow(10,18)
for key,value in factors.items():
    if value > highest_exp:
        highest_exp,best = value,key
    elif value == highest_exp and key < best:
        best = key
print(best)
    
