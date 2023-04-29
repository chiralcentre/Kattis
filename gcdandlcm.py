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

def genPossible():
    global collated,possible
    for k,v in collated.items():
        if possible:
            temp = set()
            for p in possible:
                temp.add(p * pow(k,v[0]))
                temp.add(p * pow(k,v[1]))
            possible = temp
        else:
            possible.add(pow(k,v[0]))
            possible.add(pow(k,v[1]))
        
x,y = map(int,stdin.readline().split())
#get prime factorisation of x and y
xf,yf = PrimeFactor(x),PrimeFactor(y)
#note that product of the first 13 primes > 10^14, so maximum number of prime factors for each number is 13
#collated[i] contains the min and max exponent for prime factor i in both xf and yf
collated = {}
for f,v in xf.items():
    collated[f] = [v]
    if f not in yf: #exponent of 0 to indicate absence
        collated[f].append(0)
for f,v in yf.items():
    if f not in collated:
        collated[f] = [v]
    else:
        collated[f].append(v)
    if f not in xf:
        collated[f].append(0)
#add in factor of 1, in case both a and b are coprime
collated[1] = [1,1]
#generate all possible pairs (maximum of 2^14 pairs)
possible = set() #use set to remove duplicates
genPossible()
possible = sorted(possible)
#product of LCM and GCD = product of two numbers
for a in possible:
    stdout.write(f"{a} {(y // a) * x}\n")
