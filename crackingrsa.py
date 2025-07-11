from sys import stdin,stdout
from math import sqrt

#prime factorisation code
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

for _ in range(int(stdin.readline())):
    n,e = map(int,stdin.readline().split())
    p,q = PrimeFactor(n) # should only have 2 numbers in the list
    f = (p - 1) * (q - 1)
    # brute force
    d = 1
    while (d * e - 1) % f:
        d += 1
    stdout.write(f"{d}\n")
