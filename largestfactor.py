from math import sqrt

# runs in O(sqrt(n)) time
def PrimeFactor(n):
    factors = []
    while not n%2:
        factors.append(2)
        n //= 2
    for i in range(3,int(sqrt(n))+1,2): #n must be odd now
        while not n%i:
            factors.append(i)
            n //= i
    if n > 2: # if n is a prime number > 2
        factors.append(n)
    return factors

n = int(input())
pf = PrimeFactor(n)
print(pf[-1])
