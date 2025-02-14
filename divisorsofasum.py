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

def mergeDict(d1,d2):
    res = {}
    for key,value in d1.items():
        res[key] = value + d2.get(key,0)
    for key,value in d2.items():
        if key not in d1:
            res[key] = value
    return res

n = int(input())
# required sum is n(n + 1)/2
pf1,pf2 = PrimeFactor(n),PrimeFactor(n + 1)
overall_pf = mergeDict(pf1,pf2)
overall_pf[2] -= 1 # account for dividing by 2
ans = 1
for k,v in overall_pf.items():
    ans *= (v + 1)
print(ans)
