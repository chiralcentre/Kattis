from sys import stdin,stdout
 
# sp[i] stores smallest prime factor of i
def SieveOfEratosthenes(n):
    primes = [True for i in range(n+1)] #if p[i] == true, i is prime else false
    sp = [i for i in range(n + 1)]
    # all even numbers have smallest prime factor 2
    for i in range(4,n + 1,2):
        sp[i] = 2
        primes[i] = False
    for i in range(3,n + 1,2):
        if primes[i]:
            sp[i],j = i,i
            while j * i < n:
                if primes[j * i]:
                    primes[j * i] = False
                    sp[j * i] = i
                j += 1
    primes[0],primes[1] = False,False #0 and 1 are not prime numbers
    return primes,sp

# code runs in O(N log L) time, where L is the largest number
primes,sp = SieveOfEratosthenes(1000000)
n = int(stdin.readline())
nums,pf,exponents = [],[],{}
for i in range(n):
    num = int(stdin.readline())
    nums.append(num)
    factors = {}
    while num > 1:
        factors[sp[num]] = factors.get(sp[num],0)+ 1
        num //= sp[num]
    for k,v in factors.items():
        if k in exponents:
            exponents[k].append(v)
        else:
            exponents[k] = [v]
    pf.append(factors)

# For each number, compute how many additional factors it has above the baseline. The number with the smallest additional factors is the answer.
baseline = {}
for k in exponents:
    if len(exponents[k]) > 1:
        exponents[k].sort()
        # take second largest exponent for particular prime factor, which must appear in LCM regardless of number to be removed
        baseline[k] = exponents[k][-2]
        
ans,extra = 1000000,1000000
for i in range(n):
    factors,temp = pf[i],1
    for k,v in factors.items():
        if k in baseline:
            temp *= pow(k,max(v - baseline[k],0))
        else:
            temp *= pow(k,v)
    if temp < extra:
        ans,extra = nums[i],temp
    elif temp == extra and nums[i] < ans:
        ans = nums[i]

stdout.write(f"{ans}\n")
