from math import sqrt

def factorpair(n):
    factors = []
    for i in range(1,int(sqrt(n)) + 1):
        if not n%i:
            factors += [i-1,n//i-1] if i**2 != n else [i-1] #1 is subtracted to account for Benny
    return factors

N = int(input())
friends = sorted(factorpair(N))
print(' '.join(map(str,friends)))

