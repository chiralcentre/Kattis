from math import gcd,sqrt,floor
# find largest x where x * (x + 1) / 2 < n -> x ^ 2 + x < 2n
# x ^ 2 + x < 2n -> x ^ 2 + x - 2n < 0
n = int(input())
x = floor((-1 + sqrt(1 + 8 * n)) / 2)
t = (x * x + x) // 2
base = x if t == n else x + 1
num = n - t - 1 if t != n else base - 1
if num == 0:
    print(base)
else:
    print(f"{base} {num // gcd(num, base)}/{(base) // gcd(num, base)}")
