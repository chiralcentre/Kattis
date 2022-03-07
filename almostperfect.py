from math import sqrt
from sys import stdin,stdout

def factors(n):
    step = 2 if n%2 else 1 #if number is odd, it cannot be divided by multiples of 2
    return set(factor for i in range(1,int(sqrt(n))+1,step) if not n%i for factor in (i,n//i)) #return all factors of n

for line in stdin:
    N = int(line)
    proper_sum = sum(factors(N)) - N
    stdout.write(f'{N} perfect\n') if proper_sum == N else stdout.write(f'{N} almost perfect\n') if -2 <= proper_sum - N <= 2 else stdout.write(f'{N} not perfect\n')
