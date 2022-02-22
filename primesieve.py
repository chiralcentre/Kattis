from sys import stdin,stdout
from math import sqrt
from bitarray import bitarray
# Runtime error in Kattis as Kattis does not have bitarray preinstalled
def SieveOfEratosthenes(n):
    # bit arrays are used for one byte storage of booleans
    primes = (n+1)*bitarray('1') #if p[i] == true, i is prime else false
    p,count = 2,n+1
    while (p * p <= n):
        if (primes[p]): 
            for i in range(p**2, n + 1, p):
                if primes[i]:
                    count -= 1
                primes[i] = False
        p += 1
    primes[0],primes[1] = False,False #0 and 1 are not prime numbers
    return primes,count-2 #exclude 0 and 1

n,t = map(int,stdin.readline().split())
primes,primeNum = SieveOfEratosthenes(n)
stdout.write(f'{primeNum} \n')
for _ in range(t):
    stdout.write('1'+'\n') if primes[(int(stdin.readline()))] else stdout.write('0'+'\n')

