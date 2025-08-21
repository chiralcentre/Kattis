def is_prime(n):
    """returns True if n is prime else False"""
    if n < 5 or n & 1 == 0 or n % 3 == 0:
        return 2 <= n <= 3
    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or a % n == 0:
            continue
        for _ in range(s):
            p = (p * p) % n
            if p == n - 1:
                break
        else:
            return False
    return True

def digit_sum(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

n = int(input())
is_num_prime,is_ds_prime = is_prime(n),is_prime(digit_sum(n))
if is_num_prime:
    print("ADDITIVE PRIME") if is_ds_prime else print("PRIME, BUT NOT ADDITIVE")
else:
    print("COMPOSITE")
