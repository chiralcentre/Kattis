def SieveOfEratosthenes(n): #high memory requirements
    primes = [True for i in range(n+1)] #if p[i] == true, i is prime else false
    p,count = 2,n+1
    while p * p <= n:
        if primes[p]: 
            for i in range(p * p, n + 1, p):
                if primes[i]:
                    count -= 1
                primes[i] = False
        p += 1
    primes[0],primes[1] = False,False #0 and 1 are not prime numbers
    return primes,count-2 #exclude 0 and 1


n = int(input())
sieve,_ = SieveOfEratosthenes(n)
primes = [i for i in range(1,len(sieve)) if sieve[i]]
prime_set = set(primes)
ps = [0 for _ in range(len(primes))]
ps[0] = primes[0]
# note that sum of first 1152 primes is already greater than 5000000
# use naive double for loop
stop = -1
for i in range(1,len(ps)):
    ps[i] = ps[i - 1] + primes[i]
    if ps[i] > n:
        stop = i
        break
best,ans = -1,0
for i in range(stop):
    if ps[i] in prime_set and ps[i] < n and i > best:
        best,ans = i, ps[i]
        
for i in range(stop):
    for j in range(i + 1, stop):
        d = ps[j] - ps[i]
        if d in prime_set and d < n and j - i > best:
            best,ans = j - i,d
print(ans)

