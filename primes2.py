from sys import stdin,stdout
from math import gcd,sqrt

mappings = {"0": 0, "1": 1, "2": 2, "3": 3,
            "4": 4, "5": 5, "6": 6, "7": 7,
            "8": 8, "9": 9, "A": 10, "B": 11,
            "C": 12, "D": 13, "E": 14, "F": 15}

def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if not n%2:
        return False
    for i in range(3,int(sqrt(n))+1,2): #n must be odd now
        if not n%i:
            return False
    return True

#convert n from base x to base 10
def convert(n,x):
    return sum(mappings[n[i]] * pow(x,len(n) - i - 1) for i in range(len(n)))

for _ in range(int(stdin.readline())):
    bases = {2,8,10,16}
    n = stdin.readline().strip()
    for c in n:
        if c.isalpha():
            bases = {16}
            break
        if int(c) > 1:
            bases.discard(2)
        if int(c) > 7:
            bases.discard(8)
    denom = len(bases); num = sum(isPrime(convert(n,x)) for x in bases)
    g = gcd(num,denom)
    stdout.write(f"{num // g}/{denom // g}\n")
