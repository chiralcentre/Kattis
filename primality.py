from math import sqrt,floor

#credits to https://github.com/cheran-senthil/PyRival/blob/master/pyrival/algebra/is_prime.py
#this primality test follows the deterministic variant of the Miller test
#runs in O(log(n)^4)

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

print("YES") if isPrime(int(input())) else print("NO")
