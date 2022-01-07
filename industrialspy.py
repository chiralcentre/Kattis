from math import sqrt
from itertools import permutations

def PrimeNumber(n):
    if n == 1 or n == 0:
        return False
    for i in range(2,int(sqrt(n))+1):
        if not n%i:
            return False
    return True

for _ in range(int(input())):
    string = input().strip()
    # check all possible permutations of digits in the given string
    substrings = set([int(''.join(L)) for i in range(1,len(string)+1) for L in permutations(string,i)]) #use a set to remove duplicate numbers
    primes = 0
    for num in substrings:
        if PrimeNumber(num):
            primes += 1
    print(primes)
    
