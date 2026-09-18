from sys import stdin,stdout
from math import isqrt

#use Miller Rabin's test to check if the number is prime in O(log n) time
def isPrime(n):
    if n < 5 or n & 1 == 0 or not n % 3:
        return 2 <= n <= 3
    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or not a % n:
            continue
        #for else construct: if p != n - 1 for i in range(s), return false
        for _ in range(s):
            p = (p * p) % n
            if p == n - 1:
                break
        else:
            return False
    return True

# numbers with exactly 6 divisors (3 positive, 3 negative) must be square of prime
for _ in range(int(stdin.readline())):
    raw_num = stdin.readline().strip()
    num = int(raw_num)
    b = isqrt(num)
    if b * b != num:
        continue
    if not isPrime(b):
        continue
    stdout.write(f"{raw_num}\n")
    
